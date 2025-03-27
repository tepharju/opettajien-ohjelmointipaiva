# Kysytään positiivinen kokonaisluku N
N = int(input("Anna positiivinen kokonaisluku N: "))

# Tarkistetaan, että N on positiivinen
if N > 0:
    # Käydään luvut läpi väliltä -N...N, mutta ei nollaa
    for luku in range(-N, N+1):
        if luku != 0:
            print(luku)
else:
    print("Luku ei ollut positiivinen kokonaisluku.")