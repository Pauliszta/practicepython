# Zadanie 15 - Reverse Word Order
# Treść zadania - Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# Napisz program (używając funkcji!), który prosi użytkownika o długi ciąg zawierający wiele słów. Wypisz użytkownikowi ten sam ciąg, ale ze słowami w odwrotnej kolejności.

user_text = input("powiedz mi coś fajnego \n")

def reverse_word(user_text):
    words_list = user_text.split()
    reverse_list = words_list[::-1]
    new_text = " ".join(reverse_list)
    return new_text
        

print(reverse_word(user_text))

