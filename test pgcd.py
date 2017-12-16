Mawanzi
Sephane
btssio1

exercice 7

def decompose (nb): 
    print("%d=1"%(nb), end=' ') 
    p=2 
    while n>1: 
        while nb%p==0: 
            print("x",p, end=' ') 
            n=n/p 
        p=p+1 
    print("\nb") 

x= int(input("Saisir un nombre: "))
print(decompose(x))


exercice 8

def pgcd(a, b):
    if a % b == 0:
        return b
    else:
        return pgcd(b, a % b)
 
a, b = int(input('Nombre a : ')), int(input('Nombre b : '))
print ('Le PGCD de %d et %d est %d' % (a, b, pgcd(a, b)))
