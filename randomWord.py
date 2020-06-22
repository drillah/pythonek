import random

print("Witam w programie jakie to słowo. Spróbuj odgadnąc jakie jest słowo zgadując litery")
WORDS = ("zima", "wiatr", "orzech", "parawan", "towar")

word = random.choice(WORDS)
word_counter = len(word)
count = 5
print("Twoje słow składa się z", word_counter, "liter")
info = "Podaj odpowiedź bądź litere aby sprawdzić czy znajduje się w słowie: "
check = input(info)
while check != word:
    if check == word:
        print("Gratulacje udało się!")
    elif count == 0:
        print("Niestety nie udało Ci się odgadnąć w wyznaczonej ilości prób")
        break
    elif len(check) == 1:
        for letter in check:
            if letter.lower() in word:
                print("Litera", letter, "znajduje się w słowie")
                count -= 1
                print("Pozostało", count + 1)
                check = input(info)
            else:
                print("Nie ma takiej litery w słowie")
                count -= 1
                print("Pozostało", count + 1)
                check = input(info)
    else:
        print("To nie ten wyraz, próbuj dalej")
        count -= 1
        print("Pozostało", count + 1)
        check = input(info)
else: print("Gratulacje udało się wygrać")
input("Aby zakończyć naciśnij Enter.")