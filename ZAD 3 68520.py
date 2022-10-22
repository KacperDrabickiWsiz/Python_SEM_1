import math
a=float(input('Podaj zmienną a '))
b=float(input('Podaj zmienną b '))
c=float(input('Podaj zmienną c '))
if (a==0):
    print('Brak rozwiązań')
    exit()

else:
    delta=(b*b)-4*a*c
    if (delta<0):
        print('Brak rozwiązań')
    elif (delta==0):
        x=-b/(2*a)
        print('Jedno rozwiązanie x = ',x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print('x1 = ',x1)
        print('x2 = ',x2)