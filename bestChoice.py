#najlepszy wynik

scores = []
choice = None

while choice != "0":
    print(
        """
        Najlepsze wyniki
        
        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        3 - usuń wynik
        4 - posortuj wyniki
        """
    )

    choice = input("Wybierasz: ")
    print()
    if choice == "0":
        print("Do widzenia.")
    elif choice == "1":
        print("Najlepsze wyniki:")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(input("Jaki wynik uzyskałeś?: "))
        scores.append(score)