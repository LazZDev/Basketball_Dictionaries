# Defined the list of player dictionaries
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Forward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

# Defined the Player class


class Player:
    # Constructor that took a player dictionary as input
    def __init__(self, player_info):
        # Set the name, age, position, and team attributes using the dictionary
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]


# Created a Player object using the first player dictionary in the players list
player1 = Player(players[0])
# Printed the name of the created Player object
print(player1.name)

# Defined the player dictionaries for Kevin Durant, Jason Tatum, and Kyrie Irving
kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Defined the Player class


class Player:
    # Constructor that took a player dictionary as input
    def __init__(self, player_info):
        # Set the name, age, position, and team attributes using the dictionary
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]


# Created Player instances for Kevin Durant, Jason Tatum, and Kyrie Irving
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Defined the list of player dictionaries
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
]

# Defined the Player class


class Player:
    # Constructor that takes a player dictionary as input
    def __init__(self, player_info):
        # Set the name, age, position, and team attributes using the dictionary
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]


# Initialized an empty list to store the Player instances
new_team = []

# Iterated through the list of player dictionaries
for player_dict in players:
    # Created a new Player instance for each dictionary
    new_player = Player(player_dict)
    # Add the new Player instance to the new_team list
    new_team.append(new_player)

# Printed the names of the players in the new_team list
for player in new_team:
    print(player.name)
