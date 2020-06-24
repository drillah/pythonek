inventory = []
choice = None

while choice != "0":
    print("""
    Twój inwentarz:

    0 - zamknij inwentarz
    1 - zobacz inventarz
    2 - dodaj do inwentarza
    """)

    choice = input("Wybierasz: ")
    print()

    if choice == "0":
        print("Zamykam inwentarz.")
    elif choice == "1":
        for item in inventory:
            print(item)
    elif choice == "2":
        item = input("Jaki przedmiot chcesz dodać")
        inventory.append(item)
    else:
        print("Niestety,", choice, "nie jest prawidłowym wyborem")

#musze jeszcze poćwiczyć te listy i tworzenie prostych menu z możliwością dodawania