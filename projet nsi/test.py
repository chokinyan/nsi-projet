#import pygame #pygame classique
#import pygame.locals #pour tous ce qui est touche et tout

"""pygame.init()

test_img = pygame.image.load("image/image sans droit et utilisable/plateau/téléchargé.png")
test_img = pygame.transform.scale(test_img,(600,600))
pygame.display.init()

test = pygame.SCALED

test.blit(test_img,(0,0))

pygame.display.flip()

end = False

while not(end):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

pygame.quit()"""


t ={}
for i in range(4):
    t[i+1] = ("",0,i+1)

print(len(t))

"""for i in t:
    print(type(t.get(i)[1]))"""

