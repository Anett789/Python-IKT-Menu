# étlap beolvasása kell, hogy hivatkozni tudjunk rá a függvényeinkben
import etlap_beolvasasa


kiválasztott_ételek = []

def ételek_kiválasztása(étlap):  #Ezzel lehet kiválasztani az étlapról az ételeket.
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

    return kiválasztott_ételek




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

'''
def rendelés(étlap):
    rendeles = []
    választás = int(input("Melyik ételt szeretné megrendelni[0-9]? "))
    while választás != 0:
        rendeles.append(étlap[választás-1])
        for étel in rendeles:
            print(f"étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
        választás = int(input("Melyik ételt szeretné megrendelni[0-9]? "))

    return rendeles
'''
import random

def meglepetésmenü(étlap):

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


def végleges(vég):

    index = 1
    for étel in vég:
        print(f"{index}. étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")    
        index += 1
    
    összár = sum(étel["ára"] for étel in vég)
    print(f"\t\t\tÖsszesen {összár} Ft.")