'''#FUNKCJA A
a=float(input('Podaj zmienną a '))

if (a > 0):
 a*=2
 print('Funckja a wynosi = ',a)
elif (a<0):
 a*=-3
 print("Funckja a wynosi =",a)
else: print("Funckja a wynosi =",a)


#FUNCKJA B
b=float(input('Podaj zmienną b '))

if (b >= 1):
 b**=2
 print('Funckja b wynosi = ',b)
else: print('Funckja b wynosi = ',b)


#FUNKCJA C
c=float(input('Podaj zmienną c '))

if (c > 2):
 c+=2
 print('Funckja c wynosi = ',c)
elif (c<2):
 c-=4
 print("Funckja c wynosi =",c)
else: print("Funckja c wynosi = 8.0")'''

#SPOSÓB 2
a=int(input('Podaj zmienną a '))

if a==2:
    a+=6
    print('a=',a)
    exit()
else:
     if a>0:
        a **= 2
        print('a=',a)
     elif a<0:
        a *=-3
        print('a=',a)
