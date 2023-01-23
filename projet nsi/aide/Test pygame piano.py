# Test de Piano

from tkinter import *   # Importation du module tkinter
import pygame           # Importation du module pygame

pygame.init()
pygame.mixer.init()

#Fenetre principal
fenetre=Tk()
fenetre.geometry('710x200')
fenetre.configure

fenetre.title("Essai Piano à 8 touches")

# Création du cadre qui contient une touche du clavier
cadre = Frame(fenetre, borderwidth = 15)       # espace entre la fenêtre et le cadre
cadre.grid(row = 1, column = 0)

# Création du cadre dans le cadre
frame=Frame(cadre)
frame.grid()

# Fonction qui permet de lire une note

def joue_Note(note):
    touche = notes[note]
    touche.play()

# Les 8 touches du piano

do = Button(frame,padx=0, height=10,width=10, pady=0,bd=0,text="DO", bg="white",fg="black",command=lambda: joue_Note('DO'))
do.grid(row = 0, column = 1,padx=5,pady=5,sticky = "ns")
re = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="RE", bg="white",fg="black",command=lambda: joue_Note('RE'))
re.grid(row = 0, column = 2,padx=5,pady=5,sticky = "ns")
mi = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="MI", bg="white",fg="black",command=lambda: joue_Note('MI'))
mi.grid(row = 0, column = 3,padx=5,pady=5,sticky = "ns")
fa = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="FA", bg="white",fg="black",command=lambda: joue_Note('FA'))
fa.grid(row = 0, column = 4, padx=5,pady=5,sticky = "ns")
sol = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="SOL", bg="white",fg="black",command=lambda: joue_Note('SOL'))
sol.grid(row = 0, column = 5,padx=5,pady=5, sticky = "ns")
la = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="LA", bg="white",fg="black",command=lambda: joue_Note('LA'))
la.grid(row = 0, column = 6,padx=5,pady=5, sticky = "ns")
si = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="SI", bg="white",fg="black",command=lambda: joue_Note('SI'))
si.grid(row = 0, column = 7,padx=5,pady=5, sticky = "ns")
do2 = Button(frame,padx=0, height=1,width=10, pady=0,bd=0,text="DO2", bg="white",fg="black",command=lambda: joue_Note('DO2'))
do2.grid(row = 0, column = 8,padx=5,pady=5, sticky = "ns")

# Notes

notes = {
    'DO': pygame.mixer.Sound("Son\Do.wav"),
    'RE': pygame.mixer.Sound("Son\Re.wav"),
    'MI': pygame.mixer.Sound("Son\Mi.wav"),
    'FA': pygame.mixer.Sound("Son\Fa.wav"),
    'SOL': pygame.mixer.Sound("Son\Sol.wav"),
    'LA': pygame.mixer.Sound("Son\La.wav"),
    'SI': pygame.mixer.Sound("Son\Si.wav"),
    'DO2': pygame.mixer.Sound("Son\Do2.wav")
}

mainloop()

