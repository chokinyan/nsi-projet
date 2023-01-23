# Créé par Dominique, le 18/01/2016 avec EduPython
# on génère les sons en appuyant sur les touches de s à l attention clavier qwerty
from lycee import *
import  pygame   # importation complète
from pygame.locals import *
pygame.init()
pygame.mixer.init()

tailleH = 800
tailleV = 600

# On charge le fichier de la note

do=pygame.mixer.Sound("Son\Do.wav")
re=pygame.mixer.Sound("Son\Re.wav")
mi=pygame.mixer.Sound("Son\Mi.wav")
fa=pygame.mixer.Sound("Son\Fa.wav")
sol=pygame.mixer.Sound("Son\Sol.wav")
la=pygame.mixer.Sound("Son\La.wav")
si=pygame.mixer.Sound("Son\Si.wav")
do2=pygame.mixer.Sound("Son\Do2.wav")


fin = False                                                       # on initialise pour la fin du jeu
fenetre = pygame.display.set_mode((tailleH,tailleV),RESIZABLE)    # on défini la fenêtre aux dimensions tailleH et tailleH
pygame.display.set_caption("Test notes touches.jpg")
fond = pygame.image.load("fond notes.jpg").convert()              # ou format.png  et .convert() : conversion au bon format
fenetre.blit(fond,(0,0))                                          # on colle et on positionne aux coordonnées (x,y) avec 0,0 en haut à gauche
pygame.display.flip()                                             # on rafraichit l'écran
while not fin:
    for event in pygame.event.get():
        if event.type == KEYDOWN:                                 # on test l'appui sur une touche
            if event.key == K_s:
                do.play()                                         # on joue la note
            if event.key == K_d:
                re.play()
            if event.key == K_f:
                mi.play()
            if event.key == K_g:
                fa.play()
            if event.key == K_h:
                sol.play()
            if event.key == K_j:
                la.play()
            if event.key == K_k:
                si.play()
            if event.key == K_l:
                do2.play()
        if event.type == pygame.QUIT:                             # on appuie sur la croix pour quitter
            fin = True
pygame.quit()
quit()

