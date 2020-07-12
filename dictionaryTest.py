#Tworzenie słownika

geek = {"404": "ingorant; od używango w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Keybord Plaque": "zanieczyszczenia zgromadze w klawiaturze komputera",
        "Link Rot" : "proces, w wyniku którego linki do stron WWW stają się nieaktualne",
        "Uninstalled" : "zwolniony z pracy"
        }

choice = None

while choice !=  "0":
        print(
                """
                Tranlator slangu internetowego
                
                0 - zakończ
                1 - znajdź termin
                2 - dodaj nowy termin
                3 - zmień definicję terminu
                4 - usuń termin
                """
        )
        choice = input("Wybierasz: ")
        print()

        if choice == "0":
                print("Żegraj.")
        elif choice == "1":
                term = input("Jaki termin mam przetłumaczyć?: ")
                if term in geek:
                        definition = geek[term]
                        print("\n", term, "oznacza", definition)
                else:
                        print("\nNiestety nie znam terminu", term)
        elif choice == "2":
                term = input("Jaki termin mam dodać?: ")
                if term not in geek:
                        definition = input("\nPodaj definicję tego terminu: ")
                        geek[term] = definition
                        print("\nTermin", term, "został dodany.")
                else:
                        print("\nTen termin ju./ż istnieje. Spróbuj zmienić jego definicję.")
        elif choice == "3":
                term = input("Jaki termin mam przedefiniować?: ")
                if term in geek:
                        definition = input("Jaka jest nowa definicja?: ")
                        geek[term] = definition
                        print("\nTermin", term, "został przedefiniowany.")
                else:
                        print("Ten termin nie istnieje! Spróbuj go dodać.")
        elif choice == "4":
                term = input("Który termin chcesz usunąć?")
                if term in geek:
                        del geek[term]
                        print("\nOk, termin został usunięty")
                else:
                        print("\nNie mogę tego zrobić. Termin", term, "nie ma w słowniku")
        elif choice == "5":
                print("Trafiłeś do tajnego menu w którym możesz zobaczyć wszystkie elementy słownika")
                print(geek)


