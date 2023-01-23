# Créé par Dominique, le 18/01/2017 avec EduPython
import pygame                                                    # importation complète de la librairie
from pygame.locals import *

pygame.init()

tailleH = 800
tailleV = 600
pos_x = 0
pos_y = 520
fin = False                                                       # on initialise pour la fin du jeu
fenetre = pygame.display.set_mode((tailleH,tailleV),RESIZABLE)    # on définit la fenêtre aux dimensions tailleH et tailleH
pygame.display.set_caption("Déplacement garçon")                  # on donne un titre à la fenêtre
fond = pygame.image.load("fondpygame.jpg").convert()              # ou format.png  et .convert() : conversion au bon format
fenetre.blit(fond,(0,0))                                          # on colle et on positionne aux coordonnées (x,y) avec 0,0 en haut à gauche
personnage = pygame.image.load("garcond.png").convert_alpha()     # on charge le personnage de départ de taille 60x80
fenetre.blit(personnage,(pos_x,pos_y))                            # on le positionne en bas à gauche
pygame.display.flip()                                             # on rafraichit l'écran
pygame.key.set_repeat(200, 10)                                    # déplacement si la touche reste appuyée
while not fin:
    for event in pygame.event.get():
        if event.type == KEYDOWN:                                 # on test l'appui sur une touche
            if event.key == K_UP:
                personnage = pygame.image.load("garconh.png").convert_alpha()     # on charge le personnage
                if pos_y > 0:
                    pos_y = pos_y-5
            if event.key == K_DOWN:
                personnage = pygame.image.load("garconh.png").convert_alpha()     # on charge le personnage
                if pos_y < 520:
                    pos_y = pos_y+5
            if event.key == K_LEFT:
                personnage = pygame.image.load("garcong.png").convert_alpha()     # on charge le personnage
                if pos_x > 0:
                    pos_x = pos_x-5
                fenetre.blit(fond,(0,0))
            if event.key == K_RIGHT:
                personnage = pygame.image.load("garcond.png").convert_alpha()     # on charge le personnage
                if pos_x < 740:
                    pos_x = pos_x+5
        if event.type == pygame.QUIT:                             # on appuie sur la croix pour quitter
            fin = True
    fenetre.blit(fond,(0,0))
    fenetre.blit(personnage,(pos_x,pos_y))
    pygame.display.flip()                                         # on rafraichit l'écran
pygame.quit()
quit()