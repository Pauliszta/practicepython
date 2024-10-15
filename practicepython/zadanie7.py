# Zadanie 7 - List Comprehensions
# Treść zadania - Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# Załóżmy, że dam ci listę zapisaną w zmiennej: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Napisz jedną linię w Pythonie, która bierze tę listę a i tworzy nową listę, która zawiera tylko parzyste elementy tej listy.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newa = []

for i in a:
    if int(i) % 2 == 0:
        newa.append(i)

print(newa)

b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

newb = [i for i in b if int(i) % 2 == 0]

print(newb)
