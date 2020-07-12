#Próba stworzenia własnej listy rzeczy do zrobienia
import time

toDo = {}

choice = None

while choice != "0":
    print("""
        Witam, program do przechowywania reczy do zrobienia
        Wybierz jedną z opcji:
        0 - Zakończ
        1 - Dodaj nowe zadanie do zrobienia
        2 - Usuń zadanie
        3 - Wyświetl wszystkie zadania

    """)
    print(time.strftime("%A, %d %b %Y, %H:%M:%S"))
    choice = input("Wybierasz?: ")
    print()
    if choice == "0":
        print("Do zobaczenia")
    elif choice == "1":
        term = input("Jak ma się nazywać zadanie? ")
        if term not in toDo:
            task = input("Na czym ma polegać zadaie?")
            toDo[term] = task
            print("Zadanie", term, "zostało dodane.")
    elif choice == "2":
        term = input("Podaj nazwę zadania do usunięcia? ")
        if term in toDo:
            del toDo[term]
            print("Ok, usunięte")
        else:
            print("Nazwa nie istnieje! Podaj inna nazwę")
    elif choice == "3":
        print("Wszystkie zadania")
        print(toDo)
