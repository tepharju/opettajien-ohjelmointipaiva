import random

# Arvotaan satunnainen luku väliltä 1-100
oikea_luku = random.randint(1, 100)

# Alustetaan arvausten määrä
arvausten_maara = 0

# Silmukka
while True:
    arvaus = int(input("Arvaa luku väliltä 1-100: "))
    arvausten_maara += 1
    
    if arvaus == oikea_luku:
        print(f"Oikein! Arvasit luvun {arvausten_maara} yrityksellä.")
        break
    
    elif arvaus < oikea_luku:
        print("Liian pieni arvaus. Yritä suurempaa lukua.")
        
    else:
        print("Liian suuri arvaus. Yritä pienempää lukua.")