"""
A module containing the user class, responsible for managing the users
table in the database
"""

# External
import bcrypt

# Internal
from helpers.user_helper import format_user_details


class User:
    """
    A class to manage the user table in the database
    """

    def __init__(self, cursor):
        """
        A method which is called whenever the class is initialised
        and sets the database cursor
        :param cursor: Database cursor
        """
        self._cursor = cursor

    def create_table(self):
        """
        A method to create the users table
        """
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS
                             users(
                             user_id INTEGER PRIMARY KEY,
                             email TEXT NOT NULL,
                             username TEXT NOT NULL,
                             password TEXT NOT NULL,
                             kudos INTEGER,
                             fish_count INTEGER,
                             user_age INTEGER
                             )""")

        print("Users table created successfully.")

    def drop_table(self):
        """
        A method to drop the users table
        """
        self._cursor.execute("DROP TABLE users")
        print("Users table dropped successfully.")

    @staticmethod
    def _hash_password(password):
        """
        A method to hash a password
        :param password: Password to hash
        :return: Hashed password
        """
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    def create_user(self, email, username, password, kudos, fish_count, user_age):
        """
        A method to create a user
        :param email: User email
        :param username: User's username
        :param password: User's password
        :param kudos: User's money
        :param fish_count: Total amount of user's fish
        :param user_age: User's age
        """
        query = """
                INSERT INTO users(email, username, password, kudos, fish_count, user_age)
                VALUES(?, ?, ?, ?, ?, ?)
                """
        self._cursor.execute(query, [email, username, self._hash_password(password), kudos, fish_count, user_age])
        new_user_id = self._cursor.lastrowid

        print("User created successfully.")
        return new_user_id

    def get_user_by_username(self, username):
        """
        A method to get details of user
        :param username: username of user
        :return: User
        """
        query = "SELECT user_id, email, username FROM users WHERE username=?"
        return self._cursor.execute(query, [username]).fetchone()

    def get_user_by_id(self, user_id):
        """
        A method to get details of user
        :param user_id: user ID of user
        :return: User
        """
        query = "SELECT * FROM users WHERE user_id=?"
        return self._cursor.execute(query, [user_id]).fetchone()

    def get_user_by_email(self, email):
        """
        A method to get details of user
        :param email: email of user
        :return: User
        """
        query = "SELECT user_id, email, username, password FROM users WHERE email=?"
        try:
            user = self._cursor.execute(query, [email]).fetchone()
            return format_user_details(user)
        except TypeError:
            user = None
        return user

    def update_user_kudos_amount(self, user_id, amount):
        """
        A method to change the amount of kudos for a user
        :param user_id: The user_id of the user
        :param amount: The change in the amount of kudos
        """
        # Retrieve the current amount of kudos for the user
        user_query = """
                     SELECT kudos
                     FROM users
                     WHERE user_id = ?
                     """
        self._cursor.execute(user_query, (user_id,))
        current_kudos = self._cursor.fetchone()

        if current_kudos:
            current_kudos = current_kudos[0]  # Extract the kudos value from the fetched row
            new_kudos = current_kudos + amount  # Calculate the new kudos amount

            # Update the kudos amount in the database
            update_kudos_query = """
                                 UPDATE users
                                 SET kudos = ?
                                 WHERE user_id = ?
                                 """
            self._cursor.execute(update_kudos_query, (new_kudos, user_id))
        else:
            print(f"User with ID {user_id} not found.")

    def update_user_age(self, user_id):
        """
        A method to change the amount of kudos for a user
        :param user_id: The user_id of the user
        """
        # Retrieve the current amount of kudos for the user
        user_query = """
                     SELECT user_age
                     FROM users
                     WHERE user_id = ?
                     """
        self._cursor.execute(user_query, (user_id,))
        current_age = self._cursor.fetchone()

        if current_age:
            current_age = current_age[0]  # Extract the kudos value from the fetched row
            new_age = current_age + 1  # Add one to age

            # Update the kudos amount in the database
            update_age_query = """
                                 UPDATE users
                                 SET user_age = ?
                                 WHERE user_id = ?
                                 """
            self._cursor.execute(update_age_query, (new_age, user_id))
        else:
            print(f"User with ID {user_id} not found.")

    def update_users_fish(self, user_id):
        """
        A method to count and update the number of fish a user has
        :param user_id: The user_id of the user
        """

        query = """
                SELECT * FROM fish
                WHERE user_id = ?
                """
        query_result = self._cursor.execute(query, (user_id,)).fetchall()

        quantity_all = 0

        for result in query_result:
            quantity = result[4]
            quantity_all += quantity

        update_fish_query = """
                            UPDATE users
                            SET fish_count = ?
                            WHERE user_id = ?
                            """
        self._cursor.execute(update_fish_query, (quantity_all, user_id))

    def get_user_kudos_amount(self, user_id):
        """
        A method to change the amount of kudos for a user
        :param user_id: The user_id of the user
        """
        # Retrieve the current amount of kudos for the user
        user_query = """
                     SELECT kudos
                     FROM users
                     WHERE user_id = ?
                     """
        self._cursor.execute(user_query, (user_id,))
        current_kudos = self._cursor.fetchone()

        return int(current_kudos[0])
