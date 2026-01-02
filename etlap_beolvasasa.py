def étlapbeolvasása():

    étlap = []
    with open('Python-IKT-Menu/etlap.txt', 'r', encoding='utf-8') as fájl:
        for sor in fájl:
            adatok = sor.strip().split(",")
            étel = {"étel neve": adatok[0], "tápértéke": int(adatok[1]), "ára": int(adatok[2])} #<- Ha van ötlet, még lehet hozzá adni valamit.
            étlap.append(étel)

    index = 1
    for étel in étlap:
        print(f"[{index}] étel neve: {étel["étel neve"]}, tápértéke: {étel["tápértéke"]} kcal/100gramm, ára: {étel["ára"]} Ft")
        index += 1
# A fenti szép hosszú kód kellett ahhoz, hogy szépen megformázva, mértékegységekkel, zárójelek nélkül írja ki a listából a szótárakat.


étlapbeolvasása()

    