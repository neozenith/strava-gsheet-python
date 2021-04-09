"""Command Line Tool for automating tasks to transfer data between Strava and GSheets."""

# Standard Library
import inspect
import os
import sys
from pprint import pprint as pp

# Third Party Libraries
from dotenv import load_dotenv

# Our Libraries
from core.db import Database
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
        os.getenv("STRAVA_ACCESS_TOKEN"),
        os.getenv("STRAVA_REFRESH_TOKEN"),
    )
    db = Database(os.getenv("MONGO_CONNECTION_STRING"))

    activities = strava.list_activities(perPage=5)
    filtered = [_filtered_activity(a) for a in activities]
    result = db.save_activities(filtered)
    pp(result)


def _filtered_activity(activity):
    target_attributes = [
        "id",
        "name",
        "start_date_local",
        "moving_time",
        "elapsed_time",
        "type",
        "workout_type" "distance",
        "total_elevation_gain",
        "kilojoules",
        "average_speed",
        "max_speed",
        "average_watts",
        "max_watts",
        "weighted_average_watts",
    ]
    return {attr: getattr(activity, attr) for attr in activity.__dir__() if attr in target_attributes}


if __name__ == "__main__":
    tasks = _inspect_tasks("cmd_")

    if len(sys.argv) >= 2 and sys.argv[1] in tasks.keys():
        tasks[sys.argv[1]](sys.argv[2:])
    else:
        print(f"Must provide a task from the following: {list(tasks.keys())}")
