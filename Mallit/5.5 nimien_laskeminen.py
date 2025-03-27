# Lasketaan, kuinka monta kertaa kukin veljeksistä mainitaan kirjassa "Seitsemän veljestä".

nimet = ["juhani", "tuomas", "aapo", "simeoni", "timo", "lauri", "eero"]



nimikirjasto = {}

for nimi in nimet:

    nimikirjasto[nimi] = 0

print(nimikirjasto)


kirja = open("seitseman_veljesta.txt", "r", encoding="utf8")

rivit = kirja.readlines()

for rivi in rivit:
    sanat = rivi.split()
    for sana in sanat:
        sana = sana.strip("!?.,)(:;»").lower()
        if sana in nimet:

            nimikirjasto[sana] += 1

print(nimikirjasto)
