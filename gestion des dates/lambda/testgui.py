#Tkinter est une bibliothéque qui permet
#de générer (créer) une interface graphique
#utilisateur GUI
from tkinter import *
from tkinter import messagebox
import re
def nouveau():
    a.set("")   #vider le contenu du widget E1
    b.set("")   #vider le contenu du widget E2   
    r.set("")   #vider le contenu du widget E3
    E1.focus()  #mettre le curseur à widget E1
def quitter():
    rep=messagebox.askyesno("Quitter","Voulez-vous vraiment quitter l'application?")
    if rep:
        win.destroy() #permet de quitter l'application
def calculer():
    motif=r"^\d+$"
    v1=re.search(motif,a.get())
    v2=re.search(motif,b.get())
    if v1==None:
        messagebox.showerror("Erreur","Veuillez saisir un nombre")
        a.set("")
        E1.focus()
    elif v2==None:
        messagebox.showerror("Erreur","Veuillez saisir un nombre")
        b.set("")
        E2.focus()
    else:
        x=float(a.get())#convertit le contenu du variable en float
        y=float(b.get())#convertit le contenu du variable en float
        z=x+y
        r.set(f"{z:.2f}")#met le resultat dans la variable r
win=Tk()
#Tk est la classe qui contient
#tout ce qu'il faut pour engendre une fenetre
#et la personnaliser (titre, taille, couleur,...)
#définir un titre pour notre fenetre
win.title("Mon App")#exemple: Mon App
win.geometry("400x300+300+150")#définir une taille
#à la fenetre geometry("widthxheight")
#Empecher l'utilisateur de redimensinner 
#(augmenter ou réduire) la taille de notre fenetre
win.resizable(False,False)
#un icône pour notre fenêtre
'''win.iconbitmap("computer.ico")'''
#une couleur d'arriére-plan pour notre fenêtre
win.config(bg='gray')
#déclaration des variables
a=StringVar()   #pour le 1er nombre
b=StringVar()   #pour le second nombre  
r=StringVar()   #pour le texte Resultat

   
       
#label pour le titre
Label(win,text="Simple Claculatrice",font=('Courier New',12,'bold'),fg='blue',bg='yellow').place(x=150,y=10)
Label(win,text="Le premier nombre:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=50)
Label(win,text="Le second nombre:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=80)
Button(win,text="Nouveau",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=nouveau).place(x=30,y=130)
Button(win,text="Calculer",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=calculer).place(x=150,y=130)
Button(win,text="Quitter",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=quitter).place(x=270,y=130)
#lier le widget E1 à 
#la variable a via l'attribut textvariable
E1=Entry(win,textvariable=a)
E1.place(x=220,y=50)
E2=Entry(win,textvariable=b)
E2.place(x=220,y=80)
Label(win,text="Resultat:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=180)
E3=Entry(win,textvariable=r)
E3.place(x=220,y=180)
win.mainloop() #pour faire apparaître la fenetre