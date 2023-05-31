import pygame
import random


def main():
    pygame.init()
    ecran = pygame.display.set_mode((1920,1080))
    end = False
    while not(end):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()