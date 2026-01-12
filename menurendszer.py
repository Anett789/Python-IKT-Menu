import etlap_beolvasasa
import etlap_szerkesztese


rendelés = []
meglepetés = []
vég = []



#innen futatható a program!

print("Üdvözöljük az XY interaktiv étlapon.") #<- Majd adhatunk neki valami nevet, most csak azon voltam, hogy legyen egy üdvözlő szöveg
print("")

def almenű9(): #<- bedefeltem, így nem foglal annyi helyet.

    print("")
    print("[1] Étlaphoz új elem hozzáadása")
    print("[2] Étlap elemeinek módosítása")
    print("[3] Étlap elemeinek törlése")
    print("[9] Változtatások mentése")
    print("[0] Visszalépés a főmenübe")

def főmenü():

    print("[1] Étlap megtekintése")
    print("[2] Ételek kiválasztás")
    print("[3] Tápérték kalkuláció")
    print("[4] Ár kiszámítása")
    print("[5] Meglepetés menű")
    print("[6] Rendelés véglegesítése")
    print("[9] Étlap szerkesztése [Admin funkció]")
    print("[0] Kilépés a programból")
    print("")

főmenü()  #<- Én is számok alapján gondoltam a navigálást. Nyugodtan lehet a menűpontokon változtatni, hozzáadni, elvenni, stb.

navigáció = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))

while navigáció != 0:
    if navigáció == 1:
        print("Étlap megtekintése:")
        etlap_beolvasasa.étlapbeolvasása() #<- étlap beimportálva
        print("")
        navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
        while navigáció2 != 0:
            print("Nem létező opció. Kérem, válasszon másikat!")
            print("")
            navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
        print("")
        főmenü()
    elif navigáció == 2:
        etlap_szerkesztese.ételek_kiválasztása()          
        etlap_szerkesztese.kiválasztott_ételek_törlése()     #kiíratom újra a főmenüt, hogy ne kelljen vissza görgetni.
        főmenü()
    elif navigáció == 3:
        etlap_szerkesztese.kiválasztott_ételek_tápértéke()   #tápérték kiszámítása
        főmenü()
    elif navigáció == 4:
        etlap_szerkesztese.kiválasztott_ételek_ára()        #ár kiszámítása
        főmenü()
    elif navigáció == 5:
        meglepetés = etlap_szerkesztese.meglepetésmenü()
        etlap_szerkesztese.meglepetésmenükiírása(meglepetés)
        print("")
        navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
        while navigáció2 != 0:
            print("Nem létező opció. Kérem, válasszon másikat!")
            print("")
            navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
        print("")
        főmenü()        
    elif navigáció == 6:
        vég = meglepetés
        if len(vég) == 0:
            print("Nem választott megrendelni kívánt ételt.")
            print("")
            navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
        else:    
            etlap_szerkesztese.végleges(vég)
            print("")
            megrendel = input("Meg kívánja rendelni a fenti ételeket? [I]gen/[N]em: ")
            while megrendel != 0:
                if megrendel.lower() == "i":
                    print("")
                    print("Köszönjük a megrendelését!")
                    print("")
                    navigáció2 = int(input("[0] Visszalépés a főmenübe: "))
                    break                    
                elif megrendel.lower() == "n":
                    print("")
                    print("A megrendelését töröltük!")
                    break
                elif megrendel == "0":
                    break
                else:
                    print("Nem létező opció. Kérem, válasszon másikat!")
                    megrendel = input("Meg kívánja rendelni a fenti ételeket? [I]gen/[N]em: ")
        vég.clear()
        print("")
        főmenü()        
    elif navigáció == 9: #<- Itt a szerkesztés menűponthoz hozzáadtam egy jelszó bekérést. Háromszor lehet próbálkozni, utána visszavág a főmenübe. A jelszó: 1234

        szamlaló = 3

        while szamlaló > 0:

            jelszó = int(input("Kérem, adja meg az admin jogosultsághoz a jelszavát: "))

            if jelszó != 1234:
                print(f"Helytelen jelszó! {szamlaló-1} próbálkozása van.")
                print("")

                szamlaló = szamlaló - 1

            else:
                almenű9() #<- almenű9 beillesztve

                szamlaló = 0

                navigáció2 = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))

                while navigáció2 != 0:
                    if navigáció2 == 1:
                        print("1")
                    elif navigáció2 == 2:
                        etlap_szerkesztese.étlapkiirása() #<- először kiíratom az étlapot
                        etlap_szerkesztese.étlapszerkesztése() #<- utána jöhet a szerkesztés
                    elif navigáció2 == 3:
                        etlap_szerkesztese.ételek_törlése() #ételek törlését megcsináltam. A navigáció vissza visz a főmenüig.
                        print("")
                        nav = input("Biztosan menteni kivánja a változtatásokat? [I]gen/[N]em: ")  #<- Külön mentési menüpontot hoztam létre, ennél jobban müködik az igen/nem, mint a számozás, pláne, hogy elötte megjelenítem neki az aktuális változtatásokat
                        while nav.lower() != "0":
                            if nav.lower() == "i":
                                print("A változtatások mentésre kerültek")
                                etlap_szerkesztese.mentés() #<- menti az étlapot a fájlba
                                break
                            elif nav.lower() == "n":
                                etlap_szerkesztese.étlap = etlap_szerkesztese.étlapdefault() #<- ezzel az etlap_szerkesztese.py-on lévő étlap listára hivatkozok, és azt resetelem, így a mentetlen szerkesztés elvész.
                                break
                            else:
                                print("Nem létező opció. Kérem, válasszon másikat!")
                            nav = input("Biztosan menteni kivánja a változtatásokat? [I]gen/[N]em: ")
                        else:
                            print("Nem létező opció. Kérem, válasszon másikat!")
                        almenű9()
                        navigáció2 = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))
                        print("Visszatérés a Főmenübe")
                        print("")
                        etlap_szerkesztese.étlap = etlap_szerkesztese.étlapdefault()
                        főmenü()
                        navigáció = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))
                   
                    elif navigáció2 == 9:
                        etlap_szerkesztese.étlapkiirása() #<- ezzel a már szerkesztett, de még nem mentett étlapot írja ki
                        print("")
                        nav = input("Biztosan menteni kivánja a változtatásokat? [I]gen/[N]em: ")  #<- Külön mentési menüpontot hoztam létre, ennél jobban müködik az igen/nem, mint a számozás, pláne, hogy elötte megjelenítem neki az aktuális változtatásokat
                        while nav.lower() != "0":
                            if nav.lower() == "i":
                                print("A változtatások mentésre kerültek")
                                etlap_szerkesztese.mentés() #<- menti az étlapot a fájlba
                                break
                            elif nav.lower() == "n":
                                etlap_szerkesztese.étlap = etlap_szerkesztese.étlapdefault() #<- ezzel az etlap_szerkesztese.py-on lévő étlap listára hivatkozok, és azt resetelem, így a mentetlen szerkesztés elvész.
                                break
                            else:
                                print("Nem létező opció. Kérem, válasszon másikat!")
                            nav = input("Biztosan menteni kivánja a változtatásokat? [I]gen/[N]em: ")
                        else:
                            print("Nem létező opció. Kérem, válasszon másikat!")

                    almenű9()

                    navigáció2 = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))
           
        print("Visszatérés a Főmenübe")
        print("")
        etlap_szerkesztese.étlap = etlap_szerkesztese.étlapdefault() #<- ezzel az etlap_szerkesztese.py-on lévő étlap listára hivatkozok, és azt resetelem, így a mentetlen szerkesztés elvész (ebben az esetben, amikor visszalép a főmenübe).
        főmenü()

    elif navigáció == 0:
        print("0")
    else:
        print("Nem létező opció. Kérem, válasszon másikat!")

    navigáció = int(input("Kérem, válasszon a fenti lehetőségek közül [0-9]:"))

print("Program vége")
# Így ennyi! Remélem átlátható, meg használható :)

