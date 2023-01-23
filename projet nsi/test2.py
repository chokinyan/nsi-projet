"""import pygame

pygame.init()
flags = pygame.FULLSCREEN
window_surface = pygame.display.set_mode((200,200), flags)
end = False

while not(end):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

pygame.quit()"""
"""from PIL import Image

img = Image.open("Pauline_on_a_un_probleme.jpg")
new_img = img.resize((1920,1080))
new_img.save("Pauline_on_a_un_probleme2.jpg")"""
import pygame
from bouton_pygame import Button

pygame.init()

screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)


image = pygame.image.load("Pauline_on_a_un_probleme.jpg")
#rect = image.get_rect()

#test = image.get_rect(center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2))
center = screen.get_rect().center

#test_fond = pygame.image.load(r"image\bouton\jouer.png")
#image_size = (pygame.display.get_window_size()[0],pygame.display.get_window_size()[1])
#test_fond = pygame.transform.scale(test_fond,image_size)

#bouton = Button(0,0,test_fond)

#print(screen.blit(image,image.get_rect(center = center)))

pygame.display.flip()


fin = False

while not(fin):

    #screen.fill((202,202,202))
    #if bouton.draw(screen) == True:
    #    print("ok")
    pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        elif event.type == pygame.WINDOWRESIZED:
            print("test")
            #rect = image.get_rect()
            #rect.center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2)
            center = screen.get_rect().center
            screen.blit(image,image.get_rect(center = center))
            #image_size = (pygame.display.get_window_size()[0]*(2.5/4),pygame.display.get_window_size()[1])
            #test_fond = pygame.transform.scale(test_fond,image_size)
            #bouton = Button(0,0,test_fond)




pygame.quit()
quit()