#Inwentarz bohatera
#Demonstacja tworzenia krotek

#utwórz pustą krotkę która ma wartość False
inventory = ()

#potraktowanie krotki jako warunku czyli jeśli jest pusty wieć False i False daje True :)
if not inventory:
    print("Nie posiadasz niczego")

input("\nAby kontynuować misję, naciśnij klawisz ENTER.")

#tworzymy krotkę zawierającą pewne elementy
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napój uzdrawiający")

#wyświetla krotkę
print("Wykaz twojego inwentarza:")
print(inventory)

#wyświetla każdy element krotki
print("\nElementy twojego inwentarza: ")

#wychodzi na to, że jeśli chce przejść przez elementy krotki wystarczy zainicjować zmienna item dla krotki inventory
#po czym wyświetlić wczesniej przypisaną zmienną "print(item)"
for item in inventory:
    print(item)

print("\nAby zakończyć program, naciśnij ENTER.")