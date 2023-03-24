from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
text = TextInput(color=(10,50,20,0))

end = False
while not(end):
    text.draw(screen=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True


pygame.quit()
quit()