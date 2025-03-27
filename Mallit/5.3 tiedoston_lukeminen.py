tiedosto =  open("seitseman_veljesta.txt", "r", encoding="utf8")

rivilista = tiedosto.readlines()

tiedosto.close()

print(rivilista[99])





