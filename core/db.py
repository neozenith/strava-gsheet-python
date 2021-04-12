"""Database Wrapper.

This project uses MongoDB but the specific tasks should
be abstracted and independent of the underlying technology.
"""
# Third Party Libraries
from pymongo import MongoClient


class Database:
    """Abstraction layer for database used in this project."""

    def __init__(self, connection_string):
        """Initialize Database client with a connection string."""
        super().__init__()
        self.client = MongoClient(connection_string)

    def save_activities(self, activities):
        """Save list of Strava Activities to mongo activities collection."""
        db = self.client["workouttracker"]
        collection = db["activities"]
        output = []
        for activity in activities:
            name = activity["name"]
            try:
                output.append((name, collection.insert(activity)))
            except Exception as err:
                output.append((name, err))

        return output

    def get_activities(self, opts):
        """Get list of Workout Activities from mongo activities collection."""
        db = self.client["workouttracker"]
        collection = db["activities"]
        return collection.find(opts)
