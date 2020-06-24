scores = []

choice = None

while choice != "0":
    print(
        """
        Najlepszy wynik 2.0
        
        0 - zakończ
        1 - wyświetl wyniki
        2 - dodaj wynik
        """
    )

    choice = input("Wybierasz: ")
    print()

    #zakończ
    if choice == "0":
        print("Do zobaczenia.")
    elif choice == "1":
        print("najlepszy wynik\n")
        print("GRACZ\tWYNIK")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == "2":
        name = input("Podaj nazwę gracza: ")
        score = int(input("Jaki wynik gracz uzyskał?: "))
        entry =(score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Niestety,", choice, "nie jest prawidłowym wyborem.")

