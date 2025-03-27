# Lasketaan, kuinka monta kertaa Juhani mainitaan kirjassa "Seitsemän veljestä".

laskettava = "juhani"  # Kirjoita pienellä

kirjatiedosto = open("seitseman_veljesta.txt", "r", encoding="utf8")

rivien_lista = kirjatiedosto.readlines()

kirjatiedosto.close()

laskuri = 0

for rivi in rivien_lista:
    
    rivin_sanat_listana = rivi.split()  #split luo listan yksittäisistä sanoista
    
    for sana in rivin_sanat_listana:
        sana = sana.strip("!?.,)(:;»").lower()
        
        if sana == laskettava:

            laskuri += 1

print("Sana", laskettava, "esiintyy", laskuri, "kertaa.")
