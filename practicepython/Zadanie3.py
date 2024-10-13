# Zadanie 3 - List Less Than Ten
# Treść zadania - Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
# Weź listę, powiedzmy na przykład tę: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] i napisz program, który drukuje wszystkie elementy listy, które są mniejsze niż 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

# Zadanie 3 - Extras
# Treść zadania - Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. Write this in one line of Python. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# Zamiast drukować elementy jeden po drugim, utwórz nową listę, która będzie zawierała wszystkie elementy mniejsze niż 5 z tej listy i wydrukuj tę nową listę. Napisz to w jednym wierszu Pythona. Zapytaj użytkownika o liczbę i zwróć listę, która zawiera tylko elementy z oryginalnej listy a, które są mniejsze niż liczba podana przez użytkownika.

newa = []

for i in a:
    if i < 5:
        newa.append(i)

print(newa)

userNum = int(input("Podaj liczbę "))
newa2 = []

for i in a:
    if i < userNum:
        newa2.append(i)

print(newa2)
