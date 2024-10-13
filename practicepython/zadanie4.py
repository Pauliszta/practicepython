# Zadanie 4 - Divisors
# Treść zadania - Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# Utwórz program, który prosi użytkownika o podanie liczby, a następnie drukuje listę wszystkich dzielników tej liczby. (Jeśli nie wiesz, czym jest dzielnik, jest to liczba, która dzieli się równo przez inną liczbę. Na przykład 13 jest dzielnikiem 26, ponieważ 26/13 nie ma reszty.)

num = int(input("Podaj proszę liczbę "))
list = []

for i in range(num):
    if i > 0 and num % i == 0:
        list.append(i)
list.append(num)

print(list)