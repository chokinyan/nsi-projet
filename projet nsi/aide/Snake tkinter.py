from tkinter import *
from random import randrange

# définition des gestionnaires d'evenements :

# Procédure générale de déplacement de la tête du serpent
def move1() :
    "deplacement de serpent1"
    global x, y, dx, dy, flag, temps, bX, bY, score, cX, cY
    nn = len(x)-1
    # Procédure de deplacement de chacun des segments de la queue du serpent :
    while nn > 0:
        x[nn], y[nn] = x[nn-1], y[nn-1]
        nn = nn-1
    # Procédure de deplacement de la tete du serpent
    x[0],y[0] = x[0]+dx, y[0]+dy
    # concerne les extrémités de l'aire
    if x[0] > (cX[1]-10) or x[0]< (cX[0]+15) or y[0]>(cY[1]-10) or y[0]< (cY[0]+15):
        flag = 0
        perdu_gagne.configure(text= "Vous avez perdu !")
    segment = 2
    # Si la tête du serpent touche un des segments de sa queue
    while segment < len(x):
        if x[segment] == x[0] and y[segment] == y[0]:
            flag = 0
            perdu_gagne.configure(text= "Vous avez perdu !")
        segment +=1
    nnn = 0
    while nnn < len(x):
        can1.coords(serpent[nnn],x[nnn]-10,y[nnn]-10,x[nnn]+10,y[nnn]+10)       # recalcule les coordonnées
        nnn += 1
    if flag > 0 and x[0] == bX and y[0] == bY:
        # Le serpent touche le bonus
        score = score +1
        scoreBoard.configure(text = 'Score : '+ str(score))
        placeBonus()
        ajouteSegment()
    if score%10 == 0 and score!=0 and score!=maxScore:
        niveauSuivant()
        score += 1
    if score == maxScore:
        # Fin du jeu quand le score atteind 10
        perdu_gagne.configure(text= "Vous avez gagné !")
        flag = 0
    if flag > 0:
        fen1.after(temps,move1)         # Relance la boucle

# Procédures de changement de direction
def depl_gauche(event):
    global dx, dy, flag
    if flag > 0 and dx==0:
        dx,dy = -20, 0
def depl_bas(event):
    global dx, dy, flag
    if flag > 0 and dy==0:
        dx, dy = 0, 20
def depl_haut(event):
    global dx, dy, flag
    if flag > 0 and dy==0:
        dx, dy = 0, -20
def depl_droite(event):
    global dx, dy, flag
    if flag > 0 and dx==0:
        dx, dy = 20, 0

def stop_it():
    "arrêt de l'animation"
    global flag
    flag =0

def start_it():
    "démarrage de l'animation"
    global flag, dx, dy
    if flag ==0:                    # pour ne lancer qu'une seule boucle
        flag=1
        move1()

def placeBonus():
    "place aléatoirement un bonus sur le canvas"
    global boX, bX, boY, bY, cX, cY
    boX, boY= randrange(cX[1]/20-1), randrange(cY[1]/20-1)          # Genère la coordonnée de la case du bonus
    bX,bY = boX*20+20, boY*20+20                    # Coordonnée du centre du bonus
    test = 0
    # On vérifie si le bonus n'apparait pas sur le serpent
    while test < len(x) :
        if bX== x[test] and bY == y[test]:
            placeBonus()                            # Si c'est le cas, on régénère la position
        test +=1
    can1.coords(bonusBalle, bX-8, bY-8, bX+8, bY+8) # Place le bonus

def ajouteSegment():
    "ajoute un segment à la queue du serpent"
    global x, y
    derX = x[len(x)-1]
    derY = y[len(y)-1]
    x.append(derX)
    y.append(derY)
    serpent.append(0)
    nS = len(x)-1
    serpent[nS] = can1.create_oval(derX-10,derY-10,derX+10,derY+10,width=2, fill='red')

def niveauSuivant():
    "défini la procédure de passage au niveau suivant"
    global niveau, x, y, temps
    perdu_gagne.configure(text= "Level done !")
    niveau = niveau +1                   # incrémente le compteur de score
    niveauBoard.configure(text= "Niveau "+str(niveau))
    temps = temps - 39                   # augmente la vitesse

# ======== Programme principal ============

# les variables suivantes seront utilisées de maniere globale
x = [100,80,60,40,20]   # coordonnées initiales du serpent
y = [40,40,40,40,40]	# A l'origine, le serpent comprend 5 segments
serpent = [0]*5
dx, dy = 20, 0          # vitesse itiniale
flag = 0                # declencheur de l'animation
temps = 350             # temps de pause entre chaque avancement
boX, boY = 15,18        # bonus initial
bX,bY = boX*20, boY*20
score = 0               # score initial
maxScore = 60		    # score maximal
niveau = 1              # niveau initial
cX = [0,600]		    # représente les coordonnées des coins du canvas
cY = [0,460]		    # Obligatoirement des multiples de 20

# Création du widget principal
fen1 = Tk()
fen1.title("Jeu du serpent : Attrapez les bonus oranges !")
# Création des widget esclaves :
can1 = Canvas(fen1,bg='black', height=cY[1], width=cX[1])
can1.grid(row=2, column=1,padx = 5, pady = 5,rowspan=8)
n = 0
while n < len(x):
    serpent[n] = can1.create_oval(x[n]-10,y[n]-10,x[n]+10,y[n]+10,width=2, fill='red')
    n += 1
bonusBalle = can1.create_oval(bX-8, bY-8, bX+8, bY+8, width=2, fill='orange')
# Label s'affichant occasionnellement :
perdu_gagne = Label(fen1)
perdu_gagne.grid(row=2,column=2)
Button(fen1,text='Quitter',width=8,command=fen1.quit).grid(row=9,column=2, pady=5,padx=5)
Button(fen1,text='Demarrer',width=8,command=start_it).grid(row=3,column=2, pady=5,padx=5)
Button(fen1,text='Arreter',width=8,command=stop_it).grid(row=4,column=2)
fra = Frame(fen1)
fra.grid(row=5,column=2)
Frame(fen1, height=150).grid(row=8,column=2)
fen1.bind('<Up>', depl_haut)
fen1.bind('<Down>', depl_bas)
fen1.bind('<Left>', depl_gauche)
fen1.bind('<Right>', depl_droite)
# Affichage du score :
scoreBoard = Label(fen1, text='Score : 0')
scoreBoard.grid(row=6, column=2)
niveauBoard = Label(fen1, text='Niveau 1')
niveauBoard.grid(row=7, column=2)

fen1.mainloop()