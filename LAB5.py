# słowmiki
# ZAD1
'''
lista_values=[10,20,30]
lista_keys=['dziesięć','dwadzieścia','trzydzieści']

D1={}
slownik =dict(zip(lista_keys, lista_values))
print(slownik)

#1.1
for x in range(len(lista_keys)):
    D1(lista_keys[i]) = lista_values[i]

print(D1)'''
'''D1 = lista_keys[i]:lista_values[i] for x in range(len(lista_keys))
    print(D1)
#1.2
D2 = dict(trzydzieści = 30, czterdzieści = 40, pięćdziesiąt = 50)

print(D2)

#1.3
D3 = D2.copy()
D3.update(D2)
print(D3)'''

#2
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}


for k in sample_dict.keys():
    print(k, sample_dict.items())