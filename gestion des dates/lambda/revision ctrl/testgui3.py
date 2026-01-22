from tkinter import *
from tkinter import messagebox
import re 
fen=Tk()
fen.title("La parite ")
fen.geometry("600x499")
fen.config(bg="#0f172a")
a=StringVar()
def nouveau():
    a.set("")
def verifier():
    motif=r"^\d+\.?$"
    ver=re.search(motif,a.get())
    if ver==None:
        messagebox.showwarning("Attention?"," Veuillez saisir un nombre")
        a.set("")
        E1.focus()
    else:
        n=int(a.get())
        if n <= 1:
           messagebox.showinfo("Resultat",f"{n} n'est pas un nombre premier")
        else:
            for i in range(2, int(n**0.5) + 1):
                 if n % i == 0:
                    messagebox.showinfo("Resultat",f"{n} n'est pas un nombre premier")
                    break
            else:
                messagebox.showinfo("Resultat",f"{n} est un nombre premier")
       
def quitter():
    rep =messagebox.askyesno("quitter","Voulez vous vraimant quitter")
    if rep:
       fen.destroy()                                                                                                      
def aide():
    help="1-veuillez saisir un nombre dans le champs indiqué\n 2-tu clique sur verifier pour etudier si ce nombre est premier ou non \n3- Clique sur nouveau pour reinitialiser \n 4-lique sur quitter pour quitter le programme"
    messagebox.showinfo("aide",help)
Label(fen, text="Etude de parité ", font=('Segoe UI', 12, 'bold'), fg='cyan', bg='#0f172a').place(x=250, y=10)
Label(fen, text="Veuillez saisir un nombre : ", font=('Segoe UI', 11, 'bold'), fg='white', bg="#0f172a").place(x=75, y=85)
E1= Entry(fen, bg="#FCFCFC", fg="#000000", textvariable=a)
E1.place(x=290, y=88)
Button(fen, text="Nouveau", font=('Segoe UI', 12, 'bold'), bg="#4733FE", fg="#f8fafc", command=nouveau).place(x=100, y=170)
Button(fen, text="Verifier", font=('Segoe UI', 12, 'bold'), bg="#226D25", fg="#f8fafc", command=verifier).place(x=200, y=170)
Button(fen, text="Quitter", font=('Segoe UI', 12, 'bold'), bg="#ED1B1B", fg="#f8fafc", command=quitter).place(x=300, y=170)
Button(fen, text="Aide", font=('Segoe UI', 12, 'bold'), bg="#475569", fg="#f8fafc", command=aide).place(x=400, y=170)


fen.mainloop()