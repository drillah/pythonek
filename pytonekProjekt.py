waga = int(input("Podaj swoją wagę"))
wzrost = int(input("Podaj swój wzrost"))

bmi = round(waga / ((wzrost * wzrost) / 10000))

if bmi < 19:
    print("Twoje BMI to", bmi, "chudzina z Ciebie")
elif 19 < bmi < 30:
    print("Twoje BMI to", bmi, "masz prawidłowe BMI")
else: print("Twoje BMI to", bmi, "ale się spasłeś")