# Zadanie 13 - Fibonacci
# Treść zadania - rite a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
# Napisz program, który pyta użytkownika, ile liczb Fibonacciego wygenerować, a następnie je generuje. Skorzystaj z tej okazji, aby pomyśleć o tym, jak możesz użyć funkcji. Upewnij się, że prosisz użytkownika o podanie liczby liczb w sekwencji do wygenerowania. (Wskazówka: ciąg Fibonacciego to sekwencja liczb, w której następna liczba w sekwencji jest sumą dwóch poprzednich liczb w sekwencji. Sekwencja wygląda tak: 1, 1, 2, 3, 5, 8, 13, …)

user_num = int(input("Podaj liczbę, do ktorej wygenerować ciąg Fibonacciego \n"))

def fibonacci(num):
    list = [1, 1]
    
    if num == 0:
        list = [0]
    elif num == 2:
        list = [0, 1]
    else:
        for i in range(num-2):
            list.append(list[i] + list[i+1])

    return list


print(fibonacci(user_num))

