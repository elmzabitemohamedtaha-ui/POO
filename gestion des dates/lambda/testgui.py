#tkhinter est une bibliotheque qui permet 
#de generee (creer) une interface graphique
#utilisateur GUI
from tkinter import *
win=Tk()
#tk est la classe qui contient
#tout ce qu'il faut pour engendre une fenetre
#et la personnaliser (titre,taille,couleur,...)
#defenir un titre pour notre fenetre
win.title("mon app")#exemple :mon app
win.geometry("400x300+300+150")#definir une taille 
#a la fenetre geometry("widhxheight")
#empecher l'utilisateur de redimensinner
win.resizable(False,False)
#un icone pour notre fenetre
'''win.iconbitmap("nomfichiers.ico")'''
#une couleur d'arriere-plan pour notre fenetre
win.config(bg="gray")
a=StringVar()#pour le 1er nombre
b=StringVar() #pour le second nombre
r=StringVar()#pour le texte Resultat
def nouveau():
    a.set("") #VIDER LE CONTENU DE WIDGET
    b.set("")
    r.set("")
    E1.focus()#mettre le curseur sur widget E1
#label pour le titre
Label(win,text="siumple Calculatrice",font=('tahoma',12,'bold'),fg='cyan',bg='yellow').place(x=150,y=10)

Label(win,text="le premier nombre:",font=('courier New',11,'bold'),bg='gray').place(x=20,y=50)
Label(win,text="le deuxieme nombre:",font=('courier New',11,'bold'),bg='gray').place(x=20,y=80)
Button(win,text="nouveau",font=('courier new',12,'bold'),bg='black',fg='yellow',command=nouveau).place(x=30,y=130)
Button(win,text="Calculer",font=('courier new',12,'bold'),bg='black',fg='yellow').place(x=150,y=130)
Button(win,text="Quitter",font=('courier new',12,'bold'),bg='black',fg='yellow').place(x=270,y=130)
#lier le widget E1 a la var a via l'attribut
#textvariabke

E1=Entry(win,textvariable=a)
E1.place(x=220,y=50)
E2=Entry(win,textvariable=b)
E2.place(x=220,y=80)
Label(win,text='resultat:',font=('courier New',11,'bold'),bg='gray').place(x=20,y=180)
E3=Entry(win,textvariable=r)
E3.place(x=220,y=180)




win.mainloop()#pour faire apparaitre la fenetre 