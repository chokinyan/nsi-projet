#Saber LALAOUNA T°F aussi nommer chokinyan
#Lycée Louis Armand
#Mulhouse
import os as os
import random as rng
import pygame as pyg
import pygame.locals as pygl
import keyboard
from add_pygame import *
import random as rng
import math
from time import sleep
test = "le test a été effectuer"
#-------------------------------------------------------------
class joueur_info:
        def __init__(self,numero,bot,nom = "") -> None:
            self.numero = numero
            self.position = 0
            self.effet = ""
            self.joue = True
            self.bot = bot
            if nom == "":
                self.nom = f"joueur {numero}"
            else:
                self.nom = nom
            

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

#-------------------------------------------------------------
why = int(input("entrer le truc ->"))
if why == 1:
    pyg.init()
    last_screen = 0
    icone = pyg.image.load("projet nsi\image\icone\images.png")
    screen = pyg.display.set_mode((500,500),pyg.RESIZABLE)
    bouton = {}
    end = False
    affichage_etape = 0
    comment = "debut"
    pyg.display.set_icon(icone)
    pyg.display.set_caption("Jeu de l'oie")
    #--------------------------------------------------------------
    
    #temp charge

    #--------------------------------------------------------------
    def ecran(comment = "debut") -> None:
        global bouton
        taille_screen = pyg.display.get_window_size()
        if comment == "debut":
            screen.fill((0,0,0))
            pyg.display.flip()
            print(pyg.image.get_extended())
            test_fond = pyg.image.load(r"projet nsi\image\fond\mare_naturelle.jpg")
            image_size_fond = (taille_screen[0],taille_screen[1])
            test_fond = pyg.transform.scale(test_fond,image_size_fond)
            test_debut = pyg.image.load(r"projet nsi\image\bouton\jouer.png")
            image_size_debut = (taille_screen[0]*(1/2),taille_screen[1]*(1/2))
            test_debut = pyg.transform.scale(test_debut,image_size_debut)
            bouton['B_jouer'] = Button(fild = test_debut)
            screen.blit(test_fond,(0,0))

        elif comment == "choix_bot/J":
            font = pyg.font.SysFont('arial',50,italic=False,bold=True)
            texte = font.render('Veux tu jouer avec des bots ?',True,(0,0,0))
            center = screen.get_rect().center
            image_O = pyg.image.load(r"projet nsi\image\bouton\pas d_ami.png")
            image_N = pyg.image.load(r"projet nsi\image\bouton\g_amis.png")
            image_N = pyg.transform.scale(image_N,(taille_screen[0]/2,taille_screen[1]*0.80))
            image_O = pyg.transform.scale(image_O,(taille_screen[0]/2,taille_screen[1]*0.80))
            bouton["B_botO"] = Button(fild=image_O,x=center[0]-4)
            bouton["B_botN"] = Button(fild=image_N,x=4)
            screen.fill((150,210,255,0))
            screen.blit(texte,(image_N.get_width()/2,image_N.get_height()))

        elif comment=="choix_nb_bot":
            pass

        elif comment=="choix_nb_joueur":
            pass


        elif comment == "partie":
            screen.fill((150,210,255,0))
            plateaux = pyg.image.load(r"projet nsi\image\image sans droit et utilisable\plateau\plateau.png")
            plateaux = pyg.transform.scale(plateaux,(taille_screen[0]*0.5,taille_screen[1]))
            bottomright = screen.get_rect().bottomright
            bottom = screen.get_rect().bottom
            for i in range(10):
                dée_1_img = pyg.image.load(f"projet nsi\image\dée\{rng.randint(1,6)}.png")
                screen.blit(dée_1_img,dée_1_img.get_rect(bottomright = bottomright))
                screen.blit(plateaux,plateaux.get_rect(bottom = bottom))
                #dée_size = (pyg.display.get_window_size()[0]/2,pyg.display.get_window_size()[1]/2)
                #dée_1_img = pyg.transform.scale(dée_1_img,dée_size)
                pyg.display.flip()
                dée_sound = pyg.mixer.Sound(r"projet nsi\Son\test\dée.mp3")
                #dée_sound.play()
                pyg.time.wait(1)
                #Son\dée\test.mp3
                


        elif comment == "test":
            print(pyg.display.get_driver())
            pass

#---------------------------------------------------------------

    ecran(comment)

    pyg.display.flip()

    while not(end):

        if comment == "debut":
            if bouton["B_jouer"].draw(screen = screen, precis= "center") == True:
                comment = "choix_bot/J"
                ecran(comment)
                print("test")
                pyg.time.wait(100)
        elif comment == "choix_bot/J":
            if bouton["B_botO"].draw(screen = screen) == True:
                comment = "test"
                ecran(comment)
                pyg.time.wait(100)
            elif bouton["B_botN"].draw(screen = screen) == True:
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

else:
    # int(input("nombre de joueur (entre 2 et 4) -->"))
    stuck = ["prison","puits","hotel_2","hotel"]
    joueur = [joueur_info(numero = i+1,bot=False) for i in range(3)]
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