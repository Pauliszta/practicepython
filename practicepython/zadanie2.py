# Zadanie 2 - Odd Or Even
# Treść zadania - Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Zapytaj użytkownika o liczbę. W zależności od tego, czy liczba jest parzysta czy nieparzysta, wydrukuj odpowiednią wiadomość dla użytkownika.

number = int(input("Cześć! Podaj liczbę "))

if number % 2 == 0:
    if number % 4 == 0:
        print("Twoja liczba jest parzysta i podzielna przez 4")
    else:
        print("Twoja liczba jest parzysta!")
else: 
    print("Twoja liczba jest nieparzysta!")

# Zadanie 2 - Extras
# Treść zadania - If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# Jeśli liczba jest wielokrotnością 4, wydrukuj inną wiadomość. Zapytaj użytkownika o dwie liczby: jedną liczbę do sprawdzenia (nazwij ją num) i jedną liczbę do podzielenia (check). Jeśli check dzieli równo przez num, powiedz to użytkownikowi. Jeśli nie, wydrukuj inną odpowiednią wiadomość.

num = int(input("Podaj pierwszą liczbę "))
check = int(input("Podaj drugą liczbę "))

if num % check == 0:
    print("Liczba " + str(num) + " jest podzielna przez " + str(check))
else: 
    print("Liczba " + str(num) + " nie jest podzielna przez " + str(check))
