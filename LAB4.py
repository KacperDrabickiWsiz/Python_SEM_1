#ZADANIE 1
'''lista_zakupow=['produkt1','produkt2','produkt3','produkt4','produkt5']
print(lista_zakupow)
print(lista_zakupow[0]+","+lista_zakupow[1])
lista_zakupow[2]='mleko'
print(lista_zakupow)
print(lista_zakupow[-2]+","+lista_zakupow[-1]) #-2 i -1 to ostatni i przedostati element listy'''

#ZADANIE 2
import random
x=int(input('Podaj liczbe1:'))
lista1 = []
for n in range(x):
    los1 = random.randint(1, 10)
    lista1.append(los1)
print(lista1)

x2=int(input('Podaj liczbe2:'))
lista2 = []
for n2 in range(x2):
    los2 = random.randint(5, 15)
    lista2.append(los2)
print(lista2)

x3=int(input('Podaj szukna'))
if x3 in lista1:
    print('liczba wystepuje w lista 1')
elif x3 in lista2:
    print('liczba wystepuje w lista 2')
else:
    print('liczba nie wystepuej')

zesetaw_1_2= lista1 + lista2

zesetaw_1_2.sort()

print(zesetaw_1_2)