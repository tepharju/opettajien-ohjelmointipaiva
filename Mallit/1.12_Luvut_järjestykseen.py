# Kysytään kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# Määritetään pienin, keskimmäinen ja suurin
# Aloitetaan oletuksella
pienin = luku1
keskimmainen = luku2
suurin = luku3

# Vertailut
# Vaihdetaan arvoja tarvittaessa
if pienin > keskimmainen:
    pienin, keskimmainen = keskimmainen, pienin
    
if pienin > suurin:
    pienin, suurin = suurin, pienin
    
if keskimmainen > suurin:
    keskimmainen, suurin = suurin, keskimmainen

# Tulostetaan luvut järjestyksessä
print("Luvut järjestyksessä pienimmästä suurimpaan:")
print(pienin)
print(keskimmainen)
print(suurin)