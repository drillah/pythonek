monkey_d_luffy = ["usopp", "nami", "zoro", "chopper", "franky", "brook", "jinbei"]
fruit_user = monkey_d_luffy
pirate_king =  monkey_d_luffy

#niezależnie od tego jak nazwę znienna, jesli przypiszę do niej inna zmienna zawsze wyjdzie przypisana zmienna :S
print("print(pirate_king)")
print(pirate_king)
print("\nprint(fruit_user)")
print(fruit_user)

#zmiana wartości w zmiennej do której "podlinkowana" inna zmienna zmienia wartość oryginalnej zmiennej
fruit_user[2] = "rodoan zoro"

print(fruit_user)
print(monkey_d_luffy)
#w tym momencie utworzymy kopie zmiennej monkey_d_luffy która będzie inna niż pozostałe zmienne gdyż będzie osobną listą
fruit_user = monkey_d_luffy[:]
fruit_user[2] = "mihawk"

print("Monkey")
print(monkey_d_luffy)
print("Fruit")
print(fruit_user)
