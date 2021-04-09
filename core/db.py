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
