"""
A module containing the fish class, responsible for managing the fish
table in the database
"""
from helpers.fish_helper import get_fish_data_by_name


class Fish:
    """
    A class to manage the fish table in the database
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
        A method to create the fish table
        """
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS
                                     fish(
                                     fish_id INTEGER PRIMARY KEY,
                                     user_id INTEGER NOT NULL,
                                     name TEXT NOT NULL,
                                     fish_type TEXT NOT NULL,
                                     quantity INTEGER,
                                     current_age INTEGER,
                                     fertile BOOLEAN,
                                     current_weight INTEGER,
                                     current_value INTEGER,
                                     frozen BOOLEAN,
                                     FOREIGN KEY (user_id) REFERENCES users(user_id)
                            )""")

        print("Fish table created successfully.")

    def drop_table(self):
        """
        A method to drop the users table
        """
        self._cursor.execute("DROP TABLE fish")
        print("Fish table dropped successfully.")

    def create_fish(self, user_id, name, fish_type, quantity, current_age, fertile, current_weight, current_value, frozen):
        """
        A method to create a fish
        :param user_id: ID of the user owning the fish
        :param name: Fish name
        :param fish_type: Type of fish
        :param quantity: Quantity of fish
        :param current_age: Current age of fish
        :param fertile: Boolean of whether fish is fertile
        :param current_weight: Current weight of fish
        :param current_value: Current value of fish
        :param frozen: Boolean of whether fish is frozen
        """
        query = """
                INSERT INTO fish(
                user_id, name, fish_type, quantity, current_age, fertile, current_weight, current_value, frozen)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
        self._cursor.execute(
            query, [user_id, name, fish_type, quantity, current_age, fertile, current_weight, current_value, frozen])

        print("Fish created successfully.")

    def update_fish_age(self, user_id):
        """
        A method to update the age of the fish a user has
        :param user_id: The user_id of the user
        """

        query = """
                SELECT * FROM fish
                WHERE user_id = ? and frozen = ?
                """
        query_result = self._cursor.execute(query, (user_id, False)).fetchall()

        for result in query_result:
            new_age = result[5] + 1

            # Update the age of the fish in the database
            update_query = """
                                   UPDATE fish
                                   SET current_age = ?
                                   WHERE fish_id = ?
                                   """
            self._cursor.execute(update_query, (new_age, result[0]))

    def update_fertile_fish_status(self, user_id):
        """
        A method to update the fertility of the fish a user has
        :param user_id: The user_id of the user
        """

        query = """
                    SELECT fish_id, name, current_age, fertile
                    FROM fish
                    WHERE user_id = ?
                    """
        query_result = self._cursor.execute(query, (user_id,)).fetchall()

        for fish_id, name, current_age, fertile in query_result:
            if not fertile:
                fish_info = get_fish_data_by_name(name)
                if fish_info['pref_fertile_day'] is not None and current_age >= fish_info['pref_fertile_day']:
                    update_query = """
                                    UPDATE fish
                                    SET fertile = ?
                                    WHERE fish_id = ?
                                    """
                    self._cursor.execute(update_query, (True, fish_id))

    def get_fish_list_by_user_id(self, user_id, unfrozen):
        """
        A method to get all fish belonging to a specific user_id
        :param user_id: (integer) ID of user_id to search fish for
        :param unfrozen: Boolean of whether to fetch only unfrozen fish or all fish
        :return: Fish associated with that user_id
        """

        if unfrozen:
            query = """
                    SELECT * FROM fish
                    WHERE user_id = ? AND frozen = ?
                    """
            query_result = self._cursor.execute(query, (user_id, False)).fetchall()

        else:
            query = """
                    SELECT * FROM fish
                    WHERE user_id = ?
                    """
            query_result = self._cursor.execute(query, (user_id,)).fetchall()

        return query_result

    def remove_fish(self, fish_id):
        """
        A method to remove all fish belonging to a specific fish id
        :param fish_id: (integer) ID of fish

        """
        query = """
                DELETE FROM fish
                WHERE fish_id = ?
                """
        self._cursor.execute(query, [fish_id])

        print(f"Fish id: {fish_id} deleted successfully.")

    def get_fish_name_from_id(self, fish_id):
        """
        A method to retrieve fish name from ID
        :param fish_id: (integer) ID of fish
        """

        query = """
                SELECT name FROM fish
                WHERE fish_id = ?
                """
        name = self._cursor.execute(query, [fish_id])

        return name

    def check_existing_fish_entry(self, user_id, name, current_age, frozen):
        """
        A method to check for existing fish in the database with the same age
        :param user_id: ID of the user
        :param name: Name of fish
        :param current_age: Age of the fish
        :param frozen: Whether fish are frozen
        """

        query = """
            SELECT current_age FROM fish
            WHERE name = ? AND current_age = ? AND user_id = ? AND frozen = ?
        """

        query_result = self._cursor.execute(query, (name, current_age, user_id, frozen)).fetchall()

        exists = any(row[0] == current_age for row in query_result)

        return exists

    def update_quantity_fish(self, user_id, name, current_age, amount, frozen):
        """
        A method to update the quantity of fish based on their name and age
        :param user_id: ID of the user
        :param name: Name of fish
        :param current_age: Age of the fish
        :param amount: Quantity to update
        :param frozen: Boolean for whether fish are frozen
        """

        query_age = """
            SELECT fish_id, quantity FROM fish
            WHERE name = ? AND current_age = ? AND user_id = ? AND frozen = ?
            """
        query_result = self._cursor.execute(query_age, (name, current_age, user_id, frozen)).fetchall()

        if query_result:
            old_quantity = query_result[0][1]
            new_quantity = old_quantity + amount

            if new_quantity == 0:
                self.remove_fish(query_result[0][0])
            else:
                update_query = """
                    UPDATE fish
                    SET quantity = ?
                    WHERE fish_id = ?
                    """
                self._cursor.execute(update_query, (new_quantity, query_result[0][0]))

    def dynamic_fertile_fish_search(self, user_id, list_of_fish):
        """
        A method to update the quantity of fish based on their name and age
        :param user_id: ID of the user
        :param list_of_fish: List of fish to create the where condition
        """

        where_conditions = [
            f"(name = '{name}' AND user_id = {user_id} AND fertile = 1)" for name in list_of_fish
        ]
        where_clause = ' OR '.join(where_conditions)

        query = f"""
                SELECT name FROM fish
                WHERE {where_clause}
                """

        filtered_fish_names = self._cursor.execute(query).fetchall()

        return filtered_fish_names

    def update_fish_weight_and_value(self, user_id):
        """
        A method to update the fertility of the fish a user has
        :param user_id: The user_id of the user
        """

        query = """
                SELECT fish_id, name, current_age
                FROM fish
                WHERE user_id = ?
                """

        query_result = self._cursor.execute(query, (user_id,)).fetchall()

        for fish_id, name, current_age in query_result:
            fish_info = get_fish_data_by_name(name)
            new_weight = fish_info['birth_weight'] + (fish_info['daily_weight_increase'] * current_age)
            if fish_info['sell_cost'] is not None:
                new_value = new_weight * fish_info['sell_cost']

                update_query = """
                               UPDATE fish
                               SET current_weight = ?, current_value = ?
                               WHERE fish_id = ?
                               """
                self._cursor.execute(update_query, (new_weight, new_value, fish_id))

    def dynamic_food_fish_search(self, user_id, list_of_fish):
        """
        A method to update the quantity of fish based on their name and age
        :param user_id: ID of the user
        :param list_of_fish: List of fish to create the where condition
        """

        where_conditions = [
            f"(name = '{name}' AND user_id = {user_id})" for name in list_of_fish
        ]
        where_clause = ' OR '.join(where_conditions)

        query = f"""
                SELECT * FROM fish
                WHERE {where_clause}
                """

        filtered_fish_names = self._cursor.execute(query).fetchall()

        return filtered_fish_names

    def check_fish_exists_and_quantity(self, fish_id):
        """
        A method to check for existing fish in the database with the same age
        :param fish_id: ID of fish
        """

        query = """
            SELECT quantity FROM fish
            WHERE fish_id = ? 
        """

        query_result = self._cursor.execute(query, (fish_id,)).fetchall()

        if query_result:
            return query_result[0]
        else:
            return None

    def get_fish_name_and_age(self, fish_id):
        """
        A method to check for existing fish in the database with the same age
        :param fish_id: ID of fish
        """

        query = """
            SELECT name, current_age FROM fish
            WHERE fish_id = ? 
        """

        query_result = self._cursor.execute(query, (fish_id,)).fetchall()

        if query_result:
            name, current_age = query_result[0]
            return name, current_age
        else:
            return None, None

    def freeze_fish(self, fish_id, quantity):
        """
        A method to freeze fish
        :param fish_id: ID of fish
        :param quantity: Amount of fish to freeze
        """

        fish_query = """
                     SELECT * from fish
                     WHERE fish_id = ?
                     """

        query_result = self._cursor.execute(fish_query, (fish_id,)).fetchone()

        if query_result is not None:

            if query_result[4] == quantity:
                if self.check_existing_fish_entry(query_result[1], query_result[2], query_result[5], True):
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], -quantity, False)
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], quantity, True)
                else:
                    update_query = """
                                   UPDATE fish
                                   SET frozen = ?
                                   WHERE fish_id = ?
                                   """
                    self._cursor.execute(update_query, (True, fish_id))

            else:
                self.update_quantity_fish(query_result[1], query_result[2], query_result[5], -quantity, False)
                if self.check_existing_fish_entry(query_result[1], query_result[2], query_result[5], True):
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], quantity, True)
                else:
                    self.create_fish(query_result[1], query_result[2], query_result[3], quantity,
                                     query_result[5], query_result[6], query_result[7], query_result[8], 1)

    def unfreeze_fish(self, fish_id, quantity):
        """
        A method to unfreeze fish
        :param fish_id: ID of fish
        :param quantity: Amount of fish to unfreeze
        """

        fish_query = """
                     SELECT * from fish
                     WHERE fish_id = ?
                     """

        query_result = self._cursor.execute(fish_query, (fish_id,)).fetchone()

        if query_result is not None:

            if query_result[4] == quantity:
                if self.check_existing_fish_entry(query_result[1], query_result[2], query_result[5], False):
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], -quantity, True)
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], quantity, False)
                else:
                    update_query = """
                                   UPDATE fish
                                   SET frozen = ?
                                   WHERE fish_id = ?
                                   """
                    self._cursor.execute(update_query, (False, fish_id))

            else:
                self.update_quantity_fish(query_result[1], query_result[2], query_result[5], -quantity, True)
                if self.check_existing_fish_entry(query_result[1], query_result[2], query_result[5], False):
                    self.update_quantity_fish(query_result[1], query_result[2], query_result[5], quantity, False)
                else:
                    self.create_fish(query_result[1], query_result[2], query_result[3], quantity,
                                     query_result[5], query_result[6], query_result[7], query_result[8], 0)

    def get_fish_list_based_on_name(self, name, user_id):
        """
        A method to unfreeze fish
        :param name: Name of fish
        :param user_id: The user_id owning the fish
        """

        fish_query = """
                     SELECT current_age FROM fish
                     WHERE user_id = ? AND quantity > ? AND name = ? AND fertile = ?
                     """

        fish_list = self._cursor.execute(fish_query, (user_id, 0, name, True)).fetchall()

        return fish_list
