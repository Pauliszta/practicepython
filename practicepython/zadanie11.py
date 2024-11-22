# Zadanie 11 - Check Primality Functions
# Treść zadania - Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
# Zapytaj użytkownika o liczbę i określ, czy jest ona pierwsza, czy nie. (Dla tych, którzy zapomnieli, liczba pierwsza to liczba, która nie ma dzielników.). Możesz (i powinieneś!) użyć swojej odpowiedzi na Ćwiczenie 4, aby sobie pomóc.

def check_primality(num):
    list = []

    for i in range(num):
        if i > 0 and num % i == 0:
            list.append(i)
    list.append(num)

    if len(list) > 2:
        txt = f"Twoja liczba - {num} nie jest liczba pierwsza"
    else: 
        txt = f"Twoja liczba - {num} jest liczba pierwsza"

    return txt

num = int(input("Podaj proszę liczbę "))
print(check_primality(num))
