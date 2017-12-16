#ex8

S=int(100*float(input("saisir le nb a payer:")))
c, S = S//50 , S%50
d, S = S//20 , S%20
e, S = S//10 , S%10
f, S = S//5 , S % 5
g, S = S//2 , S % 2
print("pour payer la somme S, il, au minimum",c+d+e+f+g+S,"pieces")
print(c,"pièces de 0.50€")
print(d,"pièces de 0.20€")
print(e,"pièces de 0.10€")
print(f,"pièces de 0.05€")
print(g,"pièces de 0.02€")
print(S,"pièces de 0.01€")
