# Zadanie 14 - List Remove Duplicates
# Treść zadania - Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. Extras:Write two different functions to do this - one using a loop and constructing a list, and another using sets. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# Napisz program (funkcję!), który przyjmuje listę i zwraca nową listę zawierającą wszystkie elementy pierwszej listy minus wszystkie duplikaty. Dodatki: Napisz dwie różne funkcje, aby to zrobić — jedną używającą pętli i konstruującą listę, a drugą używającą zestawów. Wróć i wykonaj Ćwiczenie 5 używając zestawów, a następnie zapisz rozwiązanie dla niego w innej funkcji.

import random

def random_list(num):
    randomlist = []
    for i in range(num):
        i = random.randint(0, 10)
        if i not in randomlist:
            randomlist.append(i)
    return randomlist

def check_duplicate(randomlist1):
    list_without_duplicate = set()
    for i in randomlist1:
        list_without_duplicate.add(i)
    return list_without_duplicate

print(check_duplicate(random_list(5)))
