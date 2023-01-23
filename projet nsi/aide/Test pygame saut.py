# Créé par Dominique, le 26/02/2020 avec EduPython
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Saut')

gris = (220,220,220)
bleu = (49,140,200)
x=0
dx=1
y=590
y_saut=10
accel=9.81
vitesse=120
fenetre.fill(gris)
pygame.draw.circle(fenetre, bleu, (x+10, y+10), 10, 0) # surface, couleur, coordonnées du centre, rayon et épaisseur
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type== KEYDOWN:                    # Si la touche est appuyée
            if event.key==K_UP:
                y_saut=-0.5*accel*x**2+vitesse*x    # Equation du MTRUV : x = 0.5at^2+v.t + x0
                if x<790 and y_saut<590:
                    y_saut=round(y_saut)
                    print("x=",x,"y_saut=",y_saut)
                    x=x+dx
                    fenetre.fill(gris)
                    pygame.draw.circle(fenetre, bleu, (x, y_saut), 10, 0)
                    pygame.display.flip()
                else :
                    pygame.quit()
                    quit()
    pygame.display.update()