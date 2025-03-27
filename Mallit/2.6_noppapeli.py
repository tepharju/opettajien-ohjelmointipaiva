import random

# Kysytään kierrosten määrä
kierrokset = int(input("Kuinka monta kierrosta pelataan? "))

# Alustetaan laskurit
noppa1_voitot = 0
noppa2_voitot = 0
tasapelit = 0

# Suoritetaan kierrokset
for kierros in range(kierrokset):
    # Heitetään noppia
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    
    # Verrataan tuloksia
    if noppa1 > noppa2:
        noppa1_voitot += 1
    elif noppa2 > noppa1:
        noppa2_voitot += 1
    else:
        tasapelit += 1

# Tulostetaan tulokset
print(f"Noppa 1 voitti {noppa1_voitot} kertaa.")
print(f"Noppa 2 voitti {noppa2_voitot} kertaa.")
print(f"Tasapelejä oli {tasapelit}.")

# Ilmoitetaan kumpi voitti useammin
if noppa1_voitot > noppa2_voitot:
    print("Noppa 1 voitti useammin.")
elif noppa2_voitot > noppa1_voitot:
    print("Noppa 2 voitti useammin.")
else:
    print("Nopat voittivat yhtä monta kertaa.")