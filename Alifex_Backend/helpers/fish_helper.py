"""
A module containing the master table for the fish database
"""

# Built-in
import random

# Internal
from config import FishConfig

ResponseKeys = FishConfig.RequestKeys


fish_data = [
    {
        "fish_name": "White Sprat",
        "fish_type": "Sprat",
        "birth_weight": 1,
        "daily_weight_increase": 0.5,
        "mutation_day": 3,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": 2,
        "sell_cost": 1
    },
    {
        "fish_name": "Blue Sprat",
        "fish_type": "Sprat",
        "birth_weight": 2,
        "daily_weight_increase": 4,
        "mutation_day": 7,
        "pref_fertile_day": 1,
        "fertile_day": 6,
        "buy_cost": 51,
        "sell_cost": 2
    },
    {
        "fish_name": "Green Sprat",
        "fish_type": "Sprat",
        "birth_weight": 2,
        "daily_weight_increase": 3,
        "mutation_day": 5,
        "pref_fertile_day": 1,
        "fertile_day": 4,
        "buy_cost": 33,
        "sell_cost": 2
    },
    {
        "fish_name": "Red Sprat",
        "fish_type": "Sprat",
        "birth_weight": 2,
        "daily_weight_increase": 2,
        "mutation_day": 9,
        "pref_fertile_day": 1,
        "fertile_day": 8,
        "buy_cost": 29,
        "sell_cost": 2
    },
    {
        "fish_name": "Grey Sprat",
        "fish_type": "Sprat",
        "birth_weight": 15,
        "daily_weight_increase": 3,
        "mutation_day": 6,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": 60,
        "sell_cost": 3
    },
    {
        "fish_name": "Rainbow Sprat",
        "fish_type": "Sprat",
        "birth_weight": 30,
        "daily_weight_increase": 2,
        "mutation_day": 3,
        "pref_fertile_day": 1,
        "fertile_day": 2,
        "buy_cost": None,
        "sell_cost": 3
    },
    {
        "fish_name": "Ultra-violet Sprat",
        "fish_type": "Sprat",
        "birth_weight": 5,
        "daily_weight_increase": 2,
        "mutation_day": 3,
        "pref_fertile_day": 1,
        "fertile_day": 2,
        "buy_cost": None,
        "sell_cost": 3
    },
    {
        "fish_name": "Blazing Angelfish",
        "fish_type": "Angelfish",
        "birth_weight": 30,
        "daily_weight_increase": 12,
        "mutation_day": 13,
        "pref_fertile_day": 9,
        "fertile_day": 12,
        "buy_cost": 880,
        "sell_cost": 11
    },
    {
        "fish_name": "Coruscating Angelfish",
        "fish_type": "Angelfish",
        "birth_weight": 15,
        "daily_weight_increase": 8,
        "mutation_day": 13,
        "pref_fertile_day": 9,
        "fertile_day": 12,
        "buy_cost": 800,
        "sell_cost": 16
    },
    {
        "fish_name": "Iridescent Angelfish",
        "fish_type": "Angelfish",
        "birth_weight": 40,
        "daily_weight_increase": 25,
        "mutation_day": 7,
        "pref_fertile_day": 1,
        "fertile_day": 6,
        "buy_cost": None,
        "sell_cost": 15
    },
    {
        "fish_name": "Acute Angle Fish",
        "fish_type": "Angle Fish",
        "birth_weight": 900,
        "daily_weight_increase": 804,
        "mutation_day": 23,
        "pref_fertile_day": 9,
        "fertile_day": 22,
        "buy_cost": 142800,
        "sell_cost": 21
    },
    {
        "fish_name": "Bermuda Tri-Angle Fish",
        "fish_type": "Angle Fish",
        "birth_weight": 8790,
        "daily_weight_increase": 0,
        "mutation_day": 13,
        "pref_fertile_day": 7,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": 8
    },
    {
        "fish_name": "Blasphemous Angle Fish",
        "fish_type": "Angle Fish",
        "birth_weight": 999,
        "daily_weight_increase": 9699,
        "mutation_day": 6,
        "pref_fertile_day": 3,
        "fertile_day": 5,
        "buy_cost": None,
        "sell_cost": 16
    },
    {
        "fish_name": "Right Angle Fish",
        "fish_type": "Angle Fish",
        "birth_weight": 500,
        "daily_weight_increase": 78,
        "mutation_day": 17,
        "pref_fertile_day": 5,
        "fertile_day": 16,
        "buy_cost": 6417,
        "sell_cost": 7
    },
    {
        "fish_name": "Double Bass",
        "fish_type": "Bass",
        "birth_weight": 1000,
        "daily_weight_increase": 145,
        "mutation_day": 23,
        "pref_fertile_day": 17,
        "fertile_day": 22,
        "buy_cost": 18600,
        "sell_cost": 9
    },
    {
        "fish_name": "Drummen Bass",
        "fish_type": "Bass",
        "birth_weight": 1200,
        "daily_weight_increase": 159,
        "mutation_day": 43,
        "pref_fertile_day": 13,
        "fertile_day": 42,
        "buy_cost": None,
        "sell_cost": 90
    },
    {
        "fish_name": "Walking Bass",
        "fish_type": "Bass",
        "birth_weight": 200,
        "daily_weight_increase": 116,
        "mutation_day": 13,
        "pref_fertile_day": 7,
        "fertile_day": 12,
        "buy_cost": 5334,
        "sell_cost": 8
    },
    {
        "fish_name": "Manx Catfish",
        "fish_type": "Catfish",
        "birth_weight": 400,
        "daily_weight_increase": 100,
        "mutation_day": 9,
        "pref_fertile_day": 5,
        "fertile_day": 8,
        "buy_cost": 6000,
        "sell_cost": 9
    },
    {
        "fish_name": "Schrodingers Catfish",
        "fish_type": "Catfish",
        "birth_weight": 800,
        "daily_weight_increase": 200,
        "mutation_day": None,
        "pref_fertile_day": 1,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": 71
    },
    {
        "fish_name": "Siamese Catfish",
        "fish_type": "Catfish",
        "birth_weight": 100,
        "daily_weight_increase": 50,
        "mutation_day": 11,
        "pref_fertile_day": 7,
        "fertile_day": 10,
        "buy_cost": 1867,
        "sell_cost": 7
    },
    {
        "fish_name": "Heavenly Choirfish",
        "fish_type": "Choirfish",
        "birth_weight": 8989,
        "daily_weight_increase": 0,
        "mutation_day": 3,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": 236
    },
    {
        "fish_name": "Wailing Choirfish",
        "fish_type": "Choirfish",
        "birth_weight": 800,
        "daily_weight_increase": 350,
        "mutation_day": 11,
        "pref_fertile_day": 9,
        "fertile_day": 10,
        "buy_cost": 29500,
        "sell_cost": 15
    },
    {
        "fish_name": "Whistling Choirfish",
        "fish_type": "Choirfish",
        "birth_weight": 120,
        "daily_weight_increase": 94,
        "mutation_day": 23,
        "pref_fertile_day": 7,
        "fertile_day": 22,
        "buy_cost": 24400,
        "sell_cost": 30
    },
    {
        "fish_name": "Yodelling Choirfish",
        "fish_type": "Choirfish",
        "birth_weight": 1200,
        "daily_weight_increase": 441,
        "mutation_day": 13,
        "pref_fertile_day": 5,
        "fertile_day": 12,
        "buy_cost": 700134,
        "sell_cost": 236
    },
    {
        "fish_name": "Atomic Eel",
        "fish_type": "Eel",
        "birth_weight": 20000,
        "daily_weight_increase": 0,
        "mutation_day": None,
        "pref_fertile_day": 3,
        "fertile_day": 4,
        "buy_cost": None,
        "sell_cost": 5
    },
    {
        "fish_name": "Parasitic Eel",
        "fish_type": "Eel",
        "birth_weight": 500,
        "daily_weight_increase": 222,
        "mutation_day": 10,
        "pref_fertile_day": 4,
        "fertile_day": 9,
        "buy_cost": 65334,
        "sell_cost": 56
    },
    {
        "fish_name": "Recombinant Eel",
        "fish_type": "Eel",
        "birth_weight": 75,
        "daily_weight_increase": 91,
        "mutation_day": 10,
        "pref_fertile_day": 4,
        "fertile_day": 9,
        "buy_cost": 3500,
        "sell_cost": 10
    },
    {
        "fish_name": "Swarming Eel",
        "fish_type": "Eel",
        "birth_weight": 15,
        "daily_weight_increase": 165,
        "mutation_day": 10,
        "pref_fertile_day": 4,
        "fertile_day": 9,
        "buy_cost": 13260,
        "sell_cost": 26
    },
    {
        "fish_name": "Piranha-eating Eel",
        "fish_type": "Eel",
        "birth_weight": 975,
        "daily_weight_increase": 200,
        "mutation_day": None,
        "pref_fertile_day": 9,
        "fertile_day": 10,
        "buy_cost": 5500,
        "sell_cost": 1
    },
    {
        "fish_name": "Greater Europan Shark",
        "fish_type": "Europan Shark",
        "birth_weight": 3000,
        "daily_weight_increase": 666,
        "mutation_day": 19,
        "pref_fertile_day": 16,
        "fertile_day": 18,
        "buy_cost": 140000,
        "sell_cost": 20
    },
    {
        "fish_name": "Lesser Europan Shark",
        "fish_type": "Europan Shark",
        "birth_weight": 300,
        "daily_weight_increase": 1063,
        "mutation_day": 12,
        "pref_fertile_day": 9,
        "fertile_day": 11,
        "buy_cost": 8400,
        "sell_cost": 2
    },
    {
        "fish_name": "Pan Europan Shark",
        "fish_type": "Europan Shark",
        "birth_weight": 16000,
        "daily_weight_increase": 9333,
        "mutation_day": 25,
        "pref_fertile_day": 2,
        "fertile_day": 24,
        "buy_cost": None,
        "sell_cost": 18
    },
    {
        "fish_name": "Faded Grouper",
        "fish_type": "Grouper",
        "birth_weight": 52000,
        "daily_weight_increase": 1600,
        "mutation_day": 56,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": 18
    },
    {
        "fish_name": "Friendly Grouper",
        "fish_type": "Grouper",
        "birth_weight": 3000,
        "daily_weight_increase": 833,
        "mutation_day": 19,
        "pref_fertile_day": 10,
        "fertile_day": 18,
        "buy_cost": 120000,
        "sell_cost": 15
    },
    {
        "fish_name": "Legendary Grouper",
        "fish_type": "Grouper",
        "birth_weight": 52000,
        "daily_weight_increase": 7200,
        "mutation_day": 16,
        "pref_fertile_day": 10,
        "fertile_day": 15,
        "buy_cost": None,
        "sell_cost": 156
    },
    {
        "fish_name": "Rock Grouper",
        "fish_type": "Grouper",
        "birth_weight": 11000,
        "daily_weight_increase": 10200,
        "mutation_day": 6,
        "pref_fertile_day": 3,
        "fertile_day": 5,
        "buy_cost": 308000,
        "sell_cost": 11
    },
    {
        "fish_name": "Super Grouper",
        "fish_type": "Grouper",
        "birth_weight": 18000,
        "daily_weight_increase": 15000,
        "mutation_day": 6,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": 17
    },
    {
        "fish_name": "Support Grouper",
        "fish_type": "Grouper",
        "birth_weight": 7000,
        "daily_weight_increase": 1000,
        "mutation_day": 26,
        "pref_fertile_day": 7,
        "fertile_day": 25,
        "buy_cost": 322000,
        "sell_cost": 21
    },
    {
        "fish_name": "Kants Philosofish",
        "fish_type": "Philosofish",
        "birth_weight": 12,
        "daily_weight_increase": 21,
        "mutation_day": 9,
        "pref_fertile_day": 1,
        "fertile_day": 8,
        "buy_cost": 7276,
        "sell_cost": 107
    },
    {
        "fish_name": "Nietzsches Philosofish",
        "fish_type": "Philosofish",
        "birth_weight": 1,
        "daily_weight_increase": 9,
        "mutation_day": 17,
        "pref_fertile_day": 5,
        "fertile_day": 16,
        "buy_cost": None,
        "sell_cost": 280
    },
    {
        "fish_name": "Platos Philosofish",
        "fish_type": "Philosofish",
        "birth_weight": 5,
        "daily_weight_increase": 23,
        "mutation_day": 6,
        "pref_fertile_day": 1,
        "fertile_day": 5,
        "buy_cost": 260,
        "sell_cost": 6
    },
    {
        "fish_name": "Russells Philosofish",
        "fish_type": "Philosofish",
        "birth_weight": 80,
        "daily_weight_increase": 10,
        "mutation_day": 9,
        "pref_fertile_day": 1,
        "fertile_day": 8,
        "buy_cost": 2774,
        "sell_cost": 26
    },
    {
        "fish_name": "Invisible Piranha",
        "fish_type": "Piranha",
        "birth_weight": 1,
        "daily_weight_increase": 1,
        "mutation_day": 17,
        "pref_fertile_day": None,
        "fertile_day": None,
        "buy_cost": None,
        "sell_cost": None
    },
    {
        "fish_name": "Ionic Piranha",
        "fish_type": "Piranha",
        "birth_weight": 3,
        "daily_weight_increase": 6,
        "mutation_day": 8,
        "pref_fertile_day": 6,
        "fertile_day": 7,
        "buy_cost": 306,
        "sell_cost": 18
    },
    {
        "fish_name": "Jovian Piranha",
        "fish_type": "Piranha",
        "birth_weight": 5,
        "daily_weight_increase": 4,
        "mutation_day": 46,
        "pref_fertile_day": 25,
        "fertile_day": 45,
        "buy_cost": 8540,
        "sell_cost": 122
    },
    {
        "fish_name": "Nano-Piranha",
        "fish_type": "Piranha",
        "birth_weight": 1,
        "daily_weight_increase": 1,
        "mutation_day": 7,
        "pref_fertile_day": 4,
        "fertile_day": 6,
        "buy_cost": 24,
        "sell_cost": 9
    }
]


def get_fish_mutation(old_fish):
    """
    A function to hold the master table for the fish mutation details
    :param old_fish: The name of the fish to query
    :return: Fish formatted as an object
    """

    new_fish = ""
    mutation_type = ""

    if old_fish == "White Sprat":
        number = random.randint(1, 3)
        if number == 1:
            new_fish = "Red Sprat"
        if number == 2:
            new_fish = "Green Sprat"
        if number == 3:
            new_fish = "Blue Sprat"
        mutation_type = "one"

    if old_fish == "Blue Sprat":
        new_fish = "Grey Sprat"
        mutation_type = "one"

    if old_fish == "Green Sprat":
        new_fish = "Grey Sprat"
        mutation_type = "one"

    if old_fish == "Red Sprat":
        new_fish = "Grey Sprat"
        mutation_type = "one"

    if old_fish == "Grey Sprat":
        number = random.randint(1, 4)
        if number == 1:
            new_fish = None
        if number in [2, 3, 4]:
            new_fish = "Rainbow Sprat"
            mutation_type = "one"

    if old_fish == "Rainbow Sprat":
        number = random.randint(1, 5)
        if number in [1, 2]:
            new_fish = "Ultra-violet Sprat"
        if number == 3:
            new_fish = "Lesser Europan Shark"
        if number == 4:
            new_fish = "Coruscating Angelfish"
        if number == 5:
            new_fish = "Siamese Catfish"
        mutation_type = "school"

    if old_fish == "Ultra-violet Sprat":
        number = random.randint(1, 10)
        if number == 1:
            new_fish = "Whistling Choirfish"
            mutation_type = "one"
        if number == 2:
            new_fish = "Platos Philosofish"
            mutation_type = "one"
        if number == 3:
            new_fish = "Walking Bass"
            mutation_type = "one"
        if number == 4:
            new_fish = "Jovian Piranha"
            mutation_type = "one"
        if number == 5:
            new_fish = "Right Angle Fish"
            mutation_type = "one"
        if number == 6:
            new_fish = "Friendly Grouper"
            mutation_type = "school"
        if number in [7, 8, 9, 10]:
            new_fish = "Rainbow Sprat"
            mutation_type = "school"

    if old_fish == "Blazing Angelfish":
        new_fish = None

    if old_fish == "Coruscating Angelfish":
        new_fish = "Blazing Angelfish"
        mutation_type = "school"

    if old_fish == "Iridescent Angelfish":
        new_fish = "Coruscating Angelfish"
        mutation_type = "school"

    if old_fish == "Acute Angle Fish":
        number = random.randint(1, 2)
        if number == 1:
            new_fish = None
        if number == 2:
            new_fish = "Whistling Choirfish"
            mutation_type = "school"

    if old_fish == "Bermuda Tri-Angle Fish":
        number = random.randint(1, 2)
        if number == 1:
            new_fish = None
        if number == 2:
            new_fish = "Bermuda Tri-Angle Fish"
            mutation_type = "school"

    if old_fish == "Blasphemous Angle Fish":
        new_fish = None

    if old_fish == "Right Angle Fish":
        number = random.randint(1, 2)
        if number == 1:
            new_fish = "White Sprat"
            mutation_type = "school"
        if number == 2:
            new_fish = "Acute Angle Fish"
            mutation_type = "one"

    if old_fish == "Double Bass":
        new_fish = "Blazing Angelfish"
        mutation_type = "school"

    if old_fish == "Drummen Bass":
        new_fish = "Blasphemous Angle Fish"
        mutation_type = "one"

    if old_fish == "Walking Bass":
        new_fish = "Siamese Catfish"
        mutation_type = "school"

    if old_fish == "Manx Catfish":
        number = random.randint(1, 10)
        if number == 1:
            new_fish = "Siamese Catfish"
            mutation_type = "school"
        if number == 2:
            new_fish = "Jovian Piranha"
            mutation_type = "school"
        if number == 3:
            new_fish = "Recombinant Eel"
            mutation_type = "school"
        if number == 4:
            new_fish = "Schrodingers Catfish"
            mutation_type = "one"
        if number == 5:
            new_fish = "Friendly Grouper"
            mutation_type = "one"
        if number in [6, 7, 8, 9, 10]:
            new_fish = None

    if old_fish == "Siamese Catfish":
        new_fish = "Walking Bass"
        mutation_type = "school"

    if old_fish == "Heavenly Choirfish":
        new_fish = None

    if old_fish == "Wailing Choirfish":
        new_fish = None

    if old_fish == "Whistling Choirfish":
        number = random.randint(1, 4)
        if number in [1, 2]:
            new_fish = None
        if number == 3:
            new_fish = "Grey Sprat"
            mutation_type = "one"
        if number == 4:
            new_fish = "Wailing Choirfish"
            mutation_type = "one"

    if old_fish == "Yodelling Choirfish":
        new_fish = "Wailing Choirfish"
        mutation_type = "one"

    if old_fish == "Parasitic Eel":
        number = random.randint(1, 10)
        if number in [1, 2, 3, 4, 5, 6, 7, 8]:
            new_fish = None
        if number == 3:
            new_fish = "Recombinant Eel"
            mutation_type = "school"
        if number == 4:
            new_fish = "Piranha-eating Eel"
            mutation_type = "school"

    if old_fish == "Recombinant Eel":
        number = random.randint(1, 5)
        if number in [1, 2, 3, 4]:
            new_fish = None
        if number == 5:
            new_fish = "Swarming Eel"
            mutation_type = "school"

    if old_fish == "Swarming Eel":
        number = random.randint(1, 10)
        if number in [1, 2, 3, 4, 5, 6, 7, 8]:
            new_fish = None
        if number == 9:
            new_fish = "Recombinant Eel"
            mutation_type = "school"
        if number == 10:
            new_fish = "Parasitic Eel"
            mutation_type = "one"

    if old_fish == "Greater Europan Shark":
        new_fish = None

    if old_fish == "Lesser Europan Shark":
        new_fish = None

    if old_fish == "Pan Europan Shark":
        new_fish = None

    if old_fish == "Faded Grouper":
        new_fish = None

    if old_fish == "Friendly Grouper":
        number = random.randint(1, 5)
        if number in [1, 2, 3, 4]:
            new_fish = None
        if number == 5:
            new_fish = "Jovian Piranha"
            mutation_type = "school"

    if old_fish == "Legendary Grouper":
        number = random.randint(1, 10)
        if number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            new_fish = None
        if number == 10:
            new_fish = "Heavenly Choirfish"
            mutation_type = "school"

    if old_fish == "Rock Grouper":
        number = random.randint(1, 5)
        if number in [1, 2, 3, 4]:
            new_fish = None
        if number == 5:
            new_fish = "Super Grouper"
            mutation_type = "one"

    if old_fish == "Super Grouper":
        number = random.randint(1, 20)
        if number in [1, 2]:
            new_fish = None
        if number in [3, 4, 5, 6, 7, 8, 9]:
            new_fish = "Faded Grouper"
            mutation_type = "one"
        if number == 10:
            new_fish = "Legendary Grouper"
            mutation_type = "one"
        if number in [11, 12, 13, 14]:
            new_fish = "Rock Grouper"
            mutation_type = "school"
        if number in [15, 16]:
            new_fish = "Support Grouper"
            mutation_type = "school"
        if number in [17, 18]:
            new_fish = "Platos Philosofish"
            mutation_type = "school"
        if number in [19, 20]:
            new_fish = "Blasphemous Angle Fish"
            mutation_type = "school"

    if old_fish == "Support Grouper":
        number = random.randint(1, 5)
        if number in [1, 2, 3, 4]:
            new_fish = None
        if number == 5:
            new_fish = "Ionic Piranha"
            mutation_type = "school"

    if old_fish == "Kants Philosofish":
        new_fish = "Friendly Grouper"
        mutation_type = "one"

    if old_fish == "Nietzsches Philosofish":
        number = random.randint(1, 10)
        if number in [1, 2, 3, 4, 5]:
            new_fish = None
        if number == 6:
            new_fish = "Invisible Piranha"
            mutation_type = "one"
        if number == 7:
            new_fish = "Lesser Europan Shark"
            mutation_type = "one"
        if number == 8:
            new_fish = "Recombinant Eel"
            mutation_type = "school"
        if number == 9:
            new_fish = "Rainbow Sprat"
            mutation_type = "school"
        if number == 10:
            new_fish = "Grey Sprat"
            mutation_type = "school"

    if old_fish == "Platos Philosofish":
        new_fish = "Right Angle Fish"
        mutation_type = "one"

    if old_fish == "Russells Philosofish":
        new_fish = "Acute Angle Fish"
        mutation_type = "one"

    if old_fish == "Invisible Piranha":
        number = random.randint(1, 10)
        if number in [1, 2, 3, 4, 5]:
            new_fish = None
        if number == 6:
            new_fish = "Nietzsches Philosofish"
            mutation_type = "one"
        if number == 7:
            new_fish = "Schrodingers Catfish"
            mutation_type = "school"
        if number == 8:
            new_fish = "Bermuda Tri-Angle Fish"
            mutation_type = "school"
        if number == 9:
            new_fish = "Pan Europan Shark"
            mutation_type = "school"
        if number == 10:
            new_fish = "Rainbow Sprat"
            mutation_type = "one"

    if old_fish == "Ionic Piranha":
        new_fish = None

    if old_fish == "Jovian Piranha":
        new_fish = None

    if old_fish == "Nano-Piranha":
        new_fish = None

    return new_fish, mutation_type


def get_fish_data_by_name(name):
    for fish in fish_data:
        if fish["fish_name"] == name:
            return fish
    return None  # Return None if fish name is not found


def get_fish_breeding(database, user_id, name, preferred):

    new_fish = ""
    random_fish_name = ""

    if name == "Red Sprat":
        if preferred:
            list_of_fish = ["Red Sprat"]
        else:
            list_of_fish = ["Red Sprat", "Blue Sprat", "Green Sprat"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            # Randomly select one fish name from the filtered list
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Red Sprat":
                new_fish = "White Sprat"
            if random_fish_name == "Blue Sprat":
                new_fish = "Green Sprat"
            if random_fish_name == "Green Sprat":
                new_fish = "Blue Sprat"
        return new_fish, random_fish_name

    if name == "Green Sprat":
        if preferred:
            list_of_fish = ["Green Sprat"]
        else:
            list_of_fish = ["Red Sprat", "Blue Sprat", "Green Sprat"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Red Sprat":
                new_fish = "Blue Sprat"
            if random_fish_name == "Blue Sprat":
                new_fish = "Red Sprat"
            if random_fish_name == "Green Sprat":
                new_fish = "White Sprat"
        return new_fish, random_fish_name

    if name == "Blue Sprat":
        if preferred:
            list_of_fish = ["Blue Sprat"]
        else:
            list_of_fish = ["Red Sprat", "Blue Sprat", "Green Sprat"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Red Sprat":
                new_fish = "Green Sprat"
            if random_fish_name == "Blue Sprat":
                new_fish = "White Sprat"
            if random_fish_name == "Green Sprat":
                new_fish = "Red Sprat"
        return new_fish, random_fish_name

    if name == "Rainbow Sprat":
        list_of_fish = ["Blazing Angelfish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Blazing Angelfish":
                new_fish = "Iridescent Angelfish"
        return new_fish, random_fish_name

    if name == "Ultra-violet Sprat":
        list_of_fish = ["Wailing Choirfish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Blazing Angelfish":
        if preferred:
            list_of_fish = ["Rainbow Sprat"]
        else:
            list_of_fish = [
                "Rainbow Sprat", "Blazing Angelfish", "Whistling Choirfish",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Rainbow Sprat":
                new_fish = "Iridescent Angelfish"
            if random_fish_name == "Blazing Angelfish":
                new_fish = "Blazing Angelfish"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Coruscating Angelfish":
        if preferred:
            list_of_fish = ["Coruscating Angelfish"]
        else:
            list_of_fish = [
                "Coruscating Angelfish", "Whistling Choirfish", "Wailing Choirfish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Coruscating Angelfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Iridescent Angelfish":
        if preferred:
            list_of_fish = ["Iridescent Angelfish"]
        else:
            list_of_fish = [
                "Iridescent Angelfish", "Yodelling Choirfish", "Whistling Choirfish",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Iridescent Angelfish":
                new_fish = "Iridescent Angelfish"
            if random_fish_name == "Yodelling Choirfish":
                new_fish = "Heavenly Choirfish"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Acute Angle Fish":
        if preferred:
            list_of_fish = ["Acute Angle Fish"]
        else:
            list_of_fish = [
                "Acute Angle Fish", "Yodelling Choirfish", "Whistling Choirfish",
                "Wailing Choirfish", "Walking Bass", "Drummen Bass", "Double Bass",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Acute Angle Fish"
            if random_fish_name == "Yodelling Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Walking Bass":
                new_fish = "Walking Bass"
            if random_fish_name == "Drummen Bass":
                new_fish = "Walking Bass"
            if random_fish_name == "Double Bass":
                new_fish = "Walking Bass"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Blasphemous Angle Fish":
        if preferred:
            list_of_fish = ["Blasphemous Angle Fish"]
        else:
            list_of_fish = [
                "Blasphemous Angle Fish", "Atomic Eel", "Wailing Choirfish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Blasphemous Angle Fish":
                new_fish = "Bermuda Tri-Angle Fish"
            if random_fish_name == "Atomic Eel":
                new_fish = "Atomic Eel"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Yodelling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Right Angle Fish":
        if preferred:
            list_of_fish = ["Lesser Europan Shark", "Greater Europan Shark", "Pan Europan Shark",
                            "Coruscating Angelfish", "Blazing Angelfish", "Iridescent Angelfish",
                            "Whistling Choirfish", "Wailing Choirfish", "Yodelling Choirfish",
                            "Siamese Catfish", "Manx Catfish", "Walking Bass", "Drummen Bass",
                            "Double Bass", "Jovian Piranha", "Ionic Piranha", "Nano-Piranha",
                            "Recombinant Eel", "Swarming Eel", "Parasitic Eel", "Piranha-eating Eel",
                            "Atomic Eel", "Right Angle Fish", "Acute Angle Fish", "Blasphemous Angle Fish",
                            "Friendly Grouper", "Support Grouper", "Rock Grouper", "Legendary Grouper",
                            "Platos Philosofish", "Russells Philosofish", "Kants Philosofish"]
        else:
            list_of_fish = ["Lesser Europan Shark", "Greater Europan Shark", "Pan Europan Shark",
                            "Coruscating Angelfish", "Blazing Angelfish", "Iridescent Angelfish",
                            "Whistling Choirfish", "Wailing Choirfish", "Yodelling Choirfish",
                            "Siamese Catfish", "Manx Catfish", "Walking Bass", "Drummen Bass",
                            "Double Bass", "Jovian Piranha", "Ionic Piranha", "Nano-Piranha",
                            "Recombinant Eel", "Swarming Eel", "Parasitic Eel", "Piranha-eating Eel",
                            "Atomic Eel", "Right Angle Fish", "Acute Angle Fish", "Blasphemous Angle Fish",
                            "Friendly Grouper", "Support Grouper", "Rock Grouper", "Legendary Grouper",
                            "Platos Philosofish", "Russells Philosofish", "Kants Philosofish", "Whistling Choirfish",
                            "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name not in ["Whistling Choirfish", "Nietzsches Philosofish"]:
                new_fish = "Right Angle Fish"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Wailing Choirfish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Double Bass":
        if preferred:
            list_of_fish = ["Double Bass"]
        else:
            list_of_fish = [
                "Double Bass", "Wailing Choirfish", "Acute Angle Fish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Double Bass":
                new_fish = "Drummen Bass"
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Walking Bass"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Drummen Bass":
        if preferred:
            list_of_fish = ["Drummen Bass"]
        else:
            list_of_fish = [
                "Drummen Bass", "Rock Grouper", "Support Grouper", "Jovian Piranha",
                "Wailing Choirfish", "Acute Angle Fish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Drummen Bass":
                new_fish = "Super Grouper"
            if random_fish_name == "Rock Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Support Grouper":
                new_fish = "Jovian Piranha"
            if random_fish_name == "Jovian Piranha":
                new_fish = "Atomic Eel"
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Walking Bass"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Walking Bass":
        if preferred:
            list_of_fish = ["Walking Bass"]
        else:
            list_of_fish = [
                "Walking Bass", "Friendly Grouper", "Rock Grouper", "Support Grouper", "Legendary Grouper",
                "Siamese Catfish", "Wailing Choirfish", "Acute Angle Fish", "Right Angle Fish",
                "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Walking Bass":
                new_fish = "Walking Bass"
            if random_fish_name == "Friendly Grouper":
                new_fish = "Double Bass"
            if random_fish_name == "Rock Grouper":
                new_fish = "Double Bass"
            if random_fish_name == "Support Grouper":
                new_fish = "Double Bass"
            if random_fish_name == "Legendary Grouper":
                new_fish = "Double Bass"
            if random_fish_name == "Siamese Catfish":
                new_fish = "Walking Bass"
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Walking Bass"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Manx Catfish":
        if preferred:
            list_of_fish = ["Manx Catfish"]
        else:
            list_of_fish = [
                "Manx Catfish", "Jovian Piranha", "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Manx Catfish":
                new_fish = "Siamese Catfish"
            if random_fish_name == "Jovian Piranha":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Siamese Catfish":
        if preferred:
            list_of_fish = ["Siamese Catfish"]
        else:
            list_of_fish = [
                "Siamese Catfish", "Walking Bass", "Jovian Piranha", "Wailing Choirfish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Siamese Catfish":
                new_fish = "Manx Catfish"
            if random_fish_name == "Walking Bass":
                new_fish = "Siamese Catfish"
            if random_fish_name == "Jovian Piranha":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Wailing Choirfish":
        if preferred:
            list_of_fish = ["Wailing Choirfish"]
        else:
            list_of_fish = ["Wailing Choirfish", "Ultra-violet Sprat", "Lesser Europan Shark", "Greater Europan Shark",
                            "Pan Europan Shark", "Coruscating Angelfish", "Blazing Angelfish", "Iridescent Angelfish",
                            "Siamese Catfish", "Manx Catfish", "Schrodingers Catfish", "Walking Bass", "Drummen Bass",
                            "Double Bass", "Jovian Piranha", "Ionic Piranha", "Nano-Piranha", "Right Angle Fish",
                            "Acute Angle Fish", "Blasphemous Angle Fish", "Bermuda Tri-Angle Fish", "Friendly Grouper",
                            "Support Grouper", "Rock Grouper", "Legendary Grouper", "Platos Philosofish",
                            "Russells Philosofish", "Kants Philosofish", "Whistling Choirfish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name not in ["Wailing Choirfish", "Blasphemous Angle Fish", "Ultra-violet Sprat",
                                        "Ionic Piranha", "Nietzsches Philosofish"]:
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Wailing Choirfish"
            if random_fish_name == "Blasphemous Angle Fish":
                new_fish = "Yodelling Choirfish"
            if random_fish_name == "Ultra-violet Sprat":
                new_fish = "Yodelling Choirfish"
            if random_fish_name == "Ionic Piranha":
                new_fish = "Recombinant Eel"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Whistling Choirfish":
        if preferred:
            list_of_fish = ["Whistling Choirfish"]
        else:
            list_of_fish = ["Whistling Choirfish", "Coruscating Angelfish", "Blazing Angelfish", "Iridescent Angelfish",
                            "Right Angle Fish", "Acute Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Coruscating Angelfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Blazing Angelfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Iridescent Angelfish":
                new_fish = "Coruscating Angelfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Yodelling Choirfish":
        if preferred:
            list_of_fish = ["Yodelling Choirfish"]
        else:
            list_of_fish = ["Yodelling Choirfish", "Iridescent Angelfish", "Right Angle Fish",
                            "Acute Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Yodelling Choirfish":
                new_fish = "Yodelling Choirfish"
            if random_fish_name == "Iridescent Angelfish":
                new_fish = "Heavenly Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Acute Angle Fish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Atomic Eel":
        if preferred:
            list_of_fish = ["Blasphemous Angle Fish"]
        else:
            list_of_fish = [
                "Blasphemous Angle Fish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Blasphemous Angle Fish":
                new_fish = "Atomic Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Parasitic Eel":
        if preferred:
            list_of_fish = ["Parasitic Eel"]
        else:
            list_of_fish = [
                "Parasitic Eel", "Recombinant Eel", "Swarming Eel", "Piranha-eating Eel",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Parasitic Eel":
                new_fish = "Parasitic Eel"
            if random_fish_name == "Recombinant Eel":
                new_fish = "Parasitic Eel"
            if random_fish_name == "Swarming Eel":
                new_fish = "Parasitic Eel"
            if random_fish_name == "Piranha-eating Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Recombinant Eel":
        if preferred:
            list_of_fish = ["Recombinant Eel"]
        else:
            list_of_fish = [
                "Recombinant Eel", "Parasitic Eel", "Swarming Eel", "Piranha-eating Eel",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Recombinant Eel":
                new_fish = "Recombinant Eel"
            if random_fish_name == "Parasitic Eel":
                new_fish = "Parasitic Eel"
            if random_fish_name == "Swarming Eel":
                new_fish = "Swarming Eel"
            if random_fish_name == "Piranha-eating Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Swarming Eel":
        if preferred:
            list_of_fish = ["Swarming Eel"]
        else:
            list_of_fish = [
                "Swarming Eel", "Recombinant Eel", "Parasitic Eel", "Piranha-eating Eel",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Swarming Eel":
                new_fish = "Swarming Eel"
            if random_fish_name == "Recombinant Eel":
                new_fish = "Swarming Eel"
            if random_fish_name == "Parasitic Eel":
                new_fish = "Parasitic Eel"
            if random_fish_name == "Piranha-eating Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Piranha-eating Eel":
        if preferred:
            list_of_fish = ["Piranha-eating Eel"]
        else:
            list_of_fish = [
                "Piranha-eating Eel", "Swarming Eel", "Recombinant Eel", "Parasitic Eel",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Piranha-eating Eel":
                new_fish = "Atomic Eel"
            if random_fish_name == "Swarming Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Recombinant Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Parasitic Eel":
                new_fish = "Piranha-eating Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Greater Europan Shark":
        if preferred:
            list_of_fish = ["Lesser Europan Shark"]
        else:
            list_of_fish = [
                "Lesser Europan Shark", "Greater Europan Shark", "Wailing Choirfish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Lesser Europan Shark":
                new_fish = "Lesser Europan Shark"
            if random_fish_name == "Greater Europan Shark":
                new_fish = "Pan Europan Shark"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Lesser Europan Shark":
        if preferred:
            list_of_fish = ["Lesser Europan Shark"]
        else:
            list_of_fish = [
                "Lesser Europan Shark", "Greater Europan Shark", "Wailing Choirfish",
                "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Lesser Europan Shark":
                new_fish = "Greater Europan Shark"
            if random_fish_name == "Greater Europan Shark":
                new_fish = "Lesser Europan Shark"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Pan Europan Shark":
        if preferred:
            list_of_fish = ["Pan Europan Shark"]
        else:
            list_of_fish = [
                "Pan Europan Shark", "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Pan Europan Shark":
                new_fish = "Pan Europan Shark"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Friendly Grouper":
        if preferred:
            list_of_fish = ["Friendly Grouper"]
        else:
            list_of_fish = [
                "Friendly Grouper", "Legendary Grouper", "Schrodingers Catfish", "Walking Bass",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Friendly Grouper":
                new_fish = "Support Grouper"
            if random_fish_name == "Legendary Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Schrodingers Catfish":
                new_fish = "Bermuda Tri-Angle Fish"
            if random_fish_name == "Walking Bass":
                new_fish = "Double Bass"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Legendary Grouper":
        if preferred:
            list_of_fish = ["Friendly Grouper"]
        else:
            list_of_fish = [
                "Friendly Grouper", "Support Grouper", "Rock Grouper",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Friendly Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Support Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Rock Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Rock Grouper":
        if preferred:
            list_of_fish = ["Rock Grouper"]
        else:
            list_of_fish = [
                "Rock Grouper", "Legendary Grouper", "Support Grouper", "Walking Bass", "Drummen Bass",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Rock Grouper":
                new_fish = "Rock Grouper"
            if random_fish_name == "Legendary Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Support Grouper":
                new_fish = "Walking Bass"
            if random_fish_name == "Walking Bass":
                new_fish = "Double Bass"
            if random_fish_name == "Drummen Bass":
                new_fish = "Super Grouper"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Support Grouper":
        if preferred:
            list_of_fish = ["Support Grouper"]
        else:
            list_of_fish = [
                "Support Grouper", "Rock Grouper", "Legendary Grouper", "Walking Bass", "Drummen Bass",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Support Grouper":
                new_fish = "Rock Grouper"
            if random_fish_name == "Rock Grouper":
                new_fish = "Walking Bass"
            if random_fish_name == "Legendary Grouper":
                new_fish = "Super Grouper"
            if random_fish_name == "Walking Bass":
                new_fish = "Double Bass"
            if random_fish_name == "Drummen Bass":
                new_fish = "Jovian Piranha"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Kants Philosofish":
        if preferred:
            list_of_fish = ["Kants Philosofish"]
        else:
            list_of_fish = [
                "Kants Philosofish", "Platos Philosofish", "Russells Philosofish",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Kants Philosofish":
                new_fish = "Kants Philosofish"
            if random_fish_name == "Platos Philosofish":
                new_fish = "Blasphemous Angle Fish"
            if random_fish_name == "Russells Philosofish":
                new_fish = "Nietzsches Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Nietzsches Philosofish":
        if preferred:
            list_of_fish = ["Nietzsches Philosofish"]
        else:
            list_of_fish = [
                "Nietzsches Philosofish", "Lesser Europan Shark", "Greater Europan Shark", "Pan European Shark",
                "Coruscating Angelfish", "Blazing Angelfish", "Iridescent Angelfish", "Yodelling Choirfish",
                "Siamese Catfish", "Manx Catfish", "Walking Bass", "Drummen Bass", "Double Bass", "Jovian Piranha",
                "Ionic Piranha", "Nano-Piranha", "Recombinant Eel", "Swarming Eel", "Parasitic Eel",
                "Piranha-eating Eel", "Acute Angle Fish", "Blasphemous Angle Fish", "Friendly Grouper",
                "Support Grouper", "Rock Grouper", "Legendary Grouper", "Platos Philosofish", "Russells Philosofish",
                "Kants Philosofish", "Wailing Choirfish", "Right Angle Fish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name not in ["Nietzsches Philosofish", "Right Angle Fish", "Wailing Choirfish"]:
                new_fish = "Yodelling Choirfish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Nietzsches Philosofish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
        return new_fish, random_fish_name

    if name == "Platos Philosofish":
        if preferred:
            list_of_fish = ["Platos Philosofish"]
        else:
            list_of_fish = [
                "Platos Philosofish", "Kants Philosofish", "Russells Philosofish",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Platos Philosofish":
                new_fish = "Platos Philosofish"
            if random_fish_name == "Kants Philosofish":
                new_fish = "Blasphemous Angle Fish"
            if random_fish_name == "Russells Philosofish":
                new_fish = "Kants Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Russells Philosofish":
        if preferred:
            list_of_fish = ["Russells Philosofish"]
        else:
            list_of_fish = [
                "Russells Philosofish", "Platos Philosofish", "Kants Philosofish",
                "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Russells Philosofish":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Platos Philosofish":
                new_fish = "Kants Philosofish"
            if random_fish_name == "Kants Philosofish":
                new_fish = "Nietzsches Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Ionic Piranha":
        if preferred:
            list_of_fish = ["Ionic Piranha"]
        else:
            list_of_fish = [
                "Ionic Piranha", "Whistling Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Ionic Piranha":
                new_fish = "Nano-Piranha"
            if random_fish_name == "Whistling Choirfish":
                new_fish = "Recombinant Eel"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Jovian Piranha":
        if preferred:
            list_of_fish = ["Jovian Piranha"]
        else:
            list_of_fish = [
                "Jovian Piranha", "Drummen Bass", "Siamese Catfish", "Manx Catfish",
                "Schrodingers Catfish", "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Jovian Piranha":
                new_fish = "Ionic Piranha"
            if random_fish_name == "Drummen Bass":
                new_fish = "Atomic Eel"
            if random_fish_name == "Siamese Catfish":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Manx Catfish":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Schrodingers Catfish":
                new_fish = "Russells Philosofish"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name

    if name == "Nano-Piranha":
        if preferred:
            list_of_fish = ["Nano-Piranha"]
        else:
            list_of_fish = [
                "Nano-Piranha", "Wailing Choirfish", "Right Angle Fish", "Nietzsches Philosofish"]
        filtered_list = database.fish.dynamic_fertile_fish_search(user_id, list_of_fish)
        if filtered_list:
            random_fish_name = random.choice(filtered_list)[0]
            if random_fish_name == "Nano-Piranha":
                new_fish = "Invisible Piranha"
            if random_fish_name == "Wailing Choirfish":
                new_fish = "Whistling Choirfish"
            if random_fish_name == "Right Angle Fish":
                new_fish = "Right Angle Fish"
            if random_fish_name == "Nietzsches Philosofish":
                new_fish = "Yodelling Choirfish"
        return new_fish, random_fish_name


def get_fish_food_list(fish_name):
    """
    A function to hold the master table for the fish feeding details
    :param fish_name: The name of the fish to query
    :return: Fish formatted as an object
    """

    hunger = 0
    style = ""
    prey_list = []

    if fish_name == "Blazing Angelfish":
        hunger = 20
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat", "Yodelling Choirfish"]

    if fish_name == "Coruscating Angelfish":
        hunger = 30
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat", "Atomic Eel",
                     "Parasitic Eel", "Piranha-Eating Eel", "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Iridescent Angelfish":
        hunger = 10
        style = "largest"
        prey_list = ["Acute Angle Fish", "Bermuda Tri-Angle Fish", "Blasphemous Angle Fish", "Right Angle Fish"]

    if fish_name == "Acute Angle Fish":
        hunger = 10
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Bermuda Tri-Angle Fish":
        hunger = 30
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat", "Ultra-violet Sprat",
                     "White Sprat", "Jovian Piranha", "Russells Philosofish", "Lesser Europan Shark",
                     "Acute Angle Fish", "Right Angle Fish", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish"]

    if fish_name == "Blasphemous Angle Fish":
        hunger = 30
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat", "Ultra-violet Sprat",
                     "White Sprat", "Jovian Piranha", "Russells Philosofish", "Lesser Europan Shark",
                     "Acute Angle Fish", "Right Angle Fish", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish"]

    if fish_name == "Right Angle Fish":
        hunger = 10
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Double Bass":
        hunger = 10
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Drummen Bass":
        hunger = 20
        style = "largest"
        prey_list = ["Lesser Europan Shark", "Kants Philosofish", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Blazing Angelfish", "Coruscating Angelfish", "Iridescent Angelfish"]

    if fish_name == "Walking Bass":
        hunger = 20
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Manx Catfish":
        hunger = 30
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Schrodingers Catfish":
        hunger = 30
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Siamese Catfish":
        hunger = 20
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat"]

    if fish_name == "Heavenly Choirfish":
        hunger = 10
        style = "smallest"
        prey_list = ["Greater Europan Shark", "Lesser Europan Shark", "Pan Europan Shark", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Invisble Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha",
                     "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel", "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Wailing Choirfish":
        hunger = 30
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish"]

    if fish_name == "Whistling Choirfish":
        hunger = 30
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish"]

    if fish_name == "Yodelling Choirfish":
        hunger = 10
        style = "smallest"
        prey_list = ["Wailing Choirfish", "Whistling Choirfish",
                     "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish"]

    if fish_name == "Atomic Eel":
        hunger = 100
        style = "any"
        prey_list = ["Atomic Eel"]

    if fish_name == "Parasitic Eel":
        hunger = 20
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Right Angle Fish", "Kants Philosofish",
                     "Nietzsches Philosofish", "Platos Philosofish", "Russells Philosofish", "Heavenly Choirfish",
                     "Wailing Choirfish", "Whistling Choirfish", "Yodelling Choirfish", "Double Bass", "Drummen Bass",
                     "Walking Bass", "Blazing Angelfish", "Coruscating Angelfish", "Iridescent Angelfish"]

    if fish_name == "Piranha-eating Eel":
        hunger = 10
        style = "smallest"
        prey_list = ["Invisible Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha"]

    if fish_name == "Recombinant Eel":
        hunger = 10
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat", "Double Bass", "Walking Bass", "Drummen Bass"]

    if fish_name == "Swarming Eel":
        hunger = 30
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat",
                     "Red Sprat", "Ultra-violet Sprat", "White Sprat", "Double Bass", "Walking Bass", "Drummen Bass"]

    if fish_name == "Greater Europan Shark":
        hunger = 30
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass",
                     "Blazing Angelfish", "Coruscating Angelfish", "Iridescent Angelfish"]

    if fish_name == "Lesser Europan Shark":
        hunger = 20
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Kants Philosofish", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Coruscating Angelfish"]

    if fish_name == "Pan Europan Shark":
        hunger = 20
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Invisible Piranha", "Ionic Piranha", "Jovian Piranha",
                     "Nano-Piranha", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass",
                     "Blazing Angelfish", "Coruscating Angelfish", "Iridescent Angelfish", "Greater Europan Shark",
                     "Lesser Europan Shark", "Pan Europan Shark"]

    if fish_name == "Faded Grouper":
        hunger = 10
        style = "smallest"
        prey_list = ["White Sprat"]

    if fish_name == "Friendly Grouper":
        hunger = 10
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Legendary Grouper":
        hunger = 20
        style = "largest"
        prey_list = ["Lesser Europan Shark", "Walking Bass", "Drummen Bass", "Double Bass"]

    if fish_name == "Rock Grouper":
        hunger = 30
        style = "largest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Super Grouper":
        hunger = 20
        style = "largest"
        prey_list = ["Lesser Europan Shark", "Greater Europan Shark", "Pan Europan Shark"]

    if fish_name == "Support Grouper":
        hunger = 10
        style = "smallest"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Kants Philosofish":
        hunger = 30
        style = "largest"
        prey_list = ["Manx Catfish", "Schrodingers Catfish", "Siamese Catfish", "Support Grouper", "Friendly Grouper",
                     "Faded Grouper", "Legendary Grouper", "Rock Grouper", "Super Grouper"]

    if fish_name == "Nietzsches Philosofish":
        hunger = 30
        style = "largest"
        prey_list = ["Kants Philosofish", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Greater Europan Shark", "Lesser Europan Shark", "Pan Europan Shark"]

    if fish_name == "Platos Philosofish":
        hunger = 10
        style = "largest"
        prey_list = ["Manx Catfish", "Schrodingers Catfish", "Siamese Catfish", "Acute Angle Fish",
                     "Bermuda Tri-Angle Fish", "Blasphemous Angle Fish", "Right Angle Fish"]

    if fish_name == "Russells Philosofish":
        hunger = 10
        style = "largest"
        prey_list = ["Manx Catfish", "Schrodingers Catfish", "Siamese Catfish", "Atomic Eel", "Parasitic Eel",
                     "Piranha-eating Eel", "Recombinant Eel", "Swarming Eel"]

    if fish_name == "Invisible Piranha":
        hunger = 80
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass", "Blazing Angelfish",
                     "Coruscating Angelfish", "Iridescent Angelfish", "Greater Europan Shark", "Lesser Europan Shark",
                     "Pan Europan Shark", "Invisible Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha"]

    if fish_name == "Ionic Piranha":
        hunger = 80
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass", "Blazing Angelfish",
                     "Coruscating Angelfish", "Iridescent Angelfish", "Greater Europan Shark", "Lesser Europan Shark",
                     "Pan Europan Shark", "Invisible Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha"]

    if fish_name == "Jovian Piranha":
        hunger = 80
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass", "Blazing Angelfish",
                     "Coruscating Angelfish", "Iridescent Angelfish", "Greater Europan Shark", "Lesser Europan Shark",
                     "Pan Europan Shark", "Invisible Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha"]

    if fish_name == "Nano-Piranha":
        hunger = 80
        style = "any"
        prey_list = ["Blue Sprat", "Green Sprat", "Grey Sprat", "Rainbow Sprat", "Red Sprat",
                     "Ultra-violet Sprat", "White Sprat", "Manx Catfish", "Schrodingers Catfish", "Siamese Catfish",
                     "Support Grouper", "Friendly Grouper", "Faded Grouper", "Legendary Grouper", "Rock Grouper",
                     "Super Grouper", "Right Angle Fish", "Acute Angle Fish", "Bermuda Tri-Angle Fish",
                     "Blasphemous Angle Fish", "Kants Philosofish", "Atomic Eel", "Parasitic Eel", "Piranha-eating Eel",
                     "Recombinant Eel", "Swarming Eel", "Nietzsches Philosofish", "Platos Philosofish",
                     "Russells Philosofish", "Heavenly Choirfish", "Wailing Choirfish", "Whistling Choirfish",
                     "Yodelling Choirfish", "Double Bass", "Drummen Bass", "Walking Bass", "Blazing Angelfish",
                     "Coruscating Angelfish", "Iridescent Angelfish", "Greater Europan Shark", "Lesser Europan Shark",
                     "Pan Europan Shark", "Invisible Piranha", "Ionic Piranha", "Jovian Piranha", "Nano-Piranha"]

    if fish_name == "Blue Sprat":
        hunger = 20
        style = "shop"
        prey_list = None

    if fish_name == "Green Sprat":
        hunger = 30
        style = "shop"
        prey_list = None

    if fish_name == "Grey Sprat":
        hunger = 10
        style = "shop"
        prey_list = None

    if fish_name == "Red Sprat":
        hunger = 10
        style = "shop"
        prey_list = None

    if fish_name == "White Sprat":
        hunger = 10
        style = "shop"
        prey_list = None

    if fish_name == "Rainbow Sprat":
        hunger = 30
        style = "smallest"
        prey_list = ["White Sprat"]

    if fish_name == "Ultra-violet Sprat":
        hunger = 30
        style = "any"
        prey_list = ["Rainbow Sprat"]

    return hunger, style, prey_list
