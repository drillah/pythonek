# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)
points = 10
guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    if guess != correct and guess!="":
        check = input("Potrzebujesz podpowiedzi?T/N")
        if check.lower() == "t":
            points -= 5
            if correct == "python":
                guess = input("Język w którym napisany jest ten program")
            elif correct == "anagram":
                guess = input("Rodzaj wyrazu jaki zgadujesz")
            elif correct == "łatwy":
                guess = input("Przeciwieństwo do trudny")
            elif correct == "skomplikowany":
                guess = input("Coś zagmatfanego")
            elif correct == "odpowiedź":
                guess = input("Odpowiedź")
            elif correct == "ksylofon":
                guess =input("Sam nie wiem co to :D")
        else:
            guess = input("Twoja odpowiedź: ")
if guess == correct:
    print("Zgadza się! Zgadłeś! Z ilością punktów:", points)

print("\nDziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
