# instrukcja - przykład z książki
# poznawanie funkcji ktore mogę sam stworzyć

# definiowanie funkcji
def instructions():
    """Wyświetl instrukcję gry."""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest gra
        'Kółko i Krzyżyk'. Będzie to ostateczna rozgrywka między Twoim ludzkim
        mózgiem a moim krzemowym procesorem.
        
        Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8,
        liczba ta odpowiada pzoycji a planszy zgodnie z poniższym schematem:
        
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
                    
        Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie. \n
        """)


# main

# print("Oto instrukcja do gry 'Kółko i Krzyżyk':")
# instructions()
# print("Ponownie...")
# instructions()

# input("\nAby zakończyć naciśnij ENTER...")

# input output instruction

def display(message):
    print(message)


def give_me_five():
    five = 5
    return five


# def ask_yes_no(question):
#     response = None
#     while response not in ("t", "n"):
#         response = input(question).lower()
#     return response

# main
# display("To jest wiadomość dla ciebie\n")
# number = give_me_five()
# print("Sprawdzamy co daje funkcja give_me_five()", number)
#
# anwser = ask_yes_no("\nProszę wprowadzić 't' lub 'n': ")
# print("Dziękuje za wprowadzenie:", anwser)
#
# print("Aby zakonczyc nacisnij Enter...")
#
#
# def question(anwser):
#     password = None
#     while password not in ("magic", "password", "admin"):
#         password = input(anwser)
#     return password
#
#
# anwser = question("\mProszę wprowadzić hasło: ")
# print("To jest poprawne hasło", anwser)

# Birthday wishes
def birthday1(name, age):
    print("Szczęśliwych urodzin,", name, "!", " Masz już", age, "lat.\n")

def birthday2(name = "Janusz", age = 5):
    if name == "Darek":
        print("Witaj", name, "wiedziałem, że mimo wieku", age, "lat dalej będziesz drążył")
    else:
        print("Szczęśliwych urodzin,", name, "!", " Masz już", age, "lat.\n")

birthday1("Janusz", 5)
birthday1(5, "Janusz")
birthday1(name = "Janusz", age = 5)
birthday1(age = 5, name = "Janusz")

birthday2()
birthday2(name = "Katarzyna")
birthday2(age = "12")
birthday2(name = "Katarzyna", age = 12)
birthday2("Katarzyna", 12)

name = input("Podaj imię: ")
age = int(input("Podaj wiek: "))

birthday2(name, age)

input("Aby zakończyć program naciśnij ENTER...")
