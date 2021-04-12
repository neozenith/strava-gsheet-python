"""Command Line Tool for automating tasks to transfer data between Strava and GSheets."""

# Standard Library
import inspect
import os
import sys
import time
from pprint import pprint as pp
from typing import Dict, List

# Third Party Libraries
from dotenv import load_dotenv

# Our Libraries
from core.db import Database
from core.gsheet import GoogleSheetWrapper
from core.strava import StravaAPIWrapper

load_dotenv()


def _inspect_tasks(prefix):
    return {
        f[0].replace(prefix, ""): f[1]
        for f in inspect.getmembers(sys.modules["__main__"], inspect.isfunction)
        if f[0].startswith(prefix)
    }


def cmd_extract(args):
    """Task to extract Strava SummaryActivities and save to database."""
    strava = StravaAPIWrapper(
        os.getenv("STRAVA_CLIENT_ID"),
        os.getenv("STRAVA_CLIENT_SECRET"),
        os.getenv("STRAVA_CREDENTIALS_FILE"),
    )

    valid_args = ["before", "after", "page", "per_page", "before_days_ago", "after_days_ago"]
    kwargs = validate_args(args, valid_args)

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
    # Iterate all paginations until reach an empty page
    while len(activities) > 0:
        activities = strava.list_activities(page=page, **kwargs)
        print(f"page:{page} [{len(activities)}]")
        total = total + len(activities)
        page = page + 1
        all_activities = all_activities + activities
    pp([a["name"] for a in all_activities])
    print(f"TOTAL: {total}")

    db = Database(os.getenv("MONGO_CONNECTION_STRING"))
    result = db.save_activities(all_activities)
    pp(result)


def cmd_load(args):
    """Load VirtualRide Activities from Mongo to Google Sheets."""
    db = Database(os.getenv("MONGO_CONNECTION_STRING"))
    activities = list(db.get_activities({"type": {"$in": ["Ride", "VirtualRide"]}}))

    sheet = GoogleSheetWrapper(
        os.getenv("GOOGLE_SHEET_CREDENTIALS_FILE"),
        os.getenv("GOOGLE_SHEET_ID"),
        os.getenv("GOOGLE_SHEET_WORKSHEET"),
    )
    sheet.save_activities(activities)


def validate_args(args, valid_args):
    """Validate args in format '--key=value'."""
    return {
        arg.replace("--", "").split("=")[0]: arg.replace("--", "").split("=")[1]
        for arg in args
        if arg.startswith("--") and "=" in arg and arg.replace("--", "").split("=")[0] in valid_args
    }


if __name__ == "__main__":
    tasks = _inspect_tasks("cmd_")

    if len(sys.argv) >= 2 and sys.argv[1] in tasks.keys():
        tasks[sys.argv[1]](sys.argv[2:])
    else:
        print(f"Must provide a task from the following: {list(tasks.keys())}")
