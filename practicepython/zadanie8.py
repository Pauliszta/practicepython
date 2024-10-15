# Zadanie 8 - Rock Paper Scissors
#  Treść zadania - Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game). Remember the rules: Rock beats scissors, Scissors beats paper, Paper beats rock

# Stwórz grę dla dwóch graczy „Kamień-Papier-Nożyce”. (Wskazówka: Poproś graczy o zagrania (używając danych wejściowych), porównaj je, wydrukuj wiadomość z gratulacjami dla zwycięzcy i zapytaj, czy gracze chcą rozpocząć nową grę). Zapamiętaj zasady: Kamień pokonuje nożyce, Nożyce pokonują papier, Papier pokonuje kamień

decision = input("Czy chcesz zagrać? Wpisz tak lub nie ").lower()
while decision == "tak":

    player1 = int(input("Gracz nr 1 - Co wybierasz? Do wyboru: 1 - kamień, 2 - papier, 3 - nożyczki "))
    player2 = int(input("Gracz nr 2 - Co wybierasz? Do wyboru: 1 - kamień, 2 - papier, 3 - nożyczki "))


    if player1 == player2:
        print("Remis!")
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
        decision = input("Wygrywa gracz nr 2. Gratulacje! Chcesz zagrać ponownie? Wybierz tak/nie ").lower()
    elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
        decision = input("Wygrywa gracz nr 1. Gratulacje! Chcesz zagrać ponownie? Wybierz tak/nie").lower()
else:
    print("Papa!")