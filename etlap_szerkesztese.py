# étlap beolvasása kell, hogy hivatkozni tudjunk rá a függvényeinkben
import etlap_beolvasasa




def étlapszerkesztése(étlap):
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

def étlapkiirása(étlap): #<- étlap kiíratása újbóli beolvasáás nélkül.
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

def mentés(étlap): #<- étlap kiírása fájlba. Szerkesztés, törlés, új ételek hozzáadása ezzel lesz mentve.

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

# a kódsorokat kicsit elrendeztem és átláthatóbb modulokra bontottam. egyrésze átkerült az etlap_rendeles-re"

def ételek_törlése(étlap):               #ételek törlése az étlapról.
    print("Étlap tételének törlése:")
    index = 1
    for étel in étlap:
        print(f"[{index}] {étel['étel neve']}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft") # 
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
            print(f"[{index}] {étel['étel neve']}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft") # maradék értékeket hozzáadtam az egységesség miatt
            index += 1
        print("[0] Visszalépés")

        x = int(input("Melyik ételt szeretné törölni?: "))


def étlapújelemhozzáadása(étlap):
    # innen hiányzik az étlap beolvasása, azt egy külön függvényben illesztettem be a menübe.

    énév = None
    étáp = None
    éár = None

    while True:

        print("[0] Visszalépés az előző menübe")

    

        énév = (input("Kérem, adja meg az étel nevét: "))
        if énév == "0":
            break
        print("") #<- hogy átláthatóbb legyen gyakran "kiíratok" ergy üres sort a menüben.
        étáp = int(input("Kérem, adja meg az étel tápértékét [kcal/100gramm]:"))
        if étáp == 0:
            break
        print("") #<- hogy átláthatóbb legyen gyakran "kiíratok" ergy üres sort a menüben.
        éár = int(input("Kérem, adja meg az étel árát [Ft]: "))
        if éár == 0:
            break
        print("") #<- hogy átláthatóbb legyen gyakran "kiíratok" ergy üres sort a menüben.

        újétel = {"étel neve": énév, "tápértéke": étáp, "ára": éár}

        étlap.append(újétel)

        print("")
        index = 1
        for étel in étlap:
            print(f"[{index}] étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
            index += 1