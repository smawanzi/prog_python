
        

def tableau(tab):
    for k in range(len(tab)):
        if k%10==9:
            print(tab[k])
        else:
            print(tab[k],"\t",end=" ")

def Fusion(t1,t2):
    res=[ ]
    m1=n1=0
    while m1<len(t1) and n1<len(t2):
        if t1[m1]<t2[n1]:
            res.append(t1[m1])
            m1=m1+1
        else:
            res.append(t2[n1])
            n1=n1+1
        if m1==len(t1):
            res+=t2[n1:]
        else:
            res+=t1[n1:]
        return res





def TriFusion(T) :
    if len(T) > 1 :
        if len(T) == 2 :
            if T[0]>T[1] : T[0],T[1] = T[1],T[0]
        else :
            m = len(T)/2
            T = Fusion(TriFusion(T[:m]),TriFusion(T[m:]))
    return T

from random import*
n=int(input ("entrez le nombre n d'éléments à trier "))
tab1=[]
for k in range(n):
    tab1=tab1+[randrange(1,100)]
    if k%10==9:
        print(tab1[k])
    else:
        print (tab1[k],"\t",end=" ")


n=int(input ("entrez le nombre n d'éléments à trier "))
tab2=[]
for k in range(n):
    tab2=tab2+[randrange(1,100)]
    if k%10==9:
        print(tab2[k])
    else:
        print (tab2[k],"\t",end=" ")

tableau(tab1)
tableau(tab2)
TriFusion(tab1)

