# Créé par Dominique, le 18/01/2017 avec EduPython
from lycee import *
import  pygame   # importation complète
from pygame.locals import *

pygame.init()

tailleH = 1600
tailleV = 1400
pos_x = tailleH/2
pos_y = tailleV/2
fin = False                                                       # on initialise pour la fin du jeu
fenetre = pygame.display.set_mode((tailleH,tailleV),RESIZABLE)    # on défini la fenêtre aux dimensions tailleH et tailleH
pygame.display.set_caption("Test Fonctions Pygame")               # on donne un titre à la fenêtre
fond = pygame.image.load("fondpygame.jpg").convert()              # ou format.png  et .convert() : conversion au bon format
fenetre.blit(fond,(0,0))                                          # on colle et on positionne aux coordonnées (x,y) avec 0,0 en haut à gauche
personnage = pygame.image.load("garcond.png").convert_alpha()     # on affiche la personnage de taille 60x80
fenetre.blit(personnage,(pos_x,pos_y))                            # on le positionne en bas à gauche
pygame.display.flip()                                             # on rafraichit l'écran
while not fin:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:                             # on teste le mouvement de la souris
            if pos_x>0 or pos_y>0 or pos_x<740 or pos_y<520 :
                pos_x = event.pos[0]
                pos_y = event.pos[1]
        if event.type == pygame.QUIT:                             # on appuie sur la croix pour quitter
            fin = True
    fenetre.blit(fond,(0,0))
    fenetre.blit(personnage,(pos_x,pos_y))
    pygame.display.flip()                                         # on rafraichit l'écran
pygame.quit()
quit()