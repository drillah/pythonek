# Zadanie z książki
print("\tProsty system logowania")

security = 0
username = ""
while not username:
    username = input("Użytkownik: ")
password = ""
while not password:
    password = input("Hasło: ")

if username == "M.Dawson" and password == "sekret":
    print("Czesc, Mike!")
    security = 5
elif username == "S.Meier" and password =="cywilizacja":
    print("Hey, Sid!")
    security = 3
elif username == "S.Miyamoto" and password =="mariobros":
    print ("Witaj, Shigeru")
    security = 5
elif username == "gosc" or password =="gosc":
    print("Witaj, gosciu!")
    security = 1
else:
    print("Nieudana próba logowania. Nie jestes taki wyjątkowy")

input("\n\nAby zakończyć wcisnij ENTER...")