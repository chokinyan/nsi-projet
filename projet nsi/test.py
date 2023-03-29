from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
text = TextInput(h = 100,w = 100,color=(125,120,60,5),bg=(255,255,255))

pygame.display.flip()

end = False
while not(end):
    pygame.display.flip()

    for event in pygame.event.get():
        text.draw(screen=screen)
        if event.type == pygame.QUIT:
            end = True

pygame.quit()
quit()