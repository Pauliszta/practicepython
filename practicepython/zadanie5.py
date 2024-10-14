# Zadanie 5 - List Overlap
# Treść zadania - Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Weź dwie listy, powiedzmy na przykład te dwie: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] i napisz program, który zwraca listę zawierającą tylko elementy wspólne dla list (bez duplikatów). Upewnij się, że Twój program działa na dwóch listach o różnych rozmiarach.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = []


for i in a:
    if i in b:
        if i not in list:
            list.append(i)

print(list)

# Zadanie 5 - Extras
# Treść zadania - Randomly generate two lists to test this. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon). 
# Losowo wygeneruj dwie listy, aby to przetestować. Napisz to w jednym wierszu Pythona (nie martw się, jeśli nie możesz tego rozgryźć na tym etapie — wkrótce do tego dojdziemy).

import random

randomlist1 = []
for i in range(12):
    i = random.randint(0, 100)
    if i not in randomlist1:
        randomlist1.append(i)
print(randomlist1)

randomlist2 = []
for i in range(12):
    i = random.randint(0, 100)
    if i not in randomlist2:
        randomlist2.append(i)
print(randomlist2)

list2 = []

for i in randomlist1:
    if i in randomlist2:
        list2.append(i)

print(list2)
