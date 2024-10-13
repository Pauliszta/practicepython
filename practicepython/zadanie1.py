# Rozwiązania zadań z strony practicepython.org

# Zadanie 1 - Character Input 
# Treść zadania - Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("Cześć! Proszę podaj swoje imię ")
today = datetime.date.today().year

age = int(input("Witaj " + name + "! Ile masz lat? "))
year = today + (100 - int(age))
message = "Oo masz " + str(age) + " lat! W " + str(year) + " będziesz mieć 100 lat."
print(message)

# Zadanie 1 - Extras
# Treść zadania - Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

howMany = input("Ile razy mam powtórzyć tą wiadomość? ")

for i in range(int(howMany)):
    print(message)
