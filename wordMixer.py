#Program bedzię wybierał jeden z zdefiniowanych wyrazów
import random

#stała
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#wybieranie losowego słowa z sekwencji WORDS
word = random.choice(WORDS)
correct = word

jumble = ""

#while word