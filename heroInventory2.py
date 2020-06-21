#Druga wersja Inwentarza bohatera z zastosowaniem krotek

inventory = ("miecz",
             "tarcza",
             "zbroja",
             "buty",
             "eliksir uzdrawiający")

print("Elementy twojego inwentarza: ")
for item in inventory:
    print(item)
#len w krotkach liczy każdy poszczególny ciąg znaków jako jeden przedmiot
print("Posiadasz", len(inventory), "przedmiotów w inwentarzu.")

if "zbroja" or "tarcza" and "miecz" in inventory:
    print("Jesteś przygotowany na ostatniego BOSSA :)")

if not "Święty Grall" in inventory:
    print("Nie możesz się wskrzesić!")

#wyświetlanie wycinek
#start = int(input("Wprowadź początek wycinka krotki"))
#finish = int(input("Wprowadź koniec wycinka krotki"))
#print("inventory[", start, ":", finish, "] to", end=" ")
#print(inventory[start:finish])

chest = ("diamenty", "złoto", "miecz nieskończoności")
print("Znajdujesz skrzynię która zawiera: ")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Aktualnie w twoim inwentarzu znajduje się:")
for item in inventory:
    print("-", item)

input("Aby zakończyć program, naciśnij ENTER.")