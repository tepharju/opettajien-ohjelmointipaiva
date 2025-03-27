# Alustetaan tyhjä lista
luvut = []

# Kysytään lukuja käyttäjältä
while True:
    luku = float(input("Anna luku (0 lopettaa): "))
    if luku == 0:
        break
    else:
        luvut.append(luku)

# Tarkistetaan, ettei lista ole tyhjä
if len(luvut) > 0:
    keskiarvo = sum(luvut) / len(luvut)
    print(f"Syöttämiesi lukujen keskiarvo on {keskiarvo}")
else:
    print("Et syöttänyt yhtään lukua.")