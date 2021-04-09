"""Command Line Tool for automating tasks to transfer data between Strava and GSheets."""

# Standard Library
import os
import sys
from pprint import pprint

# Third Party Libraries
from dotenv import load_dotenv

# Our Libraries
from core.strava import StravaAPIWrapper

load_dotenv()


def main(args):
    """CLI entry point."""
    print(args)
    strava = StravaAPIWrapper(os.getenv("STRAVA_ACCESS_TOKEN"))
    pprint(strava.list_activities(perPage=5))


if __name__ == "__main__":
    main(sys.argv)
