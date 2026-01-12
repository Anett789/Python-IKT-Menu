def étlapbeolvasása(): #<- étlap beolvasása fájlból és kiíratása. A külön kiíratás az etlap_szerkesztese.py-on van.

    étlap = []
    with open("etlap.txt", "r", encoding="utf-8") as fájl:
        for sor in fájl:
            adatok = sor.strip().split(",")
            étel = {"étel neve": adatok[0], "tápértéke": int(adatok[1]), "ára": int(adatok[2])} #<- Ha van ötlet, még lehet hozzá adni valamit.
            étlap.append(étel)

    return étlap

# A fenti szép hosszú kód kellett ahhoz, hogy szépen megformázva, mértékegységekkel, zárójelek nélkül írja ki a listából a szótárakat.


# étlapbeolvasása()
