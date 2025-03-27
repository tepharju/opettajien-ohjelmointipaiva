def listan_tulo(luvut):
    tulo = 1
    for luku in luvut:
        tulo *= luku
    return tulo

# Esimerkki käytöstä
# Pyydetään käyttäjältä lukuja ja tallennetaan ne listaan
luvut = []
maara = int(input("Kuinka monta lukua haluat syöttää? "))

for i in range(maara):
    numero = float(input(f"Anna luku {i+1}: "))
    luvut.append(numero)

# Lasketaan lukujen tulo
tulos = listan_tulo(luvut)

# Tulostetaan tulos
print(f"Syöttämiesi lukujen tulo on {tulos}.")