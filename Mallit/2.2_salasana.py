# Määritellään oikea salasana
oikea_salasana = "soylentgreenispeople"

# Alustetaan yritysten määrä
yritykset = 0
maksimi_yritykset = 3

# Silmukka salasanaa varten
while yritykset < maksimi_yritykset:
    syote = input("Anna salasana: ")
    
    if syote == oikea_salasana:
        print("Salasana oikein. Pääsy sallittu.")
        break
    
    else:
        yritykset += 1
        print("Väärä salasana.")
        
        if yritykset == maksimi_yritykset:
            print("Liian monta yritystä. Pääsy evätty.")