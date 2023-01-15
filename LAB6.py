'''
def print_imie_wiek (imie, wiek=20):
    print("imię: ",imie, "wiek: ",wiek)
print_imie_wiek("Kacper", 20)
print_imie_wiek("Michał",38)
print_imie_wiek(wiek=65,imie="Tomek")
print_imie_wiek("Antek")

def oblicz(x,y):
   return x+y,x-y
print(oblicz(1,2))
krotka=oblicz(2,4)
print(krotka[0],krotka[1])
l1,l2=oblicz(3.5,0.6)
print(l1,l2)

def find(lista, wartosc):
    new_list = []
    for i in range(len(lista)):
        if lista[i] == wartosc:
            new_list.append(i)
    return new_list
l1 = [1, 2, 1, 1, 3, 5]
wartosc_szukana = 1
lista_indeksow = find(l1, wartosc_szukana)
print(lista_indeksow)

def sum_of_values(dict1):
    wynik = 0
    for i in dict1.values():
        wynik += i
    return wynik
dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'data1':15, 'data2':-2, 'data3':1, 'data4':87}
print(sum_of_values(dict1))
print(sum_of_values(dict2))

def potęga(lista1, lista2):
    if len(lista1) != len(lista2):
        return "Listy muszą mieć taką samą długość"
    L3 = []
    for i in range(len(lista1)):
        L3.append(lista1[i] ** lista2[i])
    return L3

wynik=potęga([2,4,3,7],[2,4,6,1])
print(wynik)
'''

def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    if b==0:
        return "Wynik równy 0"
    else:
        return a/b
kalkulator={'+': dodawanie,'-': odejmowanie,'*': mnożenie,'/': dzielenie}

d='+'
l1=3
l2=5
print=(kalkulator[d](l1,l2))