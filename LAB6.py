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
'''
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