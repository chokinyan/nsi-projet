from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
text = TextInput(h = 200,w = 200,color=(125,120,60,5))

pygame.display.flip()

end = False
while not(end):
    pygame.display.flip()

    for event in pygame.event.get():
        if text.draw(screen=screen):
            print("dalut")
        if event.type == pygame.QUIT:
            end = True

pygame.quit()
quit()