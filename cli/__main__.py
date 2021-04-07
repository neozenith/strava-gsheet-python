"""Command Line Tool for automating tasks to transfer data between Strava and GSheets."""

# Standard Library
import sys
from pprint import pprint

# Third Party Libraries
from dotenv import load_dotenv

# Our Libraries
from core import list_activities

load_dotenv()


def main(args):
    """CLI entry point."""
    print(args)
    pprint(list_activities(perPage=5))


if __name__ == "__main__":
    main(sys.argv)
