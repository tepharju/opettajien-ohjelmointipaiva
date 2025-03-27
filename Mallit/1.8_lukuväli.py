# Kysytään luku käyttäjältä
luku = float(input("Anna luku: "))

# Testataan kuuluuko luku välille [4, 9]
if 4 <= luku <= 9:
    print(f"Luku {luku} on välillä [4, 9].")
else:
    print(f"Luku {luku} ei ole välillä [4, 9].")