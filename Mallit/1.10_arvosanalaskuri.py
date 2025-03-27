# Kysytään pistemäärä
pisteet = int(input("Anna kokeen pistemäärä (0-100): "))

# Tarkistetaan pisteiden kelvollisuus
if 0 <= pisteet <= 100:
    # Määritetään arvosana
    if pisteet >= 90:
        arvosana = "Erinomainen"
    elif pisteet >= 75:
        arvosana = "Hyvä"
    elif pisteet >= 60:
        arvosana = "Tyydyttävä"
    else:
        arvosana = "Hylätty"
    # Tulostetaan arvosana
    print(f"Arvosanasi on: {arvosana}")
else:
    print("Virheellinen pistemäärä. Anna luku väliltä 0-100.")