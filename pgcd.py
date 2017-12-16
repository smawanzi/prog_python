def pgcd(a, b):
    if a % b == 0:
        return b
    else:
        return pgcd(b, a % b)
 
a, b = int(input('Nombre a : ')), int(input('Nombre b : '))
print ('Le PGCD de %d et %d est %d' % (a, b, pgcd(a, b)))
