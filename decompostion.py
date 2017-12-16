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
