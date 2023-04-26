from add_pygame import TextInput
import pygame

pygame.init()
screen = pygame.display.set_mode((500,600),pygame.RESIZABLE)
text = TextInput(screen = screen,h = screen.get_height()/2,w = screen.get_width()/2,color=(125,120,60,5),bg = (255,255,255),x = 40,y = 50)

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
            #text.update_size()
            print('ok')
        if event.type == pygame.MOUSEBUTTONUP:
            print(text.taille)
            print(pygame.mouse.get_pos())


pygame.quit() 
quit()