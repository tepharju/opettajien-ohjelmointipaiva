import random

# Alustetaan tyhjä lista hedelmille
hedelmat = []

# Kysytään hedelmiä käyttäjältä
while True:
    syote = input("Lisää hedelmä varastoon (kirjoita 'lopeta' lopettaaksesi): ")
    if syote.lower() == 'lopeta':
        break
    elif syote in hedelmat:
        print(f"Hedelmä '{syote}' on jo varastossa.")
    else:
        hedelmat.append(syote)
        print(f"Hedelmä '{syote}' lisätty varastoon.")

# Tarkistetaan, onko varasto tyhjä

if len(hedelmat) > 0:
    # Arvotaan hedelmä
    arvottu_hedelma = random.choice(hedelmat)
    print(f"\nOnnea! Arvottu hedelmä on '{arvottu_hedelma}'.")
else:
    print("Varasto on tyhjä. Ei voitu arpoa hedelmää.")