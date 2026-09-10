lentokentät = {"EFHK":"Helsinki-Vantaa", 
               "EFOU":"Oulu", 
               "EFRO":"Rovaniemi", 
               "EFTU":"Turku"}

print("komennot: ")
print("luo")
print("hae")
print("lopeta")

komento = input("Anna komento haluatko syöttää luoda uuden lentoaseman, hakea tai lopettaa ohjelman: ")

lopeta = "lopeta"


while komento != lopeta:
    if komento == "luo":
        icao = input("Anna uuden luomasi lentokentän ICAO koodi: ")
        nimi = input("Anna uuden luomasi lentokentän nimi: ")
        
        if icao in lentokentät or nimi in lentokentät:
            print(f"lentokenttä {nimi} on jo lisätty")

        else:
            lentokentät[icao] = nimi
            print(f"lentokenttä {nimi} onnistuneesti luotu")

    elif komento == "hae":
        haku = input("Anna hakemasi lentokentän ICAO koodi: ")
        if haku in lentokentät:
            lentokentännimi = lentokentät[haku]
            print(f"Hakemasi lentokentän nimi on {lentokentännimi}")

        else:
            print("Lentokenttää ei löytynyt antamallasi koodilla")

    else:
        print("komentoa ei tunnisteta")


    komento = input("Anna komento haluatko syöttää luoda uuden lentoaseman, hakea tai lopettaa ohjelman: ")
