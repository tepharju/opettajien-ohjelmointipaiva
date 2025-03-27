luvut =  [45, 44, 36, 39, 40]

def mediaani(lista:list):
    järjestetty = sorted(lista)
    keskikohta = len(järjestetty)//2
    return järjestetty[keskikohta]

print(mediaani(luvut))
    