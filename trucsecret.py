import pygame
import random
import keyboard


# 90 case donc un jeu de 10*10
# A-J ↓↑  || 1-10 ←→
# 1 Porte-avions (5 cases) ;
# 1 Croiseur (4 cases) ;
# 2 Contre-torpilleurs (3 cases) ;
# 1 Torpilleur (2 cases).

def genere_plateau():
    global plateau_rect
    for j in range(10):
        for i in range(10):
            if plateau_rect[j][i]["rect"] == None:
                print("non")
                rect = pygame.Rect(i*77,j*77,73,73)
                plateau_rect[j][i]["rect"] = rect
                pygame.draw.rect(ecran,(255,255,255),rect)
            else :
                rect = pygame.Rect(i*77,j*77,73,73)
                plateau_rect[j][i]["rect"] = rect
                if plateau_rect[j][i]["Bateau"][0]:
                    pygame.draw.rect(ecran,(0,255,0),rect)
                else :
                    pygame.draw.rect(ecran,(255,255,255),rect)
                if plateau_rect[j][i]["Croix"] and plateau_rect[j][i]["toucher"]:
                    pygame.draw.line(ecran,(0,0,0),(case["rect"].x,case["rect"].y),(case["rect"].x + case["rect"].width,case.y + case["rect"].height),width=3)
                    pygame.draw.line(ecran,(0,0,0),(case["rect"].x,case["rect"].y + case["rect"].height),(case["rect"].x + case["rect"].width,case["rect"].y),width=3)
                elif plateau_rect[j][i]["Croix"] and not(plateau_rect[j][i]["toucher"]):
                    pygame.draw.line(ecran,(255,0,0),(case["rect"].x,case["rect"].y),(case["rect"].x + case["rect"].width,case["rect"].y + case["rect"].height),width=3)
                    pygame.draw.line(ecran,(255,0,0),(case["rect"].x,case["rect"].y + case["rect"].height),(case["rect"].x + case["rect"].width,case["rect"].y),width=3)
#766
pygame.init()
ecran = pygame.display.set_mode((1720,780))
pygame.display.set_caption("Bataille navale")
end = False
plateau_rect = [[{"Croix" : False , "rect" : None , "toucher" : False , "Bateau" : [False, ""] } for i in range(10) ] for j in range(10)]
genere_plateau()
plateau_joueur = [[0 for i in range(10)] for i in range(10)]
plateau_bot = [[0 for i in range(10)] for i in range(10)]
tour = 0
piece_placer = 0
#max 5
Porte_avions = ecran.subsurface(pygame.Rect((1607,380),(73,385)))
Porte_avions.fill((0,255,0))
#(1607,329)
Croiseur = None
Contre_torpilleurs1 = None
Contre_torpilleurs2 = None
Torpilleur = None
toucher = False
joueur_joue = False
game_play = False
peux_jouer = False
Placement_piece = False
tour_texte_fond = pygame.font.SysFont("None",100)
tour_texte = tour_texte_fond.render(f"tour numero : {str(tour)}",False,(255,255,255))
tour_rect = pygame.Rect(925,0,575,68)
tour_surf = ecran.subsurface(tour_rect)
tour_surf.blit(tour_texte,(0,0))
ecran.blit(tour_surf.copy(),tour_rect)
text_rect = pygame.Rect((plateau_rect[3][-1]["rect"].x + plateau_rect[3][-1]["rect"].width + 20,plateau_rect[3][-1]["rect"].y),(930,plateau_rect[4][-1]["rect"].y))
txt_surf = ecran.subsurface(text_rect)
texte_fond = pygame.font.SysFont("None",60)
text = texte_fond.render("Clicker sur le bouton pour commencer",False,(255,0,0))
txt_surf.blit(text,(0,0))
ecran.blit(txt_surf.copy(),text_rect)
bouton_rect = pygame.Rect((plateau_rect[7][-1]["rect"].x + plateau_rect[8][-1]["rect"].width + 100,plateau_rect[8][-1]["rect"].y),(500,100))
bouton_surf = ecran.subsurface(bouton_rect)
bouton_surf.fill((255,0,0))
bt_txt_fond = pygame.font.SysFont("None",100,bold=True)
bt_txt = bt_txt_fond.render("Jouer",False,(0,0,0))
bouton_surf.blit(bt_txt,bt_txt.get_rect(center = bouton_surf.get_rect().center))
ecran.blit(bouton_surf.copy(),bouton_rect)
ecran.blit(Porte_avions.copy(),pygame.Rect((1607,380),(73,385)))

while not(end):

    pygame.display.flip()

    if game_play:

        for collone in plateau_rect:

            for case in collone:

                if case["rect"].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

                    if toucher:

                        pygame.draw.line(ecran,(255,0,0),(case["rect"].x,case["rect"].y),(case["rect"].x + case["rect"].width,case["rect"].y + case["rect"].height),width=3)
                        pygame.draw.line(ecran,(255,0,0),(case["rect"].x,case["rect"].y + case["rect"].height),(case["rect"].x + case["rect"].width,case["rect"].y),width=3)
                    
                    else:

                        pygame.draw.line(ecran,(0,0,0),(case["rect"].x,case["rect"].y),(case["rect"].x + case["rect"].width,case["rect"].y + case["rect"].height),width=3)
                        pygame.draw.line(ecran,(0,0,0),(case["rect"].x,case["rect"].y + case["rect"].height),(case["rect"].x + case["rect"].width,case["rect"].y),width=3)
                        
                    case["croix"] = True
                    print(case)
                    tour += 1
                    tour_texte = tour_texte_fond.render(f"tour numero : {str(tour)}",False,(255,255,255))
                    tour_surf.fill((0,0,0))
                    tour_surf.blit(tour_texte,(0,0))
                    ecran.blit(tour_surf.copy(),tour_rect)
                    pygame.time.wait(250)

    if bouton_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not(Placement_piece):
        
        #Placement_piece = True
        game_play = True
        txt_surf.fill((0,0,0))
        text = texte_fond.render("Poser les piece, puis appyue sur le bouton",False,(255,0,0))
        txt_surf.blit(text,(0,0))
        bouton_surf.fill((255,0,0))
        bt_txt = bt_txt_fond.render("Validé les piece",False,(0,0,0))
        bouton_surf.blit(bt_txt,bt_txt.get_rect(center = bouton_surf.get_rect().center))
        ecran.blit(txt_surf.copy(),text_rect)
        ecran.blit(bouton_surf.copy(),bouton_rect)
    
    if pygame.mouse.get_pressed()[0]:
        #print(pygame.mouse.get_pos())
        #ecran.blit(Porte_avions.copy(),pygame.Rect((10,10),(73,385)))
        ecran.fill((0,0,0),pygame.Rect((0,0),(766,766)))
        genere_plateau()
        pygame.time.wait(1)


    if keyboard.is_pressed("Esc"):

        pygame.quit()
        quit()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            end = True

pygame.quit()
quit()