import pygame,sys
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768))

#Chargement et collage du fond
fond = pygame.image.load("newyork2.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("spiderman.gif").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():	#Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:	#Si clic gauche
				#On change les coordonnées du perso
                if event.pos[0]>0 and event.pos[0]<960:
                    perso_x = event.pos[0]
                if event.pos[1]>0 and event.pos[1]<596:
                    perso_y = event.pos[1]


    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (perso_x, perso_y))
    #Rafraichissement
    pygame.display.flip()