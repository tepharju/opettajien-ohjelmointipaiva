# Kysytään lukua, kunnes luku on positiivinen
while True:
    luku = float(input("Anna positiivinen luku: "))
    if luku > 0:
        print(f"Syötit luvun {luku}.")
        break
    else:
        print("Luku ei ollut positiivinen. Yritä uudelleen.")