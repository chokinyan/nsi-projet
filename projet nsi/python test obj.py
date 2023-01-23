import os as os
import random as rng
import pygame as pyg
import pygame.locals as pygl
from PIL import Image
import keyboard
from bouton_pygame import Button
import random as rng
import math
test = "le test a été effectuer"
#-------------------------------------------------------------
pyg.init()
last_screen = 0
icone = pyg.image.load("image\icone\images.png")
screen = pyg.display.set_mode((500,500),pyg.RESIZABLE)
B_jouer = B_nbjoueur = B_nbot = B_botO = B_botN = None
end = False
affichage_etape = 0
comment = "debut"
pyg.mouse.set_cursor(*pyg.cursors.arrow)
pyg.display.set_icon(icone)
#--------------------------------------------------------------
def ecran(comment = "debut") -> None:
    global B_jouer,B_nbjoueur,B_nbot,B_botO,B_botN
    taille_screen = pyg.display.get_window_size()
    if comment == "debut":
        test_gif = pyg.image.load("majo-no-tabitabi-the-journey-of-elaina.gif")
        print(pyg.image.get_extended())
        test_fond = pyg.image.load("mare_naturelle.jpg")
        image_size_fond = (taille_screen[0],taille_screen[1])
        test_fond = pyg.transform.scale(test_fond,image_size_fond)
        test_debut = pyg.image.load(r"image\bouton\jouer.png")
        image_size_debut = (taille_screen[0]*(1/2),taille_screen[1]*(1/2))
        test_debut = pyg.transform.scale(test_debut,image_size_debut)
        B_jouer = Button(fild = test_debut)
        screen.blit(test_fond,(0,0))

    elif comment == "choix_bot/J":
        center = screen.get_rect().center
        image_O = pyg.image.load(r"image\pas d_ami.png")
        image_N = pyg.image.load(r"image\g_amis.png")
        image_N = pyg.transform.scale(image_N,(taille_screen[0]/2,taille_screen[1]*0.80))
        image_O = pyg.transform.scale(image_O,(taille_screen[0]/2,taille_screen[1]*0.80))
        B_botO = Button(fild=image_O,x=center[0]-4)
        B_botN = Button(fild=image_N,x=4)
        screen.fill((150,210,255,0))



    elif comment == "partie":
        screen.fill((150,210,255,0))
        plateaux = pyg.image.load(r"image\image sans droit et utilisable\plateau\plateau.png")
        plateaux = pyg.transform.scale(plateaux,(taille_screen[0]*0.5,taille_screen[1]))
        bottomright = screen.get_rect().bottomright
        bottom = screen.get_rect().bottom
        for i in range(10):
            dée_1_img = pyg.image.load(f"image\dée\{rng.randint(1,6)}.png")
            screen.blit(dée_1_img,dée_1_img.get_rect(bottomright = bottomright))
            screen.blit(plateaux,plateaux.get_rect(bottom = bottom))
            #dée_size = (pyg.display.get_window_size()[0]/2,pyg.display.get_window_size()[1]/2)
            #dée_1_img = pyg.transform.scale(dée_1_img,dée_size)
            pyg.display.flip()
            dée_sound = pyg.mixer.Sound(r"Son\dée\test.mp3")
            #dée_sound.play()
            pyg.time.wait(1)
            #Son\dée\test.mp3



class joueur_info:
    def __init__(self,numero,bot) -> None:
        self.numero = numero
        self.position = 0
        self.effet = ""
        self.joue = True
        self.bot = bot

    def new_position(self,total) -> None:
        global tour
        if tour < len(joueur):
            if (déP == 6 and déD == 3) or (déP == 6 and déD == 3):
                self.id_case(26)
                self.position = 26
                tour += 1

            elif (déP == 5 and déD == 4) or (déD == 4 and déP == 5):
                self.id_case(53)
                self.position = 53
                tour +=1

            else:
                tour += 1
                self.id_case(self.position+total)
                self.position += total
                self.effet = plateau.joueur_effet(self.position)
                self.effect()

        else:

            if (self.position+total) < 63:
                tour += 1
                self.id_case(self.position+total)
                self.position += total
                self.effet = plateau.joueur_effet(self.position)
                self.effect()
            
            elif (self.position+total) > 63:
                tour += 1
                self.id_case(63 - (self.position - (63 - total)))
                self.position = 63 - (self.position - (63 - total))
                self.effet = plateau.joueur_effet(self.position)
                self.effect()
            
            elif (self.position+total) == 63:
                tour += 1
                self.joue = False
                self.effet = "Fini"
                quit()

    def id_case(self,new_pos) -> None:
        for i in joueur:
            if i.numero != self.numero:
                if i.position == new_pos:
                    i.position == self.position

    def effect(self) -> None:
        if self.effet in stuck:
            self.joue = False
            if self.effet == "prison":
                for test in joueur:
                    if test.numero == self.numero:
                        continue
                    else:
                        if test.effet == "prison":
                            test.effet,self.effet = "",""
                            test.joue,self.joue = True,True
            elif self.effet == "puits":
                for test in joueur:
                    if test.numero == self.numero:
                        continue
                    else:
                        if test.effet == "puits":
                            test.effet = ""
                            test.joue = True
        elif self.effet == "mort":
            self.position = 0
            self.effet = ""

class plateau:
    def __init__(self,numero_case) -> None:
        if numero_case == 19:
            self.effect = "hotel_2"

        elif numero_case == 31:
            self.effect = "puits"
        
        elif numero_case == 42:
            self.effect = "labyrinthe"
        
        elif numero_case == 52:
            self.effect = "prison"
        
        elif numero_case == 58:
            self.effect = "mort"
        
        else:
            self.effect = ""
    
    def joueur_effet(case) -> str:
        return (plateau_jeu[case-1].effect)

#---------------------------------------------------------------

ecran(comment=comment)

pyg.display.flip()

while not(end):

    if comment == "debut":
        if B_jouer.draw(screen = screen, precis= "center") == True:
            comment = "choix_bot/J"
            ecran(comment)
            print("test")
    elif comment == "choix_bot/J":
        if B_botO.draw(screen = screen) == True:
            print("ok")
        elif B_botN.draw(screen = screen) == True:
            print("ok")

    pyg.display.flip()
    for event in pyg.event.get():

        if event.type == pyg.QUIT:
            end = True
        
        elif event.type == pyg.WINDOWRESIZED:
            ecran(comment=comment)

        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_F11:
                window = pyg.display.get_window_size()
                ecran_taille = pyg.display.get_desktop_sizes()

                if window == ecran_taille[0]:
                    screen = pyg.display.set_mode(last_screen,pyg.RESIZABLE)
                    ecran(comment=comment)
                else:
                    last_screen = pyg.display.get_window_size()
                    screen = pyg.display.set_mode((0,0),pyg.FULLSCREEN)
                    ecran(comment=comment)

        
        
        """elif event.type == pyg.WINDOWFOCUSLOST:
            py.notification.notify(
                title = "TEST",
                message = "att c'est un test"
            )"""


pyg.quit()
quit()




# int(input("nombre de joueur (entre 2 et 4) -->"))
stuck = ["prison","puits","hotel_2","hotel"]
joueur = [joueur_info(i+1) for i in range(3)]
plateau_jeu = [plateau(i+1) for i in range(63)]
fin = False
tour = 0
classement = []

print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("GO!")

while not(fin):
    for qui in joueur:
        if qui.joue == False:
            if qui.effet == "hotel_2":
                qui.effet = "hotel"
                continue
            elif qui.effet == "hotel":
                qui.effet = ""
                qui.joue = True
                continue
            else:
                continue
        else:
            déP,déD = rng.randint(1,6),rng.randint(1,6)
            qui.new_position(déP+déD)
            print("----------------------------------------------------")
            print(qui.position)
            print(qui.effet)
            print(déP,"  ",déD)
            print(qui.numero)