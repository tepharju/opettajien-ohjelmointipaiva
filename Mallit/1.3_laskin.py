# Kysytään kaksi kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))

# Lasketaan laskutoimitukset
summa = luku1 + luku2

tulo = luku1 * luku2

erotus = luku1 - luku2

if luku2 != 0:

    osamaara = luku1 / luku2

else:

    osamaara = "Määrittelemätön (nollalla ei voi jakaa)"

# Tulostetaan tulokset
print(f"Lukujen summa: {summa}")
print(f"Lukujen tulo: {tulo}")
print(f"Lukujen erotus: {erotus}")
print(f"Lukujen osamäärä: {osamaara}")