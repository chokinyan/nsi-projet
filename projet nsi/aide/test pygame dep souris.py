# Créé par dmack1, le 18/02/2021 en Python 3.4
import pygame
pygame.init()

largeur = 400
hauteur = 400
vitesse = [10, 8]
color = 255, 255, 255
screen = pygame.display.set_mode((largeur,hauteur), pygame.RESIZABLE)

balle = pygame.image.load("ballon.png")
ballerect = balle.get_rect()
perdu = False

while not perdu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdu = True
        ballerect = ballerect.move(vitesse)
        if ballerect.left < 0 or ballerect.right > largeur:
            vitesse[0] = -vitesse[0]
        if ballerect.top < 0 or ballerect.bottom > hauteur:
            vitesse[1] = -vitesse[1]

        screen.fill(color)
        screen.blit(balle, ballerect)
        pygame.display.flip()

pygame.quit()
quit()
