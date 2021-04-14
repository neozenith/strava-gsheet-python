"""Command Line Tool for automating tasks to transfer data between Strava and GSheets."""

# Standard Library
import inspect
import sys

# Third Party Libraries
from dotenv import load_dotenv

# Our Libraries
from strava_gsheet.core import extract, load, sync

load_dotenv()


def _inspect_tasks(prefix):
    return {
        f[0].replace(prefix, ""): f[1]
        for f in inspect.getmembers(sys.modules["__main__"], inspect.isfunction)
        if f[0].startswith(prefix)
    }


def cmd_extract(args):
    """Task to extract Strava SummaryActivities and save to database."""
    valid_args = ["before", "after", "page", "per_page", "before_days_ago", "after_days_ago"]
    kwargs = _validate_args(args, valid_args)

    extract(**kwargs)


def cmd_load(args):
    """Load VirtualRide Activities from Mongo to Google Sheets."""
    load()


def cmd_sync(args):
    """Extract and Load data from Strava to Google Sheets in one action."""
    valid_args = ["before", "after", "page", "per_page", "before_days_ago", "after_days_ago"]
    kwargs = _validate_args(args, valid_args)
    sync(**kwargs)


def _validate_args(args, valid_args):
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
