from lycee import *
import  pygame                # importation complète
from pygame.locals import *

pygame.init()

"""trame = 25                      # nombre de trames/secondes
tps = pygame.time.Clock()"""

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Animation')

#on définit les couleurs
blanc = (255,255,255)
gris = (220,220,220)
noir = (0,0,0)
vert = (50,255,50)
bleu = (49,140,200)
rouge = (255,50,50)
jaune = (255,228,54)

font_txt = pygame.font.SysFont('arial',50)                   # Arial est une police du système
text = font_txt.render('Salut la compagnie',1,blanc,bleu) # couleur de la police et couleur du fond
text_pos = text.get_rect()
text_pos.center = (400, 32)

while True:
    fenetre.fill(gris)
# on donne la surface, la couleur et les positions des coins
    pygame.draw.polygon(fenetre, vert, ((0, 0), (200, 200), (0, 200)))
# on donne la surface, la couleur, coordonnées premier point, dernier point et l'épaisseur
    pygame.draw.line(fenetre, noir, (0, 300), (400, 300),5)
# on donne la surface, la couleur, les coordonnées du centre, le rayon et l'épaisseur
    pygame.draw.circle(fenetre, bleu, (100, 300), 50, 0)
# on donne la surface, la couleur, les coordonnées du premier point du rectangle, la taille horizontale, la taille verticale et l'épaisseur
    pygame.draw.ellipse(fenetre,jaune, (0,500,80,50),2)
# on donne la surface, la couleur, les coordonnées du premier point du rectangle, la taille horizontale, la taille verticale et l'épaisseur
    pygame.draw.rect(fenetre,rouge, (0, 250, 100, 50),5)
# on donne la surface, la couleur, coordonnées premier point, dernier point et l'épaisseur
    pygame.draw.arc(fenetre,noir,(0,350,800,450),0,1.27,3)
    fenetre.blit(text, text_pos)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    # tps.tick(trame)