import random

# snakes and ladders type of game, but "tower"
# maximum of len(pokemon_pieces) players
# gameplay
  # play against comuputer (pick)
  # 3 player max

pokemon_pieces = [
  "alolan ninetales",
  "ciderace",
  "magearna",
  "tsareena",
  "umbreon",
  ]
chosen_pokemon_pieces = []

list_of_players = []

class Player:
  def __init__(self, name):
    self.name = name
    self.piece = None
    self.place = 0
    self.order = None
  
  def move_forward(self, amount):
    total_move = self.place + amount
    setattr(self, "place", total_move)
    print(f"{self.piece} has moved up {amount} spaces. {self.piece} is now at space {total_move}")

  def move_down(self, amount):
    back_to = self.place - amount
    setattr(self, "place", back_to)
    print(f"{self.piece} has moved down {amount} spaces. {self.piece} is now at space {back_to}")

  def pick_pokemon_piece(self, pokemon_list):
    display_pokemon_pieces(pokemon_list)
    pick_pokemon = ask(f"Which pokemon do you choose to represent you?").lower()
    if pick_pokemon in pokemon_list:
      chosen_pokemon = pokemon_list.pop(pokemon_list.index(pick_pokemon))
      setattr(self, "piece", chosen_pokemon)
    else:
      improper_input("ERROR", "Please input available pokemon from list", pick_pokemon)

  def get_piece(self):
    return self.piece

  # organizes players based on position, distance from finish line
  # assume opponent is a list
  # updates self.__order
  def position(self, finish_line, opponents):
    order = []
    player_position = finish_line - self.place
    order.append(player_position)
    
    for opponent in opponents:
      opponent_position = finish_line - opponent.place
      order.append(opponent_position)

    player_order = sorted(order).index(player_position) + 1

    setattr(self, "order", player_order)
  
  def give_ordinal(self, order):
    ordinals = {1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th"}
    return ordinals[order]
  
  def get_order(self, finish_line, opponents):
    self.position(finish_line, opponents)
    ordinal = self.give_ordinal(self.order)
    return f"==> {self.piece} is currently in {self.order}{ordinal} place"

def display_pokemon_pieces(pokemon_list):
  for pokemon in pokemon_list:
    print(pokemon)

def roll_dice():
  return random.randint(1, 6)

def ketchup_says(type, statement):
  print(f"===>{type}: {statement}")

def ask(question):
  return input(f"==>{question}")

def recursive_fn(fn_name):
  return fn_name()

def improper_input(error, message, fn):
  ketchup_says(error, message)
  return recursive_fn(fn)

def check_if_input_digit(user_input, error, message, fn):
  if user_input.isdigit():
    return int(user_input)
  else:
    return improper_input(error, message, fn)

def ask_player_numbers():
  number_of_players = ask("How many players are playing? 1 - 3\n")
  players = check_if_input_digit(number_of_players, "INVALID NUMBER", "Please input correct number of players: 1 - 3", ask_player_numbers)
  if players < 1 or players > 3:
    improper_input("OUT OF RANGE", "Please input between 1 - 3", ask_player_numbers)
  else:
    return players

#constructs instance of class Player and returns instance
def create_new_player(player_num):
  player_name = ask(f"What is player {player_num}'s name?")
  if len(player_name) > 1: 
    player_name = Player(player_name)
    print(f"Welcome, {player_name.name}")
    print(f"Pick your pokemon:")
    player_name.pick_pokemon_piece(pokemon_pieces)
    return player_name
  else:
    improper_input("INVALID NAME", "Please input at least one character for name", create_new_player)

def create_each_player(number_of_players):
  for each_player in range(1, number_of_players + 1):
    create_new_player()
    print(each_player)


create_each_player(3)


