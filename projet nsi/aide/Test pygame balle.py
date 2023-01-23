import pygame
from time import *
from pygame.locals import *

pygame.init()
tailleH = 800
tailleV = 600
H = 10
V = 10
vitesse=0.01
bleu = 50, 50, 255

fenetre = pygame.display.set_mode((tailleH,tailleV))
pygame.display.set_caption("Test déplacement Pygame")              # on donne un titre à la fenêtre
balle = pygame.image.load("ballon.png")
balle_pos = balle.get_rect()
fenetre.fill(bleu)
fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                              # on appuie sur la croix pour quitter
            fin = True

    balle_pos = balle_pos.move(H,V)
    if balle_pos.left < 0 or balle_pos.right > tailleH:            # on touche le bord gauche ou droit
        H = -H
    if balle_pos.top < 0 or balle_pos.bottom > tailleV:            # on touche le bord haut ou bas
        V = -V
    print(vitesse)
    fenetre.fill(bleu)
    fenetre.blit(balle, balle_pos)
    sleep(vitesse)                                                 # on ralenti la vitesse
    pygame.display.flip()
pygame.quit()
quit()