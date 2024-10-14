# Zadanie 6 - String Lists
# Treść zadania - Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
# Zapytaj użytkownika o ciąg znaków i wydrukuj, czy ten ciąg znaków jest palindromem, czy nie. (Palindrom to ciąg znaków, który czytany od początku do końca brzmi tak samo.)

text = input("Podaj słowo: ").lower()

textlist = []
textreverse = []

for i in range(0, len(text)):
    textlist.append(text[i])

for i in range(1, len(text)+1):
    textreverse.append(text[-i])

if textlist == textreverse:
    print("To jest palindrom!")
else:
    print("To nie jest palindrom!")
