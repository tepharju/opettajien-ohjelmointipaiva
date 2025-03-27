# Kysytään käyttäjän nimi ja ikä
nimi = input("Anna nimesi: ")
ika = int(input("Anna ikäsi: "))

# Tervehditään käyttäjää
print(f"Hei {nimi}!")

# Lasketaan syntymävuosi

syntymavuosi = 2024 - ika

# Lasketaan elinaika sekunneissa

elinaika_sekunneissa = ika * 365 * 24 * 60 * 60

# Tulostetaan tulokset
print(f"Syntymävuotesi on {syntymavuosi}.")
print(f"Olet elänyt noin {elinaika_sekunneissa} sekuntia.")