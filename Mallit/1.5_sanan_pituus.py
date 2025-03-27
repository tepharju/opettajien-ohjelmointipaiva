# Kysytään sana käyttäjältä
sana = input("Syötä sana: ")

# Lasketaan merkkien määrä
pituus = len(sana)

# Tarkistetaan, onko merkkejä enemmän kuin yksi
if pituus > 1:

    print(f"Sanassa on {pituus} merkkiä.")

else:

    print("Syötit vain yhden merkin.")