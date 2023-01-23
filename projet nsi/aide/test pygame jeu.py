# Créé par Dom, le 17/06/2019 en Python 3.4
import sys,math,random,pygame
from pygame.locals import *                       # importation des constantes de Pygame en local

# Paramètres
largeur = 640
hauteur = 480
periode = 60
titre = "Essai jeu"

# INITIALISATION DU JEU
pygame.init()
fenetre = pygame.display.set_mode((largeur,hauteur))
pygame.display.set_caption(titre)
rectfenetre = fenetre.get_rect()
font = pygame.font.Font(None, 36)

               # Affichage d'un texte
texte = font.render("PERDU",1,pygame.Color("#FF0000"))
fenetre.blit (texte ,(300,450))
rectTexte = texte.get_rect()
rectTexte.center = rectfenetre.center

# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
    time = clock.tick(periode)
    print(time)

	# GESTION DES EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    fenetre.fill(pygame.Color("#0000FF"))
    fenetre.blit(texte,rectTexte)
    pygame.display.update()
