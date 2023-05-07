import random

# Player class to keep track of player position and dice rolls
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.skip_turns = 0

    def roll_dice(self):
        return random.randint(1, 6)

# Define the board with 10 squares
board = ['Square1', 'Square2', 'Square3', 'Square4', 'Square5',
         'Square6', 'Square7', 'Square8', 'Square9', 'Square10']

# Define the players
player1 = Player('Player1')
player2 = Player('Player2')

# Define custom squares
# Square where players can only roll one die for X turns
square_play_one_die = ['Square3', 'Square8']
x_turns_play_one_die = 3

# Square where players move backward on the next turn
square_move_backward = ['Square4', 'Square7']

# Square where players can stop for the next turn
square_stop = ['Square6', 'Square9']

# Square where two players face off and the loser moves back
square_face_off = ['Square2', 'Square5']
face_off_losing_moves_back = True

# Function for a player's turn
def play_turn(player):
    print(f"{player.name}'s turn")
    if player.skip_turns > 0:
        print(f"{player.name} cannot roll the dice this turn")
        player.skip_turns -= 1
    else:
        dice1 = player.roll_dice()
        dice2 = player.roll_dice()
        print(f"{player.name} rolled the dice: {dice1}, {dice2}")
        if board[player.position] in square_play_one_die:
            print(f"{player.name} can only roll one die for the next {x_turns_play_one_die} turns")
            player.skip_turns = x_turns_play_one_die - 1
        if board[player.position] in square_move_backward:
            print(f"{player.name} will move backward on the next turn")
            player.skip_turns = 1
        if board[player.position] in square_stop:
            print(f"{player.name} will skip the next turn")
            player.skip_turns = 1
        player.position += dice1 + dice2
        if player.position >= len(board):
            print(f"{player.name} wins!")
            return True
    return False

# Game loop
while True:
    if play_turn(player1):
        break
    if play_turn(player2):
        break
