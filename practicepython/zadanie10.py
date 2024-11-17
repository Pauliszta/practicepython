# Zadanie 10 - List Overlap Comprehensions 
# Treść zadania - This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Ćwiczenie w tym tygodniu będzie powrotem do starego ćwiczenia (patrz Ćwiczenie 5), z tym wyjątkiem, że wymagać będzie rozwiązania w inny sposób.
# Weź dwie listy, powiedzmy na przykład te dwie:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# i napisz program, który zwraca listę zawierającą tylko elementy wspólne dla list (bez duplikatów). Upewnij się, że Twój program działa na dwóch listach o różnych rozmiarach.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set([i for i in a if i in b]))