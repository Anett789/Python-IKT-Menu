124
etlap = {

  "Almával töltött csirkemell" : {

    "azonosito": "1",

    "nev": "Almával töltött csirkemell",

    "ar": 1000,

    "kaloria_tartalom": 500,

    "alapanyagok": ["alma", "csirkemell", "sajt", "tejföl"]

  },

  "Almáspite" : {

    "azonosito": "1",

    "nev": "Almáspite",

    "ar": 2000,

    "kaloria_tartalom": 100,

    "alapanyagok": ["alma", "porcukor", "tojás", "tejföl", "vaj", "liszt,"]

  },

  "Franciasaláta" : {

    "azonosito": "1",

    "nev": "Franciasaláta",

    "ar": 4000,

    "kaloria_tartalom": 200,

    "alapanyagok": ["alma", "krumpli" , "fehérrépa", "sárgarépa", "zöldborsó", "tejföl", "majonéz","mustár","só", "bors", "citromlé"]

  }

}
#ezért lett szükséges az azonosító(a listában a lista), mert egyszerűbb a menüből úgy választani, hogy csakszámokat ír be a rendelő)
 
valasztas = input("Kérlek válaszd ki a menüpontot:")

if valasztas == "1":

    etelekListazasa(valasztas)

elif valasztas == "2":

      print("Még nincs kész")