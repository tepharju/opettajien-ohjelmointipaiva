def itseisarvo(luku):
    if luku >= 0:
        return luku
    else:
        return -luku

# Esimerkki käytöstä
numero = float(input("Anna luku: "))
tulos = itseisarvo(numero)
print(f"Luvun {numero} itseisarvo on {tulos}.")