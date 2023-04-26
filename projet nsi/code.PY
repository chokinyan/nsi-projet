import random

# Classe de joueur pour garder une trace de la position du joueur et des jets de dés
classe Joueur :
    def __init__(self, name) :
        self.name = name
        self.position = 0
        self.skip_turns = 0

    def lancer_dée(self) :
        return random.randint(1, 6)


# Définir le plateau avec 10 cases
board = ['Case1', 'Case2', 'Case3', 'Case4', 'Case5',
         'Case6', 'Case7', 'Case8', 'Case9', 'Case10']

# Définir les joueurs
joueur1 = Joueur('Joueur1')
joueur2 = Joueur('Joueur2')

# Définitions des cases personnalisées
# Case où les joueurs ne peuvent jouer qu'un seul dé pendant X tours
carré_jouer_un_meurt = ['Case3', 'Case8']
x_tours_jouer_un_meurt = 3 # Changez cette valeur pour spécifier le nombre de tours

# Carré où les joueurs reculent au tour suivant
square_move_backward = ['Square4', 'Square7']

# Place où les joueurs peuvent s'arrêter pour le prochain tour
square_stop = ['Case6', 'Case9'] # Case où les joueurs peuvent s'arrêter pour le tour suivant

# Case où deux joueurs s'affrontent et où le perdant recule
square_face_off = ['Case2', 'Case5']
face_off_losing_moves_back = True # Change cette valeur en False si le perdant ne recule pas


# Boucle de jeu
while True :
    # Tour du joueur 1
    print(f "Tour de {joueur1.nom}")
    si player1.skip_turns > 0 :
        print(f"{joueur1.nom} ne peut pas lancer les dés ce tour-ci")
        player1.skip_turns -= 1
    else :
        Dée1 = player1.roll_dice()
        dée2 = player1.roll_dice()
        print(f"{joueur1.nom} a lancé les dés : {dice1}, {dice2}")
        if board[player1.position] in square_play_one_die :
            print(f"{joueur1.nom} ne peut jouer qu'un seul dé pour les prochains {x_tours_jouer_un_die} tours")
            player1.skip_turns = x_turns_play_one_die - 1
        if board[player1.position] in square_move_backward :
            print(f"{joueur1.nom} reculera au prochain tour.")
            player1.skip_turns = 1
        if board[player1.position] in square_stop :
            print(f"{joueur1.nom} passera le prochain tour.")
            player1.skip_turns = 1

        player1.position += dice1 + dice2
        si player1.position >= len(board) :
            print(f"{joueur1.nom} gagne !")
            break

    # Tour du joueur 2
    print(f "Tour de {joueur2.nom}")
    si player2.skip_turns > 0 :
        print(f"{joueur2.nom} ne peut pas lancer les dés ce tour-ci")
        player2.skip_turns -= 1
    else :
        dée1 = player2.roll_dice()
        dée2 = player2.roll_dice()
        print(f"{joueur2.nom} a lancé les dés : {dée1}, {dée2}")
        if board[player2.position] in Case_joueur_un_meurt :
            print(f"{joueur2.nom} ne peut jouer qu'un seul dé pour les prochains {x_ Case_joueur_un_meurt} tours")
            player2.skip_turns = x_tours_joueur_un_meurt - 1
        if board[player2.position] in square_move_backward :
            print(f"{joueur2.nom} reculera au prochain tour.")
            player2.skip_turns = 1
        if board[player2.position] in square_stop :
            print