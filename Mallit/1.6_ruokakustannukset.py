# Kysytään työpaikkaruokailun hinta ja määrä
lounaan_hinta = float(input("Anna työpaikkaruokailun hinta (€): "))
lounaita_viikossa = int(input("Kuinka monta kertaa syöt lounaan viikossa? "))

# Kysytään muiden ruokaostosten hinta viikossa
muut_ruokaostokset = float(input("Anna muiden ruokaostosten hinta viikossa (€): "))

# Lasketaan viikottaiset ja päivittäiset ruokamenot
viikon_menot = (lounaan_hinta * lounaita_viikossa) + muut_ruokaostokset

# Tarkistetaan alennus
if viikon_menot > 100:
    alennus = viikon_menot * 0.10
    viikon_menot -= alennus
    print(f"Saat 10% alennuksen ({alennus:.2f} €)!")
else:
    alennus = 0

paivan_menot = viikon_menot / 7

# Tulostetaan menot
print(f"Ruokamenot viikossa: {viikon_menot:.2f} €")
print(f"Keskimääräiset ruokamenot päivässä: {paivan_menot:.2f} €")