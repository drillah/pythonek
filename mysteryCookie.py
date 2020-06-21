import random

print("Witaj w programie 'Magiczne ciasteczko!\n")
print("W ciasteczku znajdowała się przepowiednia, \n")
input("A brzmi ona...")

magic_queue = random.randint(1, 5)

if magic_queue == 1:
    print("Spotkasz wybrankę swojego życia!")
elif magic_queue == 2:
    print("Jesteś skazany na sukces")
elif magic_queue == 3:
    print("Zapomnisz o czymś")
elif magic_queue == 4:
    print("Pieniądze polecą z nieba")
else:
    print("Napotkasz trudności!")