"""
A module for managing the game endpoint methods
"""
import math
import random

# Built-in
import requests.exceptions

# Internal
from config import Config
from db_manager import DatabaseManager
from helpers.fish_helper import get_fish_breeding, get_fish_data_by_name, get_fish_mutation, get_fish_food_list
from helpers.response_formatter import (
    format_error_response,
    format_ok_response
)

ResponseKeys = Config.GenericConfig.ResponseKeys
ResponseMessages = Config.GameConfig.ResponseMessages


def advance_day(user_id):
    """
    A function to handle the method for the user advancing the day
    :param user_id: ID of the user
    :return: Request response
    """

    try:
        with DatabaseManager(Config.GenericConfig.database_path) as database:
            database.get_database_version()
            database.users.update_user_age(user_id)
            database.fish.update_fish_age(user_id)
            database.fish.update_fertile_fish_status(user_id)
            database.fish.update_fish_weight_and_value(user_id)
            list_of_fish = database.fish.get_fish_list_by_user_id(user_id, True)
            food_log = feed_fish(database, user_id, list_of_fish)
            mutation_log = check_for_mutations(database, user_id, list_of_fish)
            breeding_log = check_for_breeding(database, user_id, list_of_fish)
            database.users.update_users_fish(user_id)

            response_log = {
                "food_log": food_log,
                "mutation_log": mutation_log,
                "breeding_log": breeding_log,
                "message": ResponseMessages.game_advanced_success
            }
            response = format_ok_response({ResponseKeys.message: response_log})

    except requests.exceptions.RequestException as error:
        response = format_error_response({ResponseKeys.error: error})
    return response


def check_for_mutations(database, user_id, list_of_fish):
    """
    A function to get all the fish from the user and check for mutations and handle them
    :param database: Instance of the database
    :param user_id: ID of the user
    :param list_of_fish: List of fish belonging to the user
    :return: Request response
    """

    mutation_log = ""
    for fish in list_of_fish:
        name = fish[2]
        fish_info = get_fish_data_by_name(name)
        if fish_info['mutation_day'] == fish[5]:
            new_fish_name, mutation_type = get_fish_mutation(name)
            if new_fish_name is not None:
                new_fish_info = get_fish_data_by_name(new_fish_name)
                if mutation_type == "one":
                    if database.fish.check_existing_fish_entry(user_id, new_fish_name, 0, False):
                        database.fish.update_quantity_fish(user_id, new_fish_name, 0, fish[4], False)
                    else:
                        current_value = new_fish_info['birth_weight'] * new_fish_info['sell_cost']
                        database.fish.create_fish(
                            user_id, new_fish_name, new_fish_info['fish_type'], fish[4],
                            0, False, new_fish_info['birth_weight'], current_value, 0)
                    mutation_log += f"{fish[4]} {fish[2]} mutated into {fish[4]} {new_fish_name}\n"
                else:
                    if database.fish.check_existing_fish_entry(user_id, new_fish_name, 0, False):
                        database.fish.update_quantity_fish(user_id, new_fish_name, 0, 1, False)
                    else:
                        current_value = new_fish_info['birth_weight'] * new_fish_info['sell_cost']
                        database.fish.create_fish(
                            user_id, new_fish_name, new_fish_info['fish_type'], 1, 0,
                            False, new_fish_info['birth_weight'], current_value, 0)
                    mutation_log += f"{fish[4]} {fish[2]} mutated into 1 {new_fish_name}\n"
            database.fish.remove_fish(fish[0])

    if mutation_log == "":
        mutation_log = "No fish mutated"
    return mutation_log


def check_for_breeding(database, user_id, list_of_fish):
    """
    A function to get all the fish from the user and check for breeding and handle them
    :param database: Instance of the database
    :param user_id: ID of the user
    :param list_of_fish: List of fish belonging to the user
    :return: Request response
    """

    breeding_log = ""
    new_fish_counts = {}
    condition_met = False

    for fish in list_of_fish:
        preferred = True
        quantity = 0
        fish_info = get_fish_data_by_name(fish[2])
        if fish[6] and fish_info['fertile_day'] is not None:
            if fish[5] >= fish_info['fertile_day']:
                preferred = False
            while quantity < fish[4]:
                new_fish_name, bred_with_fish = get_fish_breeding(database, user_id, fish[2], preferred)
                if new_fish_name != "":
                    condition_met = False
                    if bred_with_fish == fish[2] and fish[4] == 1:
                        fish_list = database.fish.get_fish_list_based_on_name(fish[2], user_id)
                        for fish_item in fish_list:
                            if fish_item[0] != fish[5]:
                                condition_met = True
                    else:
                        condition_met = True
                    if condition_met:
                        new_fish_info = get_fish_data_by_name(new_fish_name)
                        if database.fish.check_existing_fish_entry(user_id, new_fish_name, 0, False):
                            database.fish.update_quantity_fish(user_id, new_fish_name, 0, 1, False)
                        else:
                            current_value = new_fish_info['birth_weight'] * new_fish_info['sell_cost']
                            database.fish.create_fish(
                                user_id, new_fish_name, new_fish_info['fish_type'], 1, 0,
                                False, new_fish_info['birth_weight'], current_value, 0)
                        new_fish_counts[new_fish_name] = new_fish_counts.get(new_fish_name, 0) + 1
                quantity += 1

    for name, count in new_fish_counts.items():
        breeding_log += f"{count} {name} bred\n"

    if breeding_log == "":
        breeding_log = "No fish were bred"
    return breeding_log


def feed_fish(database, user_id, list_of_fish):
    """
    A function to get all the fish from the user and feed them
    :param database: Instance of the database
    :param user_id: ID of the user
    :param list_of_fish: List of fish belonging to the user
    :return: Request response
    """

    food_log = ""
    eaten_fish_counts = {}
    died_fish_counts = {}
    died_shop_counts = {}
    fish_food_cost = 0

    for fish in list_of_fish:
        fish_quantity = database.fish.check_fish_exists_and_quantity(fish[0])
        if fish_quantity is not None:
            quantity = 0
            target_quantity = fish_quantity[0]
            while quantity < target_quantity:
                hunger, style, prey_list = get_fish_food_list(fish[2])
                hunger_fraction = hunger / 100
                amount_to_eat = fish[7] * hunger_fraction

                if style == "shop":
                    cost_of_food = math.ceil(amount_to_eat)
                    user_kudos = database.users.get_user_kudos_amount(user_id)
                    if user_kudos > cost_of_food:
                        database.users.update_user_kudos_amount(user_id, -cost_of_food)
                        fish_food_cost += cost_of_food
                    else:
                        database.fish.update_quantity_fish(user_id, fish[2], fish[5], -1, False)
                        died_shop_counts[fish[2]] = died_shop_counts.get(fish[2], 0) + 1
                else:
                    # Initialize eaten fish tracking
                    eaten_fish = {
                        "fully_eaten": {},
                        "partially_eaten_fish_id": None,
                        "partially_eaten_quantity": 0
                    }
                    sorted_fish_list = []
                    eaten_amount = 0

                    fish_list = database.fish.dynamic_food_fish_search(user_id, prey_list)
                    if style == "smallest":
                        sorted_fish_list = sorted(fish_list, key=sort_key_smallest_to_largest)
                    if style == "largest":
                        sorted_fish_list = sorted(fish_list, key=sort_key_largest_to_smallest)
                    if style == "any":
                        sorted_fish_list = fish_list[:]
                        random.shuffle(sorted_fish_list)

                    # Iterate through the sorted fish list
                    for fish_to_eat in sorted_fish_list:
                        fish_id, name, amount, weight = fish_to_eat[0], fish_to_eat[2], fish_to_eat[4], fish_to_eat[7]

                        # Check if there is any fish left to eat
                        if amount_to_eat <= 0:
                            break

                        # Calculate how many fish to eat from this row
                        fish_to_eat = min(amount, math.ceil(amount_to_eat / weight))

                        # Update eaten amount and amount to eat
                        eaten_amount += fish_to_eat
                        amount_to_eat -= fish_to_eat * weight

                        # Update the quantity of this fish type
                        new_quantity = max(amount - fish_to_eat, 0)

                        # Update the eaten fish tracking
                        if new_quantity == 0:
                            eaten_fish["fully_eaten"][fish_id] = {"name": name, "eaten_quantity": amount}
                        elif eaten_fish["partially_eaten_fish_id"] is None:
                            eaten_fish["partially_eaten_fish_id"] = fish_id
                            eaten_fish["partially_eaten_quantity"] = amount - new_quantity

                    # Check if any partially eaten fish row reached zero
                    if eaten_fish["partially_eaten_fish_id"] and eaten_fish["partially_eaten_quantity"] == 0:
                        fully_eaten_fish_id = eaten_fish.pop("partially_eaten_fish_id")
                        eaten_fish["fully_eaten"].append(fully_eaten_fish_id)

                    if amount_to_eat > 0:
                        died_fish_counts[fish[2]] = died_fish_counts.get(fish[2], 0) + 1
                        database.fish.update_quantity_fish(user_id, fish[2], fish[5], -1, False)

                    for fish_id, fish_info in eaten_fish["fully_eaten"].items():
                        database.fish.remove_fish(fish_id)
                        eaten_fish_counts[fish_info["name"]] = eaten_fish_counts.get(fish_info["name"], 0) + fish_info[
                            "eaten_quantity"]

                    if eaten_fish["partially_eaten_quantity"] > 0:
                        name, age = database.fish.get_fish_name_and_age(eaten_fish["partially_eaten_fish_id"])
                        database.fish.update_quantity_fish(user_id, name, age, -eaten_fish["partially_eaten_quantity"], False)
                        eaten_fish_counts[name] = eaten_fish_counts.get(name, 0) + eaten_fish["partially_eaten_quantity"]

                quantity += 1

    for name, count in died_fish_counts.items():
        food_log += f"{count} {name} died of hunger\n"

    for name, count in eaten_fish_counts.items():
        food_log += f"{count} {name} eaten by another fish\n"

    food_log += f"{fish_food_cost} kudos spent buying fish food\n"

    for name, count in died_shop_counts.items():
        food_log += f"{count} {name} died from a lack of funds\n"

    return food_log


def sort_key_largest_to_smallest(fish):
    return -fish[7]


def sort_key_smallest_to_largest(fish):
    return fish[7]
