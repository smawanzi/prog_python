a = int(input('Valeur a : '))
b = int(input('Valeur b : '))
c = int(input('Valeur c : '))
d = int(input('Valeur d : '))
e = int(input('Valeur e : '))
f = int(input('Valeur f : '))
print ("a = ",a," b = ",b," c = ",c," d = ",d," e = ",e," f = ",f)
a = a+d
d = a-d
a = a-d

a = a+c
c = a-c
a = a-c

b = b+c
c = b-c
b = b-c

c = c+f
f = c-f
c = c-f

c = c+e
e = c-e
c = c-e
print ("a = ",a," b = ",b," c = ",c," d = ",d," e = ",e," f = ",f)
