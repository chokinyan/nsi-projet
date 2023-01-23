# Créé par Dominique, le 18/01/2016 avec EduPython
from lycee import *
import  pygame   # importation complète
from pygame.locals import *
pygame.init()
pygame.mixer.init()

tailleH = 800
tailleV = 600
fin = False                                                       # on initialise pour la fin du jeu
fenetre = pygame.display.set_mode((tailleH,tailleV),RESIZABLE)    # on défini la fenêtre aux dimensions tailleH et tailleH
pygame.display.set_caption("Test Son Pygame")                     # on donne un titre à la fenêtre
fond = pygame.image.load("fondpygame.jpg").convert()              # ou format.png  et .convert() : conversion au bon format
fenetre.blit(fond,(0,0))                                          # on colle et on positionne aux coordonnées (x,y) avec 0,0 en haut à gauche
pygame.display.flip()                                             # on rafraichit l'écran
musique=pygame.mixer.Sound('Son\Ballade.wav')                     # on charge le fichier de musique
while not fin:
    for event in pygame.event.get():
        if event.type == KEYDOWN:                                 # on test l'appui sur une touche
            if event.key == K_UP:
                musique.play()                                    # on joue le morceau
            if event.key == K_DOWN:
                musique.stop()                                    # on arrête le morceau
            if event.key == K_LEFT:
                pygame.mixer.pause()                              # on met en pause le morceau
            if event.key == K_RIGHT:
                pygame.mixer.unpause()                            # on met en continue le morceau
        if event.type == pygame.QUIT:                             # on appuie sur la croix pour quitter
            fin = True
pygame.quit()
quit()

