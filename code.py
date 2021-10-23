
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

#calcul de delta
delta=b**2-4*a*c

#affichage
print("Résolution de l'équation ",a,"x² + ",b,"x + ",c)


if delta>0:
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
    print("Delta est positif -> 2 solutions")
    print("x1 =",x1)
    print("x2 =",x2)
else:
    if delta==0:
        x0=-b/(2*a)
        print("Delta est nul -> 1 solution unique")
        print("x0 =",x0)
    else:
        print("Pas de solution sur IR")
