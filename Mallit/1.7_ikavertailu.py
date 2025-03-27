# Kysytään ensimmäisen henkilön nimi ja syntymävuosi
nimi1 = input("Anna ensimmäisen henkilön nimi: ")
vuosi1 = int(input(f"Anna {nimi1}:n syntymävuosi: "))

# Kysytään toisen henkilön nimi ja syntymävuosi
nimi2 = input("Anna toisen henkilön nimi: ")
vuosi2 = int(input(f"Anna {nimi2}:n syntymävuosi: "))

# Vertailu
if vuosi1 < vuosi2:
    print(f"{nimi1} on vanhempi kuin {nimi2}.")
elif vuosi1 > vuosi2:
    print(f"{nimi2} on vanhempi kuin {nimi1}.")
else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja.")