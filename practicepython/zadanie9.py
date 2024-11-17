# Zadanie 9 - Guessing Game One
# Treść zadania - Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# Wygeneruj losową liczbę od 1 do 9 (w tym 1 i 9). Poproś użytkownika o odgadnięcie liczby, a następnie powiedz mu, czy odgadł za nisko, za wysoko, czy dokładnie.
# Dodatki:
# Kontynuuj grę, aż użytkownik wpisze „exit”
# Śledź, ile zgadnięć wykonał użytkownik, a po zakończeniu gry wydrukuj to.

import random

player_solution = input("Podaj liczbę od 1 do 9 \n")

random_num = random.randint(1, 9)
status = True
proba = 1


while status:
    if player_solution == "exit":
        print("To koniec! Papa")
        status = False
    elif int(player_solution) > random_num:
        print("Twój wynik jest za wysoki.")
        print(f"Spróbuj ponownie. \n To Twoja {proba} próba. ")
        player_solution = input("Podaj nowa liczbę \n")
        proba = proba + 1
    elif int(player_solution) < random_num:
        print("Twój wynik jest za niski.")
        print(f"Spróbuj ponownie. \n To Twoja {proba} próba. ")
        player_solution = input("Podaj nowa liczbę \n")
        proba = proba + 1
    else:
        print(f"Gratulacje! \n To Twoja {proba} próba")
        status = False





