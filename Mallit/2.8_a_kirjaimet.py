# Pyydetään sana käyttäjältä
sana = input("Syötä sana: ")

# Alustetaan laskuri
a_maara = 0

# Käydään sanan kirjaimet läpi
for kirjain in sana:
    if kirjain == 'a' or kirjain == 'A':
        a_maara += 1

# Tulostetaan tulos
print(f"Sanassa '{sana}' on {a_maara} a-kirjainta.")