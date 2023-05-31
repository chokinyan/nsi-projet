import pygame
import random
import keyboard


# 90 case donc un jeu de 10*10
# A-J ↓↑  || 1-10 ←→
# 1 Porte-avions (5 cases) ;
# 1 Croiseur (4 cases) ;
# 2 Contre-torpilleurs (3 cases) ;
# 1 Torpilleur (2 cases).

def main():
    pygame.init()
    ecran = pygame.display.set_mode((1720,780))
    pygame.display.set_caption("Bataille navale")
    end = False
    plateau_joueur = [[0 for i in range(10)] for i in range(10)]
    plateau_bot = [[0 for i in range(10)] for i in range(10)]
    plateau_rect = [[] for i in range(10)]
    for j in range(10):
        for i in range(10):
            rect = pygame.Rect(i*ecran.get_width()/10+1,j*ecran.get_height()/10+1,ecran.get_width()/10-5,ecran.get_height()/10-5)
            plateau_rect[j].append(rect)
            pygame.draw.rect(ecran,(255,255,255),rect)
    pygame.display.flip()
    while not(end):
        for collone in plateau_rect:
            for case in collone:
                if case.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    print("ok")
        if keyboard.is_pressed("Esc"):
            pygame.quit()
            quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()