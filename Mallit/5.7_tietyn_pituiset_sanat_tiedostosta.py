sanatiedosto = open("kotus_sanat.txt", "r")

sanalista = sanatiedosto.readlines()

sanatiedosto.close()

oikeat_sanat = []

for sana in sanalista:
    
    sana  = sana.rstrip()
    
    if len(sana) == 3:
        
        oikeat_sanat.append(sana)
        
for sana in oikeat_sanat:
    
    print(sana)