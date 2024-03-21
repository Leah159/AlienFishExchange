"""
This module contains the database manager class.
This is responsible for managing database functionality
"""

# External
import sqlite3

# Internal
from users import User
from fish import Fish


class DatabaseManager:
    """
    Class to manage database functionality
    """

    def __init__(self, database):
        """
        A method which is called whenever the class is initialised
        and opens a connection to the database
        :param database: Database path
        """
        self._connection = sqlite3.connect(database)
        self._cursor = self._connection.cursor()
        self.users = User(self._cursor)
        self.fish = Fish(self._cursor)

    def __enter__(self):
        """
        A method called when a new instance of the
        DatabaseManager class is created
        :return: Self
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        A method called at the end of the use of a context
        manager to handle closing the database connection
        :param exc_type: Exception type
        :param exc_val: Exception value
        :param exc_tb: Exception traceback
        """
        self.get_database_changes()
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
        print("Disconnected from the database.")

    def get_database_version(self):
        """
        A method that queries the database for the sqlite version
        """
        version = self._cursor.execute("SELECT sqlite_version();").fetchall()
        print(f"Connected to the database successfully.\nSQLite version: {version[0][0]}")

    def get_database_changes(self):
        """
        A method to return the total changes made to the database
        """
        if self._connection.total_changes == 0:
            print("No changes were made to the database.")
        else:
            print(f"Total number of changes to the database: {self._connection.total_changes}")

    def create_tables(self):
        """
        A method to create all tables in the database
        """

        self.users.create_table()
        self.fish.create_table()

        print("Database tables created successfully.")

    def drop_tables(self):
        """
        A method to drop all tables from the database
        """

        self.users.drop_table()
        self.fish.drop_table()

        print("Database tables created successfully.")
