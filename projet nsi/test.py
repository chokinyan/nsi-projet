from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
text = TextInput(screen = screen,h = screen.get_height(),w = screen.get_width(),color=(125,120,60,5))

pygame.display.flip()

end = False
while not(end):
    pygame.display.flip()

    for event in pygame.event.get():
        text.draw(event=event)
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
        if event.type == pygame.WINDOWRESIZED:
            text.update_size(h = screen.get_height(),w = screen.get_width())
pygame.quit()
quit()