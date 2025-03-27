# Etsitään suomen kielen kaikki palindromit

def on_palindromi(sana):

    kaannetty = sana[::-1]

    if sana == kaannetty:
        return True
    else:
        return False

# Ohjelma alkaa

palindromilista = []

tiedosto = open("kotus_sanat.txt", "r")

sanalista = tiedosto.readlines()

for sana in sanalista:
    sana = sana.rstrip() # poistetaan lopusta rivinvaihdot ja muut tyhjät
    if on_palindromi(sana):
        palindromilista.append(sana)

for sana in palindromilista:
    print(sana)
