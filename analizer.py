#Analizator komunikatów

message = input("Wprowadź komunikat: ")

print("\nDługość twojego komunikatu wynosi", len(message))

print("\nNajczęściej używana litera w języku polskim, 'a' ,")
if "darek" in message.lower():
    print("wystąpiła w Twoim komunikacie.")
else:
    print("Nie wystąpiła w twoim komunikacie.")

print("Aby zakończyć naciśnij ENTER...")