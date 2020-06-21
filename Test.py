#Licznik bardziej zaawansowany
#
# start = int(input("Wprowadź liczbę początkową: "))
# finish = int(input("\nWprowadź liczbę końcową: ")) + 1
# between = int(input("\nWprowadź co ile ma liczyć licznik: "))
#
# for i in range(start, finish, between):
#     print(i)

#pisanie od tyłu
word = input("Wprowadź słowo: ")
word_count = len(word)

for i in range(word_count, 0, -1):
    print(word[i - 1])
input("Aby zakończyć wciśnij ENTER.")