# Zadanie 12 - List Ends
# Treść zadania - Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
# Napisz program, który przyjmuje listę liczb (na przykład a = [5, 10, 15, 20, 25]) i tworzy nową listę zawierającą tylko pierwszy i ostatni element podanej listy. W celach ćwiczeniowych napisz ten kod wewnątrz funkcji.


def first_last_num(list):
    newlist = []
    last = len(list)
    newlist.append(list[0])
    newlist.append(list[-1])

    return newlist

print(first_last_num([5, 10, 15, 20, 25]))