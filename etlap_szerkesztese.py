# étlap beolvasása kell, hogy hivatkozni tudjunk rá a függvényeinkben
étlap = []
with open("etlap.txt", "r", encoding="utf-8") as fájl:
    for sor in fájl:
        adatok = sor.strip().split(",")
        étel = {"étel neve": adatok[0], "tápértéke": int(adatok[1]), "ára": int(adatok[2])}
        étlap.append(étel)

def étlapszerkesztése():
    # innen hiányzik az étlap beolvasása, azt egy külön függvényben illesztettem be a menübe.
    print("[0] Visszalépés az előző menübe")

    x = int(input("Melyik ételnek az adatait szeretné módosítani [0-9]: "))
    print("") #<- hogy átláthatóbb legyen gyakran "kiíratok" ergy üres sort a menüben.

    while x != 0:
        if x >= 1 and x <= len(étlap):  #<- azért kellett a második értéket len-nel megadni, mert ha az étlaphoz hozzáadunk, vagy elveszünk, így akkor is müködni fog.
            print(f"[1]étel neve: {étlap[x-1]["étel neve"]},\n[2]tápértéke: {étlap[x-1]["tápértéke"]} kcal/100gramm,\n[3]ára: {étlap[x-1]["ára"]} Ft") #<- azért x-1, mert a lista 0-tól indul, de a menüben 1 az első érték.
            print("[0] Visszalépés az előző menübe")
            mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: ")) 
            while mod != 0:
                if mod == 1:
                    név = input("Kérem, adja meg az étel új nevét: ")
                    étlap[x-1]["étel neve"] = név #<- így az étlapban az x-1. szótár "étel neve"-t írom át. A többi értéknél is hasonlóan jártam el.
                    print("")
                    print(f"[1]étel neve: {étlap[x-1]["étel neve"]},\n[2]tápértéke: {étlap[x-1]["tápértéke"]} kcal/100gramm,\n[3]ára: {étlap[x-1]["ára"]} Ft") #<- sortörést raktam az értékek közé, mert szerkesztésnél átláthatóbb.
                    print("[0] Visszalépés az előző menübe")
                    mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: "))
                elif mod == 2:
                    táp = int(input("Kérem, adja meg az étel tápértékét: "))
                    étlap[x-1]["tápértéke"] = táp
                    print("")
                    print(f"[1]étel neve: {étlap[x-1]["étel neve"]},\n[2]tápértéke: {étlap[x-1]["tápértéke"]} kcal/100gramm,\n[3]ára: {étlap[x-1]["ára"]} Ft")
                    print("[0] Visszalépés az előző menübe")
                    mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: "))
                elif mod == 3:
                    ár = int(input("Kérem, adja meg az étel árát: "))
                    étlap[x-1]["ára"] = ár
                    print("")
                    print(f"[1]étel neve: {étlap[x-1]["étel neve"]},\n[2]tápértéke: {étlap[x-1]["tápértéke"]} kcal/100gramm,\n[3]ára: {étlap[x-1]["ára"]} Ft")
                    print("[0] Visszalépés az előző menübe")
                    mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: "))
                else:
                    print("")
                    print("Nem létező opció. Kérem, válasszon másikat!")
                    print("")
                    print(f"[1]étel neve: {étlap[x-1]["étel neve"]},\n[2]tápértéke: {étlap[x-1]["tápértéke"]} kcal/100gramm,\n[3]ára: {étlap[x-1]["ára"]} Ft")
                    print("[0] Visszalépés az előző menübe")
                    mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: "))
        else:
            print("Nem létező opció. Kérem, válasszon másikat!") #<- Ezt nagyjából mindenhol alkalmaztam, ha esetleg hibás "parancs" kerül kiadása.
            print("")

        print("")
        index = 1
        for étel in étlap:
            print(f"[{index}] étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
            index += 1
        print("[0] Visszalépés az előző menübe")
        x = int(input("Melyik ételnek az adatait szeretné módosítani [0-9]: "))

# mod = int(input("Az étel melyik elemét szeretné módosítani [1-3]: ")) <- ez a teszteléshez kellett, de még lehet jól jön így itt hagytam magamnak.

def étlapkiirása(): #<- étlap kiíratása újbóli beolvasáás nélkül.
    index = 1
    for étel in étlap:
        print(f"[{index}] étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
        index += 1

def étlapdefault(): #<- Ez ahhoz kellett, hogy ha szerkesztés után azt választjuk, hogy nem mentjük el, akkor "visszaállítja" az étlapot az eredeti (fájlból beolvasott) állapotába. Sima beolvasásként is használható (bár ezt nem teszteltem le). 

    étlap = []
    with open("etlap.txt", "r", encoding="utf-8") as fájl:
        for sor in fájl:
            adatok = sor.strip().split(",")
            étel = {"étel neve": adatok[0], "tápértéke": int(adatok[1]), "ára": int(adatok[2])}
            étlap.append(étel)      
    return étlap #<- ezzel kerülnek bele az étlapba az "eredeti" elemek.

def mentés(): #<- étlap kiírása fájlba. Szerkesztés, törlés, új ételek hozzáadása ezzel lesz mentve.

    with open("etlap.txt", "w", encoding="utf-8") as fájl:
        for étel in étlap:
            for ertek in étel.values(): #<- így csak a szótárak értékei lesznek kimentve, úgy ahogy az eredeti txt fájlban is szerepelt.
                fájl.write(str(ertek) + ",") #<- visszaalakítva stringekké és vesszővel elválasztva.
            fájl.write("\n") #<- egy szótár értékeinek kimentése után sortörés.
     
'''
index = 1
for étel in étlap:
    print(f"[{index}] étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
    index += 1
'''
    #ezt itt hagytam, ha esetleg még szükség lesz a formázott kiíratásra, csak a három ' kell kitörölni alul és felül.

# ide alulra mehet az "Étlaphoz új elem hozzáadása" és az "Étlap elemeinek törlése"

<<<<<<< HEAD
kiválasztott_ételek = []

def ételek_kiválasztása():  #Ezzel lehet kiválasztani az étlapról az ételeket.
    print("Étlap:")
    index = 1
    for étel in étlap:
        print(f"[{index}] {étel['étel neve']}")
        index += 1
    print("")

    x = int(input("Válasszon ételt: "))

    while x != 0:
        if 1 <= x <= len(étlap):
            kiválasztott_ételek.append(étlap[x-1])
            print(f"{étlap[x-1]['étel neve']} hozzáadva a listához.")
        else:
            print("Nincs ilyen opció!")

        print("")
        x = int(input("Válasszon újabb ételt [0 = kész]: "))





def kiválasztott_ételek_törlése():   #Csináltam olyan lehetöséget, hogy a kiválasztott ételeket lehessen szerkeszteni.
    if len(kiválasztott_ételek) == 0:
        print("Nincs kiválasztott étel!")

    while True:
        print("\nKiválasztott ételek:")
        index = 1
        for étel in kiválasztott_ételek:
            print(f"[{index}] {étel['étel neve']} "
                  f"({étel['tápértéke']} kcal/100g, {étel['ára']} Ft)")
            index += 1

        print("[0] Kész ")

        x = int(input("Szeretné törölni valamelyik ételt?: "))

        if x == 0:
            break
        elif 1 <= x <= len(kiválasztott_ételek):
            törölt = kiválasztott_ételek.pop(x-1)
            print(f"{törölt['étel neve']} törölve lett a kiválasztások közül.")
        else:
            print("Nincs ilyen opció!")



def kiválasztott_ételek_tápértéke():    #a kiválasztott ételek kalóriáját kalkulálja ki.
    if len(kiválasztott_ételek) == 0:
        print("Nincs kiválasztott étel!")
       

    össz_tápérték = 0

    print("\nKiválasztott ételek tápértéke:")
    for étel in kiválasztott_ételek:
        print(f"- {étel['étel neve']}: {étel['tápértéke']} kcal/100g")
        össz_tápérték += étel["tápértéke"]

    print(f"\nÖsszes tápérték: {össz_tápérték} kcal/100g")





def kiválasztott_ételek_ára():    #a kiválasztott ételek árát kalkulálja ki.
    if len(kiválasztott_ételek) == 0:
        print("Nincs kiválasztott étel!")
       

    össz_ára = 0

    print("\nKiválasztott ételek ára:")
    for étel in kiválasztott_ételek:
        print(f"- {étel['étel neve']}: {étel['ára']} Ft")
        össz_ára += étel["ára"]

    print(f"\nÖsszes ára: {össz_ára} Ft")




def ételek_törlése():               #ételek törlése az étlapról.
    print("Étlap tételének törlése:")
    index = 1
    for étel in étlap:
        print(f"[{index}] {étel['étel neve']}")
        index += 1
    print("[0] Visszalépés")

    x = int(input("Melyik ételt szeretné törölni?: "))

    while x != 0:
        if 1 <= x <= len(étlap):
            törölt = étlap.pop(x-1)
            print(f"{törölt['étel neve']} törölve lett.")
        else:
            print("Nincs ilyen opció!")

        print("")
        index = 1
        for étel in étlap:
            print(f"[{index}] {étel['étel neve']}")
            index += 1
        print("[0] Visszalépés")

        x = int(input("Melyik ételt szeretné törölni?: "))
=======
def rendelés():
    rendeles = []
    választás = int(input("Melyik ételt szeretné megrendelni[0-9]? "))
    while választás != 0:
        rendeles.append(étlap[választás-1])
        for étel in rendeles:
            print(f"étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
        választás = int(input("Melyik ételt szeretné megrendelni[0-9]? "))

    return rendeles

import random

def meglepetésmenü():

    meglepetés = []

    meglepi = int(input("Hány fő részére szeretne meglepetés menűt? "))

    for i in range(meglepi):
        meglepetés.append(étlap[random.randint(0, len(étlap)-1)])
    
    return meglepetés

def meglepetésmenükiírása(meglepetés):

    index = 1
    for étel in meglepetés:
        print(f"{index}. étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
        index += 1


    összár = sum(étel["ára"] for étel in meglepetés)
    print(f"\t\t\tÖsszesen {összár} Ft.")


# meglepetés = meglepetésmenü()
# rendeles = rendelés()

# vég = meglepetés + rendeles

def végleges(vég):
    
    index = 1
    for étel in vég:
        print(f"{index}. étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")    
        index += 1

    összár = sum(étel["ára"] for étel in vég)
    print(f"\t\t\tÖsszesen {összár} Ft.")
>>>>>>> 9534eb8 (meglepi menü hozzáadva)
