import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.skip_turns = 0

    def roll_dice(self):
        return random.randint(1, 6)

board_size = 10

special_squares = {
    2: {'name': 'Face off', 'lose_turn': False, 'move_backward': True},
    3: {'name': 'Play one die', 'num_turns': 3},
    4: {'name': 'Move backward', 'num_turns': 1, 'move_backward': True},
    6: {'name': 'Stop', 'num_turns': 1},
    7: {'name': 'Move backward', 'num_turns': 1, 'move_backward': True},
    9: {'name': 'Stop', 'num_turns': 1},
}

players = [Player('Player 1'), Player('Player 2')]

def play_turn(player):
    print(f"Turn of {player.name}")
    if player.skip_turns > 0:
        print(f"{player.name} cannot roll the dice this turn")
        player.skip_turns -= 1
    else:
        dice1 = player.roll_dice()
        dice2 = player.roll_dice()
        print(f"{player.name} rolled the dice: {dice1}, {dice2}")
        if player.position + dice1 + dice2 in special_squares:
            special_square = special_squares[player.position + dice1 + dice2]
            print(f"{player.name} landed on {special_square['name']}")
            player.skip_turns = special_square.get('num_turns', 0) - 1
            if special_square.get('move_backward', False):
                player.position -= 1
            if special_square.get('lose_turn', False):
                players[(players.index(player) + 1) % 2].skip_turns += 1
        else:
            player.position += dice1 + dice2
        if player.position >= board_size:
            print(f"{player.name} wins!")

while True:
    play_turn(players[0])
    if players[0].position >= board_size:
        break
    play_turn(players[1])
    if players[1].position >= board_size:
        break