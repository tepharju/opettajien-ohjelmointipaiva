# Kysytään käyttäjältä luku
luku = int(input("Anna kokonaisluku: "))

# Alkuluvun testaus
if luku < 2:
    print(f"{luku} ei ole alkuluku.")
else:
    onko_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            onko_alkuluku = False
            break
    if onko_alkuluku:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")

# Tulostetaan alkuluvut väliltä 2…500
print("Alkuluvut väliltä 2…500:")

for luku in range(2, 501):
    onko_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            onko_alkuluku = False
            break
    if onko_alkuluku:
        print(luku)