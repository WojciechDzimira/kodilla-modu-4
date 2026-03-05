import sys
import logging
logging.basicConfig(level=logging.DEBUG)


def number_input(text):
    """
    Funkcja wprowadzenia liczbę przez uzytkownika, sprawdza czy 
    uzytkownik faktycznie wprowadził liczbę
    """
    while True:
        try:
            number = float(input(f"{text}"))
            return number
        except ValueError:
            print("to nie liczba, wprowadz jeszcze raz.")
def int_input(text):
    """
    Funkcja prosi uzytkownika o liczbę całkowitą i sprawdza czy 
    uzytkownik faktycznie wprowadził liczbę calkowita
    """
    while True:
        try:
            number = int(input(f"{text}"))
            if number > 0:
                return number
            else:
                print("to nie jest dodatnia liczba całkowita, wprowadz jeszcze raz.")
        except ValueError:
            print("to nie jest dodatnia liczba całkowita, wprowadz jeszcze raz.")

def operation_components():
    """
    Funkcja pobiera 2 liczby i zwraca jew
    """
    number_1 = number_input("Podaj składnik 1. ")
    number_2 = number_input("Podaj składnik 2. ")
    return number_1, number_2

def operation_choosing():
    """"
    Funkcja wyboru operacji przez użytkownia
    sprawdza czy liczba wprowadzona odpowida dostępnym operacjom
    """
    while True:
        operation = int_input("Wprowadz liczbę: ")
        if operation  in {1, 2, 3, 4}:
            return operation
        else:
            print("Błedna liczba, wpisz jeszcze raz")   
def addition():
    """
    funkcja wprowadza tyle liczb ile wpisze uzytkownik, sumuje je i wyswietla wynik
    """
    
    add_number = int_input("ile liczb chcesz dodać? ")
    numbers_list = []
    for i in range(add_number):
        number = number_input(f"Podaj składnik {i+1}. ")
        numbers_list.append(number)
    list_sum = sum(numbers_list)
    logging.debug(f"dodaje elementy listy {numbers_list} ")
    print(f"wynik to: {list_sum}")
        
def subtraction():
    """
    funkcja wprowadza 2 liczby odejmuje je i wyświetla wynik
    """
    
    number_1, number_2 = operation_components()
    logging.debug(f"odejmuję {number_1} i {number_2}")
    print(f"wynik to: {number_1 - number_2}")

def multiplication():
    """
    funkcja wprowadza 2 liczby mnoży je i wyświetla wynik
    """
    
    multip_number = int_input("ile liczb chcesz pomnożyć? ")
    numbers_list = []
    for i in range(multip_number):
        number = number_input(f"Podaj składnik {i+1}. ")
        numbers_list.append(number)
    result = 1
    for number in numbers_list:
        result = result * number

    logging.debug(f"mnożę elementy listy {numbers_list} ")
    print(f"wynik to: {result}")
        

def division():
    """
    funkcja wprowadza 2 liczby, sprawdza czy nie ma 0, dzieli je i wyświetla wynik
    """
    number_1, number_2 = operation_components()
    if  number_2 == 0:
        print("pamiętaj cholero nie dziel przez 0 :)")
    else:
        logging.debug(f"dzielę {number_1} i {number_2}")
        print(f"wynik to: {number_1 / number_2}")




if __name__ == "__main__":
    while True:
        print(
                "\n"
                "Podaj działanie, posługując się odpowiednią liczbą::\n"
                "  1  Dodawanie\n"
                "  2  Odejmowanie\n"
                "  3  Mnożenie\n"
                "  4  Dzielenie\n"
                )

        operation = operation_choosing()
        if operation == 1:
            addition()  
        elif operation == 2:
            subtraction()
        elif operation == 3:
            multiplication()
        elif operation == 4:
            division()
        
        once_again = input("chcesz wykonać następne działanie? wpisz T, chcesz zakończyć wpisz cokolwiek ")
        if once_again.lower() != "t":
            break