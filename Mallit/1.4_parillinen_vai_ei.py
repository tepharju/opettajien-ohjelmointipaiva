# Kysytään käyttäjältä luku
luku = int(input("Anna kokonaisluku: "))

# Tarkistetaan parillisuus
if luku % 2 == 0:
    print(f"Luku {luku} on parillinen.")
else:
    print(f"Luku {luku} on pariton.")