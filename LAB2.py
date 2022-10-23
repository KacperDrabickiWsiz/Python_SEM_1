#ZADANIE 1
'''a=int(input('Podaj wiek: '))

if a<4:
    cena=0
elif a<=18:
    cena=10
else: cena=20
print(f'Cena= {cena}zł')'''

#ZADANIE 2
'''
print("""
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie 
5) potęgowanie """)

z=int(input('Jaką operacje chcesz wykoać: '))
if z>=6 or z<=0:
    print('Niepoprawna wartość')
    exit()

x=float(input('Podaj wartość 1: '))
y=float(input('Podaj wartość 2: '))

if z==1:
    w=x+y
elif z==2:
    w=x-y
elif z==3:
    w=x*y
elif z==4:
    if y==0:
        print('Niepoprawna wartość')
        exit()
    else:
        w=x/y
elif z==5:
    w=x**y

print(f'Wynik = {w}')'''

#PĘTLA WHILE
'''
a=int(input('Podaj liczbę: '))
b=int(input('Podaj liczbę: '))

if a>b:
    wieksza = a
    mniejsza = b
else:
    wieksza = b
    mniejsza = a

while(mniejsza <= wieksza):
    print(mniejsza, end=' ')
    mniejsza = mniejsza + 1
'''
#ZADANIE 2
'''
x = -4
while x<=4:
    print(f"f{x} = {2*x**2-5*x-8}")
    x+=0.5
    '''
#ZADANIE 3
'''
while True:
    x=int(input('Podaj liczbe:'))
    if x<0: break
'''
#ZADANIE 4
a=int(input('Podaj liczbę: '))
b=int(input('Podaj liczbę: '))

if a>b:
    wieksza = a
    mniejsza = b
else:
    wieksza = b
    mniejsza = a
while(mniejsza <= wieksza):
    if mniejsza%2 == 1: #skip liczb nieparzystych
        mniejsza +=1
        continue
    print(mniejsza, end=' ')
    mniejsza = mniejsza + 1
