#chokinyan 
#juste voila
"""
les parties de code mis en commantaire sont ceux qui ne serront pas mis lors du rendu, du a un manque de temps faut dire je taffe casi seul
"""
import keyboard
import os as os
import random as rng
import pygame as pyg
import add_pygame as addp
import random as rng
import math as math
from time import sleep
import sys
test = "le test a été effectuer"
why = 1
#-------------------------------------------------------------
class joueur_info:
        def __init__(self,numero:int,bot:bool,nom :str = "") -> None:
            self.numero = numero
            self.position = 0
            self.effet = ""
            self.joue = True
            self.bot = bot
            self.nom = f"joueur {numero}"
            
        def new_position(self,total:int) -> None:
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

        def id_case(self,new_pos:int) -> None:
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
        def __init__(self,numero_case : int) -> None:
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
        
        def joueur_effet(case:int) -> str:
            return (plateau_jeu[case-1].effect)

class screen:
    def __init__(self,h : int = 500,w : int = 500,icone : str = "" , dis_name : str = "", addon  : int = 0) -> None:
        if icone != "":
            self.icone = pyg.image.load(icone)
            pyg.display.set_icon(self.icone)
        if dis_name != "":
            pyg.display.set_caption(dis_name)
        self.scr = pyg.display.set_mode((h,w),addon)
    
    def clear(self,bg : tuple[int,int,int,int] = (0,0,0,0)) -> None:
        self.scr.fill(bg)

class etat_screen:
    def __init__(self,disp : screen) -> None:
        self.disp = disp
        self.size()
        self.etat = ""
        self.image_R = pyg.image.load(r"projet nsi\image\retour\Sans titre.png")
        self.debut()

    def size(self) -> None:
        self.taille_screen = self.disp.scr.get_size();self.center = (self.disp.scr).get_rect().center;self.topleft = (self.disp.scr).get_rect().topleft;self.topright = (self.disp.scr).get_rect().topright;self.bottom = (self.disp.scr).get_rect().bottom;self.bottomleft =  (self.disp.scr).get_rect().bottomleft;self.bottomright = (self.disp.scr).get_rect().bottomright;self.left = (self.disp.scr).get_rect().left;self.right = (self.disp.scr).get_rect().right

    def reload_screen(self) -> None:
        self.size()
        getattr(self,self.etat)()

    def debut(self)-> None:
        self.etat = sys._getframe(0).f_code.co_name
        self.disp.clear()
        pyg.display.flip()
        test_fond = pyg.image.load(r"projet nsi\image\fond\mare_naturelle.jpg")
        image_size_fond = (self.taille_screen[0],self.taille_screen[1])
        test_fond = pyg.transform.scale(test_fond,image_size_fond)
        test_debut = pyg.image.load(r"projet nsi\image\bouton\jouer.png")
        image_size_debut = (self.taille_screen[0]*(1/2),self.taille_screen[1]*(1/2))
        test_debut = pyg.transform.scale(test_debut,image_size_debut)
        bouton.update(B_jouer = addp.Button(fild = test_debut))
        ((self.disp).scr).blit(test_fond,(0,0))
        pyg.display.flip()

    def choix_bot_or_J(self) -> None:
        self.etat = "choix_bot_or_J"
        ((self.disp).clear((150,210,255,0)))
        font = pyg.font.SysFont('arial',50,italic=False,bold=True)
        texte = font.render('Veux tu jouer avec des bots ?',True,(0,0,0))
        image_O = pyg.image.load(r"projet nsi\image\bouton\pas d_ami.png")
        image_N = pyg.image.load(r"projet nsi\image\bouton\g_amis.png")
        image_N = pyg.transform.scale(image_N,(self.taille_screen[0]/2,self.taille_screen[1]*0.80))
        image_O = pyg.transform.scale(image_O,(self.taille_screen[0]/2,self.taille_screen[1]*0.80))
        bouton.update(B_botO = addp.Button(fild=image_O,x=self.center[0]-4))
        bouton.update(B_botN = addp.Button(fild=image_N,x=4))
        ((self.disp).scr).blit(texte,(self.center[0]/2,image_N.get_height()))

    def choix_nb_bot(self) -> None:
        self.etat = sys._getframe(0).f_code.co_name
        ((self.disp).clear((150,210,255,0)))
        font = pyg.font.SysFont('arial',50,italic=False,bold=True)
        texte = font.render('Avec combien de bot voulez-vous jouer ?',True,(240,0,30))
        image_1 = pyg.image.load(r"projet nsi\image\nb robot\1.jpg")
        image_2 = pyg.image.load(r"projet nsi\image\nb robot\2.jpg")
        image_3 = pyg.image.load(r"projet nsi\image\nb robot\3.jpg")
        image_1 = pyg.transform.scale(image_1,(image_1.get_size()[0]*(1/3),image_1.get_size()[1]*0.5))
        image_2 = pyg.transform.scale(image_2,(image_2.get_size()[0]*(1/3),image_2.get_size()[1]*0.5))
        image_3 = pyg.transform.scale(image_3,(image_3.get_size()[0]*(1/3),image_3.get_size()[1]*0.5))
        self.image_R = pyg.transform.scale(self.image_R,(pyg.display.get_window_size()[0]/2,pyg.display.get_window_size()[1]/10))
        
        bouton.update(bot1 = addp.Button(fild=image_1,x=(self.center[0]-image_2.get_width())-image_1.get_width()*0.5,y=self.center[1]-(image_1.get_height()/2)))
        bouton.update(bot2 = addp.Button(fild=image_2,x=self.center[0],y=self.center[1]-(image_1.get_height()/2)))
        bouton.update(bot3 = addp.Button(fild=image_3,x=image_2.get_width()+self.center[0]+image_3.get_width()*0.5,y=self.center[1]-(image_1.get_height()/2)))
        bouton.update(B_retour = addp.Button(fild=self.image_R,y=pyg.display.get_window_size()[1]-self.image_R.get_height(),x=self.center[0]-self.image_R.get_width()/2))
        ((self.disp).scr).blit(texte,(self.center[0]/2,0))

    def choix_nb_joueur(self) -> None:
        self.etat = sys._getframe(0).f_code.co_name
        ((self.disp).clear((150,210,255,0)))
        font = pyg.font.SysFont('arial',50,italic=False,bold=True)
        texte = font.render('Combien etes-vous ?',True,(240,0,30))
        image_1 = pyg.image.load(r"projet nsi\image\nb joueur\2V.jpg")
        image_1_F = pyg.image.load(r"projet nsi\image\nb joueur\2X.jpg")
        image_2 = pyg.image.load(r"projet nsi\image\nb joueur\3V.jpg")
        image_2_F = pyg.image.load(r"projet nsi\image\nb joueur\3X.jpg")
        image_3 = pyg.image.load(r"projet nsi\image\nb joueur\4V.jpg")
        image_3_F = pyg.image.load(r"projet nsi\image\nb joueur\4X.jpg")
        image_1 = pyg.transform.scale(image_1,(image_1.get_size()[0]*(1/3),image_1.get_size()[1]*0.5))
        image_2 = pyg.transform.scale(image_2,(image_2.get_size()[0]*(1/3),image_2.get_size()[1]*0.5))
        image_3 = pyg.transform.scale(image_3,(image_3.get_size()[0]*(1/3),image_3.get_size()[1]*0.5))
        image_1_F = pyg.transform.scale(image_1_F,(image_1_F.get_size()[0]*(1/3),image_1_F.get_size()[1]*0.5))
        image_2_F = pyg.transform.scale(image_2_F,(image_2_F.get_size()[0]*(1/3),image_2_F.get_size()[1]*0.5))
        image_3_F = pyg.transform.scale(image_3_F,(image_3_F.get_size()[0]*(1/3),image_3_F.get_size()[1]*0.5))

        self.image_R = pyg.transform.scale(self.image_R,(pyg.display.get_window_size()[0]/2,pyg.display.get_window_size()[1]/10))
        
        bouton.update(BJ2 = addp.Button(fild=image_1,x=(self.center[0]-image_2.get_width())-image_1.get_width()*0.5,y=self.center[1]-(image_1.get_height()/2)))
        bouton.update(BJ3 = addp.Button(fild=image_2,x=self.center[0],y=self.center[1]-(image_1.get_height()/2)))
        bouton.update(BJ4 = addp.Button(fild=image_3,x=image_2.get_width()+self.center[0]+image_3.get_width()*0.5,y=self.center[1]-(image_1.get_height()/2)))

        bouton.update(BJ2F = addp.Button(fild=image_1_F,x=(self.center[0]-image_2_F.get_width())-image_1_F.get_width()*0.5,y=self.center[1]-(image_1_F.get_height()/2)))
        bouton.update(BJ3F = addp.Button(fild=image_2_F,x=self.center[0],y=self.center[1]-(image_1_F.get_height()/2)))
        bouton.update(BJ4F = addp.Button(fild=image_3_F,x=image_2_F.get_width()+self.center[0]+image_3_F.get_width()*0.5,y=self.center[1]-(image_1_F.get_height()/2)))

        bouton.update(B_retour = addp.Button(fild=self.image_R,y=pyg.display.get_window_size()[1]-self.image_R.get_height(),x=self.center[0]-self.image_R.get_width()/2))
        ((self.disp).scr).blit(texte,(self.center[0]/2,0))
    
    def choix_nom(self) -> None:
        global joueur
        self.etat = sys._getframe(0).f_code.co_name
        ((self.disp).clear((150,210,255,0)))
        font = pyg.font.SysFont('arial',50,italic=False,bold=True)
        texte = font.render('Entre ton nom',True,(240,0,30))
        if "nom" not in textinp:
            joueur = [joueur_info(i,False,f"joueur {i}") for i in range(nb_bot+nb_j)]
            textinp.update(nom = addp.TextInput(screen = (etat.disp).scr,bg = (255,255,255),text_color=(0,0,0),x=etat.taille_screen[0] - (2*(etat.taille_screen[0]/3)),y= etat.taille_screen[1] - (2*(etat.taille_screen[1]/3)),h = etat.taille_screen[1]/3,w = etat.taille_screen[0]/3))
        bouton.update(B_retour = addp.Button(fild=self.image_R,y=pyg.display.get_window_size()[1]-self.image_R.get_height(),x=self.center[0]-self.image_R.get_width()/2))
        ((self.disp).scr).blit(texte,(self.center[0],0))

    def partie(self,dée : bool = False) -> None:
        global pion
        self.etat = sys._getframe(0).f_code.co_name
        ((self.disp).clear((150,210,255,0)))
        haut = 0
        for i in range(len(joueur)):
            pion.__setitem__(i+1,pyg.image.load(f"projet nsi\image\pion\pion{i+1}.png"))
            #pion[i+1] = pyg.transform.scale(pion[i+1])
            pion[i+1]
        font = pyg.font.SysFont(name = 'None',size = 30)
        image_lance = pyg.image.load(r"projet nsi\image\dée\lance.png")
        image_lance = pyg.transform.scale(image_lance,(pyg.display.get_window_size()[0]/3,pyg.display.get_window_size()[1]/7))
        plateaux = pyg.image.load(r"projet nsi\image\image sans droit et utilisable\plateau\plateau.png")
        plateaux = pyg.transform.scale(plateaux,(self.taille_screen[0]*0.5,self.taille_screen[1]))
        bouton.update(Blance = addp.Button(x = pyg.display.get_window_size()[0]-image_lance.get_width(),y = pyg.display.get_window_size()[1]-image_lance.get_height() ,fild = image_lance))
        dée_1_img = pyg.image.load(r"projet nsi\image\dée\1.png")
        ((self.disp).scr).blit(dée_1_img,(pyg.display.get_window_size()[0]-dée_1_img.get_width(),pyg.display.get_window_size()[1]-(image_lance.get_height()+dée_1_img.get_height())))
        ((self.disp).scr).blit(plateaux,plateaux.get_rect(bottom = self.bottom))
        for j in pion.values():
            ((self.disp).scr).blit(j,plateaux.get_rect(bottom = self.bottom))
        for i in joueur:
            texte = f"{i.nom} , postion : {i.position}"
            texte = font.render(texte,False,(0,0,0))
            ((self.disp).scr).blit(texte,(pyg.display.get_window_size()[0]-texte.get_width(),0+haut))
            haut += texte.get_height()

        if dée:
        
            for i in range(10):

                dée_1_img = pyg.image.load(f"projet nsi\image\dée\{rng.randint(1,6)}.png")
                ((self.disp).scr).blit(dée_1_img,(pyg.display.get_window_size()[0]-dée_1_img.get_width(),pyg.display.get_window_size()[1]-(image_lance.get_height()+dée_1_img.get_height())))
                ((self.disp).scr).blit(plateaux,plateaux.get_rect(bottom = self.bottom))
                pyg.display.flip()
                dée_sound = pyg.mixer.Sound(r"projet nsi\Son\test\dée.mp3")
                #dée_sound.play()
                #pyg.time.wait(300)
                #Son\dée\test.mp3
    
    def test(self) -> None:
        self.disp.clear()
        self.etat = sys._getframe(0).f_code.co_name
        print(pyg.display.get_driver())

#-------------------------------------------------------------
nb_bot = 0
nb_j = 1
pyg.init()
last_screen = 0
bouton = {}
pion = {}
joueur = None
textinp = {}
end = False
ecran = screen(icone = r"projet nsi/image/icone/images.png",dis_name="Jeu de l'oie",h=1280,w= 720)
etat = etat_screen(disp=ecran)
#--------------------------------------------------------------

#temp code test

#--------------------------------------------------------------

while not(end):

    pyg.display.flip()

    match etat.etat:

        case "debut":
            if bouton["B_jouer"].draw(screen = ecran.scr, precis= "center"):
                etat.choix_bot_or_J()
                pyg.time.wait(200)

        case "choix_bot_or_J":
            if bouton["B_botO"].draw(screen = ecran.scr):
                etat.choix_nb_bot()
                pyg.time.wait(200)
            elif bouton["B_botN"].draw(screen = ecran.scr):
                etat.choix_nb_joueur()
                pyg.time.wait(200)

        case "choix_nb_bot":
            if bouton["bot1"].draw(screen = ecran.scr):
                nb_bot = 1
                etat.choix_nb_joueur()
                pyg.time.wait(200)
            elif bouton["bot2"].draw(screen = ecran.scr):
                nb_bot = 2
                etat.choix_nb_joueur()
                pyg.time.wait(200)
            elif bouton["bot3"].draw(screen = ecran.scr):
                etat.partie()
                pyg.time.wait(200)
            elif bouton["B_retour"].draw(screen=ecran.scr):
                etat.choix_bot_or_J()
                pyg.time.wait(200)
    
        case "choix_nb_joueur":

            if nb_bot == 0:
                if bouton["BJ2"].draw(screen=ecran.scr):
                    nb_j = 1
                    etat.choix_nom()
                elif bouton["BJ3"].draw(screen=ecran.scr):
                    nb_j = 3
                    etat.choix_nom()
                elif bouton["BJ4"].draw(screen=ecran.scr):
                    nb_j = 4
                    etat.choix_nom()
            elif nb_bot == 1:
                if bouton["BJ2"].draw(screen=ecran.scr):
                    nb_j = 2
                    etat.choix_nom()
                elif bouton["BJ3"].draw(screen=ecran.scr):
                    nb_j = 3
                    etat.choix_nom()
                elif bouton["BJ4F"].draw(screen=ecran.scr):
                    pass
            elif nb_bot == 2:
                if bouton["BJ2"].draw(screen=ecran.scr):
                    nb_j = 2
                    etat.choix_nom()
                elif bouton["BJ3F"].draw(screen=ecran.scr):
                    pass
                elif bouton["BJ4F"].draw(screen=ecran.scr):
                    pass
            
            if bouton["B_retour"].draw(screen=ecran.scr):
                etat.choix_bot_or_J()
                pyg.time.wait(200)

        case "choix_nom":
            if bouton["B_retour"].draw(screen=ecran.scr):
                etat.debut()
                textinp.clear()
                pyg.time.wait(200)
    
        case "partie":
            if bouton["Blance"].draw(screen = ecran.scr):
                etat.partie(True)

    if keyboard.is_pressed("Esc"):
        end = True

    for event in pyg.event.get():

        if etat.etat == "choix_nom":
            textinp["nom"].draw(event=event,screen = (etat.disp).scr)

        if event.type == pyg.QUIT:
            end = True
        
        #elif event.type == pyg.WINDOWRESIZED:
        #    etat.reload_screen()
        #    if etat.etat == "choix_nom":
        #        textinp["nom"].update_size({"x" : etat.taille_screen[0] - (2*(etat.taille_screen[0]/3)),"y" :  etat.taille_screen[1] - (2*(etat.taille_screen[1]/3)),"h" : etat.taille_screen[1]/3,"w" : etat.taille_screen[0]/3})

        elif event.type == pyg.KEYDOWN:

            if etat.etat == "choix_nom":
                    if event.key == pyg.K_RETURN and textinp["nom"].focus:
                        if textinp["nom"].text != '':
                            joueur[0].nom = textinp["nom"].text
                        pyg.mouse.set_cursor(textinp["nom"].cursor)
                        etat.partie()

        #    if event.key == pyg.K_F11:
        #        window = pyg.display.get_window_size()
        #        ecran_taille = pyg.display.get_desktop_sizes()
        #        if window == ecran_taille[0]:
        #            ecran.scr = pyg.display.set_mode(last_screen,pyg.RESIZABLE)
        #            etat.reload_screen()
        #        else:
        #            last_screen = pyg.display.get_window_size()
        #            ecran.scr = pyg.display.set_mode((0,0),pyg.FULLSCREEN)
        #            etat.reload_screen()
                
        #elif event.type == pyg.WINDOWFOCUSLOST:
        #    py.notification.notify(
        #        title = "TEST",
        #        message = "att c'est un test"
        #    )

pyg.quit()
quit()

stuck = ["prison","puits","hotel_2","hotel"]
joueur = [joueur_info(numero = i+1,bot=False) for i in range(3)]
plateau_jeu = [plateau(i+1) for i in range(63)]
fin = False
tour = 0
classement = []

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