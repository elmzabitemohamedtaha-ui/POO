from tkinter import *
from tkinter import messagebox
import re
win=Tk()
win.title("Parite") #exemple: Mon APP
win.geometry("600x350")
win.resizable(False, False)
win.config(bg="#0f172a")
a=StringVar()
def Nouveau():
  a.set("")
  E1.focus()
def Verifier():
    motif=r"^\d+$"
    v1=re.search(motif, a.get())
    if v1==None:
      messagebox.showwarning("Attention", "Veuillez entrer un nombre valide")
      a.set("")
      E1.focus()
    else:
        n=int(a.get())
        if n%2==0:
           messagebox.showinfo("Verification", f"{a.get()} est pair")
        else:
          messagebox.showinfo("Verification", f"{a.get()} est impair")
def Quitter():
  rep=messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter l'application ?")
  if rep:
    win.destroy()
def Aide():
   help="Ce programme vous aide a verifier la parite d'un nombre"
   help +="\nPour ajouter un reinitialiser le nombre veuillez clicker sur le bouton 'Nouveau' "
   help +="\nPour verifier la parite du nombre saisi veuillez clicker sur le bouton 'Verifier' "
   help +="\nPour quitter ce programme veuillez clicker sur le bouton 'Quitter' \nUn message de confirmation sera afficher par la suite "
   help +="\nMerci pour votre comprehension !"
   messagebox.showinfo("Help", help)
Label(win, text="Parite d'un nombre", font=('Segoe UI', 20, 'bold'), fg='cyan', bg='#0f172a').place(x=180, y=70)
Label(win, text="Nombre a verifier: ", font=('Segoe UI', 15, 'bold'), fg='white', bg="#0f172a").place(x=110, y=150)
Button(win, text="Nouveau", font=('Segoe UI', 14, 'bold'), bg="#475569", fg="#f8fafc", command=Nouveau).place(x=100, y=220)
Button(win, text="Verifier", font=('Segoe UI', 14, 'bold'), bg="#2563eb", fg="#f8fafc", command=Verifier).place(x=230, y=220)
Button(win, text="Quitter", font=('Segoe UI', 14, 'bold'), bg="#dc2626", fg="#f8fafc", command=Quitter).place(x=350, y=220)
Button(win, text="Aide", font=('Segoe UI', 14, 'bold'), bg="#d9f100", fg="#f8fafc", command=Aide).place(x=470, y=220)
E1= Entry(win, bg="#FFFFFF", fg="#060708", textvariable=a)
E1.place(x=300, y=160)
win.mainloop()