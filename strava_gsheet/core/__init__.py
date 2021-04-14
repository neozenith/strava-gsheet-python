"""Core library functionality for Extract/Load tasks."""

# Standard Library
import os
import time
from pprint import pprint as pp
from typing import Dict, List

# Third Party Libraries
from dotenv import load_dotenv

from .db import Database
from .gsheet import GoogleSheetWrapper
from .strava import StravaAPIWrapper

load_dotenv()


def extract(**kwargs):
    """Task to extract Strava SummaryActivities and save to database."""

    # Allow relative date args to specify the exact epoch times.
    if "after_days_ago" in kwargs:
        kwargs["after"] = int(time.time()) - int(kwargs["after_days_ago"]) * 24 * 60 * 60
        del kwargs["after_days_ago"]

    if "before_days_ago" in kwargs:
        kwargs["before"] = int(time.time()) - int(kwargs["before_days_ago"]) * 24 * 60 * 60
        del kwargs["before_days_ago"]

    page = 1
    activities: List[Dict[str, str]] = [{}]
    all_activities: List[Dict[str, str]] = []
    total = 0
    db = Database(os.getenv("MONGO_CONNECTION_STRING"))
    strava = StravaAPIWrapper(
        os.getenv("STRAVA_CLIENT_ID"),
        os.getenv("STRAVA_CLIENT_SECRET"),
        db.get_credential("strava"),
        db.save_credentials,
    )

    # Iterate all paginations until reach an empty page
    while len(activities) > 0:
        activities = strava.list_activities(page=page, **kwargs)
        print(f"page:{page} [{len(activities)}]")
        total = total + len(activities)
        page = page + 1
        all_activities = all_activities + activities
    pp([a["name"] for a in all_activities])
    print(f"TOTAL: {total}")

    result = db.save_activities(all_activities)
    pp(result)
    return result


def load():
    """Load VirtualRide Activities from Mongo to Google Sheets."""
    db = Database(os.getenv("MONGO_CONNECTION_STRING"))
    activities = list(db.get_activities({"type": {"$in": ["Ride", "VirtualRide"]}}))

    sheet = GoogleSheetWrapper(
        db.get_credential("gsheet"),
        os.getenv("GOOGLE_SHEET_ID"),
        os.getenv("GOOGLE_SHEET_WORKSHEET"),
    )
    return sheet.save_activities(activities)


def sync(**kwargs):
    """Extract and Load data from Strava to Google Sheets in one action."""
    return [extract(**kwargs), load()]
