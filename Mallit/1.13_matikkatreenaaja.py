import random
# Generoidaan kaksi satunnaista lukua väliltä 1-10
luku1 = random.randint(1, 10)
luku2 = random.randint(1, 10)

# Valitaan satunnainen operaattori
operaatiot = ['+', '-', '*', '/']
operaatio = random.choice(operaatiot)

# Tämän voisi tehdä myös arpomalla satunnaisluku väliltä 1..4 ja asettamalla
# 1 = jakolasku, 2 = tulo jne. 

# Varmistetaan, ettei jakolaskussa jaeta nollalla
if operaatio == '/':
    while luku2 == 0:
        luku2 = random.randint(1, 10)

# Lasketaan oikea vastaus
if operaatio == '+':
    oikea_vastaus = luku1 + luku2
elif operaatio == '-':
    oikea_vastaus = luku1 - luku2
elif operaatio == '*':
    oikea_vastaus = luku1 * luku2
elif operaatio == '/':
    oikea_vastaus = luku1 / luku2

# Pyydetään käyttäjältä vastaus
kayttajan_vastaus = input(f"Mikä on {luku1} {operaatio} {luku2}? ")

# Yritetään muuntaa vastaus numeroksi
try:
    kayttajan_vastaus = float(kayttajan_vastaus)
except ValueError:
    print("Virheellinen syöte. Vastaus täytyy olla numero.")
    exit()

# Tarkistetaan vastaus
if abs(kayttajan_vastaus - oikea_vastaus) < 0.0001:
    print("Oikein! Hyvin tehty.")
else:
    print(f"Väärin. Oikea vastaus on {oikea_vastaus}.")