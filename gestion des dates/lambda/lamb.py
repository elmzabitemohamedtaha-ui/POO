msg=lambda:print("bonjour tout le monde")
#appel
msg()
#fonction lambda somme
som=lambda a,b:a+b
#appel
x=int(input("taper le premier nombre:"))
y=int(input("taper le deuxieme nombre:"))
print(f"la somme est:{som(x,y)}")

carree=lambda x: x*x
x=int(input("taper un nombre:"))
print(f"le carre de {x} est:{carree(x)}")
#fonction parite
parite=lambda n:"pair"if n%2==0 else "impair"
#appel
a=int
