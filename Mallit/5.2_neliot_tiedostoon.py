tiedosto  = open("neliot.txt", "w")

for k in range(1,101):
    
    tiedosto.write(str(k**2)+"\n")

tiedosto.close()

print("Valmis!")