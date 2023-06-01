import pygame
import random
import keyboard


# 90 case donc un jeu de 10*10
# A-J ↓↑  || 1-10 ←→
# 1 Porte-avions (5 cases) ;
# 1 Croiseur (4 cases) ;
# 2 Contre-torpilleurs (3 cases) ;
# 1 Torpilleur (2 cases).

def phase_jeu():
    if phase == 1:
        plateau_rect = [[] for i in range(10)]
        for j in range(10):
            for i in range(10):
                rect = pygame.Rect(i*80,j*80,75,75)
                plateau_rect[j].append(rect)
                pygame.draw.rect(ecran,(255,255,255),rect)
        return plateau_rect
    elif phase == 2:
        pass

pygame.init()
ecran = pygame.display.set_mode((1720,780))
pygame.display.set_caption("Bataille navale")
end = False
plateau_rect = [[] for i in range(10)]
for j in range(10):
    for i in range(10):
        rect = pygame.Rect(i*77,j*77,73,73)
        plateau_rect[j].append(rect)
        pygame.draw.rect(ecran,(255,255,255),rect)
plateau_joueur = [[0 for i in range(10)] for i in range(10)]
plateau_bot = [[0 for i in range(10)] for i in range(10)]
tour = 0
piece_placer = 0
#max 5
Porte_avions = None
Croiseur = None
Contre_torpilleurs1 = None
Contre_torpilleurs2 = None
Torpilleur = None
toucher = False
joueur_joue = False
game_play = False
tour_texte_fond = pygame.font.SysFont("None",100)
tour_texte = tour_texte_fond.render(f"tour numero : {str(tour)}",False,(255,255,255))
tour_rect = pygame.rect.Rect(925,0,575,68)
tour_surf = ecran.subsurface(tour_rect)
tour_surf.blit(tour_texte,(0,0))
ecran.blit(tour_surf.copy(),tour_rect)
#75*75 les case
text_rect = pygame.rect.Rect((plateau_rect[3][-1].x + plateau_rect[3][-1].width + 20,plateau_rect[3][-1].y),(930,plateau_rect[4][-1].y))
txt_surf = ecran.subsurface(text_rect)
texte_fond = pygame.font.SysFont("None",60)
text = texte_fond.render("Clicker sur le bouton pour commencer",False,(255,0,0))
txt_surf.blit(text,(0,0))
ecran.blit(txt_surf.copy(),text_rect)
bouton_rect = pygame.rect.Rect((plateau_rect[7][-1].x + plateau_rect[8][-1].width + 100,plateau_rect[8][-1].y),(500,100))
bouton_surf = ecran.subsurface(bouton_rect)
bouton_surf.fill((255,0,0))
bt_txt_fond = pygame.font.SysFont("None",100,bold=True)
bt_txt = bt_txt_fond.render("Jouer",False,(0,0,0))
bouton_surf.blit(bt_txt,bt_txt.get_rect(center = bouton_surf.get_rect().center))
ecran.blit(bouton_surf.copy(),bouton_rect)

while not(end):

    pygame.display.flip()

    if game_play:

        for collone in plateau_rect:

            for case in collone:

                if case.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

                    if toucher:

                        pygame.draw.line(ecran,(255,0,0),(case.x,case.y),(case.x + case.width,case.y + case.height),width=3)
                        pygame.draw.line(ecran,(255,0,0),(case.x,case.y + case.height),(case.x + case.width,case.y),width=3)
                    else:

                        pygame.draw.line(ecran,(0,0,0),(case.x,case.y),(case.x + case.width,case.y + case.height),width=3)
                        pygame.draw.line(ecran,(0,0,0),(case.x,case.y + case.height),(case.x + case.width,case.y),width=3)
                    tour += 1
                    tour_texte = tour_texte_fond.render(f"tour numero : {str(tour)}",False,(255,255,255))
                    tour_surf.fill((0,0,0))
                    tour_surf.blit(tour_texte,(0,0))
                    ecran.blit(tour_surf.copy(),tour_rect)
                    pygame.display.flip()
                    pygame.time.wait(250)

    if bouton_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not(game_play):
        
        game_play = True
        txt_surf.fill((0,0,0))
        text = texte_fond.render("Poser les piece, quand cela est fait appyue sur le bouton",False,(255,0,0))
        txt_surf.blit(text,(0,0))
        bouton_surf.fill((255,0,0))
        bt_txt = bt_txt_fond.render("Validé les piece",False,(0,0,0))
        bouton_surf.blit(bt_txt,bt_txt.get_rect(center = bouton_surf.get_rect().center))
        ecran.blit(txt_surf.copy(),text_rect)
        ecran.blit(bouton_surf.copy(),bouton_rect)

    if keyboard.is_pressed("Esc"):

        pygame.quit()
        quit()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            end = True

pygame.quit()
quit()