import random

print("\tWitaj w grze, 'Jaka to liczba'!")
print("\nMam na mysli pewną liczbę z zakresu od 0 do 100")
print("Sprobój odgadnąc o jakiej liczbie mysle!\n")

the_number = random.randint(0, 100)
guess = int(input("Ta liczba to: "))
tries = 5
while tries != 0:
    if guess > the_number:
        print("Za dużo!")
        tries -= 1

    else:
        print("Za mało!")
        tries -= 1

    guess = int(input("Ta liczba to:"))
    print("Pozostało Ci:", tries, "prób")


