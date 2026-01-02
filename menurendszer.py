print("Üdvözöljük az XY interaktiv étlapon.") #<- Majd adhatunk neki valami nevet, most csak azon voltam, hogy legyen egy üdvözlő szöveg
print("")

def főmenü():

    print("[1] Étlap megtekintése")
    print("[2] Ételek kiválasztás")
    print("[3] Tápérték kalkuláció")
    print("[4] Ár kiszámítása")
    print("[5] Meglepetés menű")
    print("[6] Kiszállítási idő")
    print("[9] Étlap szerkesztése [Admin funkció]")
    print("[0] Kilépés a programból")
    print("")

főmenü()  #<- Én is számok alapján gondoltam a navigálást. Nyugodtan lehet a menűpontokon változtatni, hozzáadni, elvenni, stb.

navigáció = int(input("Kérem válaszon a fenti lehetőségek közül [0-9]:"))

while navigáció != 0:
    if navigáció == 1:
        print("1")
    elif navigáció == 2:
        print("2") #<- Egyenlőre csak print, így legalább látjuk, hogy a menűpontra kiírat valamit
    elif navigáció == 3:
        print("3")
    elif navigáció == 4:
        print("4")
    elif navigáció == 5:
        print("5")
    elif navigáció == 6:
        print("6")
    elif navigáció == 9: #<- Itt a szerkesztés menűponthoz hozzáadtam egy jelszó bekérést. Háromszor lehet próbálkozni utána visszavág a főmenübe. A jelszó: 1234

        szamlaló = 3

        while szamlaló > 0:

            jelszó = int(input("Kérem, adja meg az admin jogosultsághoz a jelszavát: "))

            if jelszó != 1234:
                print(f"Helytelen jelszó! {szamlaló-1} próbálkozása van.")
                print("")

                szamlaló = szamlaló - 1

            else: # késöbb akár ezt is be lehet def-elni, mint almenü
                print("[1] Étlaphoz új elem hozzáadása")
                print("[2] Étlap elemeinek modosítása")
                print("[3] Étlap elemeinek törlése")
                print("[0] Visszalépés a főmenübe")
                print("")

                szamlaló = 0

                navigáció2 = int(input("Kérem válaszon a fenti lehetőségek közül [0-9]:"))

                while navigáció2 != 0:
                    if navigáció2 == 1:
                        print("1")
                    elif navigáció2 == 2:
                        print("2")
                    elif navigáció2 == 3:
                        print("3")
                    else:
                        print("Nem létező opció. Kérem válasszon másikat!")

                    navigáció2 = int(input("Kérem válaszon a fenti lehetőségek közül [0-9]:"))
           
        print("Visszatérés a Főmenübe")
        print("")

        főmenü()

    elif navigáció == 0:
        print("0")
    else:
        print("Nem létező opció. Kérem válasszon másikat!")

    navigáció = int(input("Kérem válaszon a fenti lehetőségek közül [0-9]:"))

print("Program vége")
# Így ennyi! Rermélem átlátható, meg használható :)