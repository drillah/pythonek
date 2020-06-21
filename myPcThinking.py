import random
import datetime

print("Komputer spróbuje znaleść wybraną przez Ciebie liczbę")

my_number = int(input("Podaj liczbę którą chcesz aby znalazł"))
tries = 0
pc_checker = random.randint(1, 100)

while pc_checker != my_number:
    if pc_checker > my_number:
        print("Za dużo szukam dalej...", pc_checker)
        tries += 1
    else:
        print("Za mało szukam dalej...", pc_checker)
        tries += 1

    pc_checker = random.randint(1, 100)

else:
    print("Udało się ta liczba to", pc_checker, "wykonałem", tries, "prób")

