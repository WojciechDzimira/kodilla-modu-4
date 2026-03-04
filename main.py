def words_input():
    '''
        Funkcja pobiera słowo od użytkowniak, sprawdza czy sa tylko litery
        oraz zmniejsza litery 
    '''
    while True:
        word = input("podaj słowo: ").lower()
        if word.isalpha():
            return word
        else:
            print("Twoje słowo zawiera liczby lub znaki specjalne, wprowadz je ponownie")

def palindrome(word):
    """
    Funkcja sprawdza w pętli czy pierwszy i ostatni element słowa jest taki sam
    jeśli tak zwraca True, jeśli nie zwraca False
    """
    word_length = int(len(word)/2)
    for i in range(word_length):
        if word[i] == word[i*-1-1]:
            pass
        else:
            return False
    return True

word = words_input()
if palindrome(word):
    print("Twoje słowo jest palindromem")
else:
    print("Twoje słowo nie jest palindromem")