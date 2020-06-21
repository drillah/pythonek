#bez samogłosek
#Tworzenie nowych łańcuchów z wykorzystaniem pętli for

message = input("Wprowadź komunikat: ")
new_message = ""

#jest to zmienna z samogłoskami które chcemy wykluczyć
VOWELS = "aąeęioóuy"

print()
#pętla idzie przez łańcuch message i jeśli litery nie zostały zadeklarowane w VOWELS zostaną ponownie wypisane
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Został utworzony nowy łańcuch: ", new_message)

print("\nTwój komunikat bez samogłosek to:", new_message)
input("\nAby zakończyć program, naciśnij klawisz ENTER")