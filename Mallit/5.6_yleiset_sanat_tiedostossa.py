sanalista = {}

with open("seitseman_veljesta.txt", "r", encoding="utf8") as veljekset:
    rivit = veljekset.readlines()

for rivi in rivit:
    sanat = rivi.split()
    for sana in sanat:
        sana = sana.strip("!?.,)(:;»-").lower()
        if sana in sanalista:
            sanalista[sana] += 1
        else:
            sanalista[sana]=1


jarjestetty = sorted(sanalista.items(), key = lambda arvopari: -arvopari[1])


for i in range(100):
    
    x = jarjestetty[i]
    
    print(x[0]+":"+(15-len(x[0]))*" " + str(x[1]) + " kpl")
        

