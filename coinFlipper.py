import random
counter = 1
eagle = 0
back = 0
while counter <= 100:
    flip = random.randint(0, 1)
    if flip == 0:
        print("Orzeł")
        eagle += 1
    else:
        print("Reszka")
        back += 1
    counter += 1

print("Wyrzucono", eagle, "orzełków oraz", back, "rzeszek")