from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,700),pygame.RESIZABLE)
text = TextInput(screen = screen,h = screen.get_height()/2,w = screen.get_width()/2,color=(125,120,60,5))

pygame.display.flip()

end = False
while not(end):
    pygame.display.flip()

    for event in pygame.event.get():
        text.draw(event=event)
        text.test()
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
        if event.type == pygame.WINDOWRESIZED:
            text.update_size(w = pygame.display.get_window_size()[0],h = pygame.display.get_window_size()[1])
pygame.quit()
quit()