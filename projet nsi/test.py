from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000),pygame.RESIZABLE)
text = TextInput(h = 500,w = 500,color=(125,120,60,50))

pygame.display.flip()

end = False
while not(end):

    if text.draw(screen=screen):
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True


pygame.quit()
quit()