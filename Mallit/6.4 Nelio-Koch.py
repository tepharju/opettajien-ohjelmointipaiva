# Kochin neliökäyrä-fraktaali

import turtle
from turtle import fd, rt, lt, bk, speed

def nelioKoch(min_pituus, pituus):
    if pituus < min_pituus:
        fd(pituus)
        return
    nelioKoch(min_pituus, pituus/4.)
    lt(90)
    nelioKoch(min_pituus, pituus/4.)
    rt(90)
    nelioKoch(min_pituus, pituus/4.)
    rt(90)
    nelioKoch(min_pituus, pituus/4.)
    nelioKoch(min_pituus, pituus/4.)
    lt(90)
    nelioKoch(min_pituus, pituus/4.)
    lt(90)
    nelioKoch(min_pituus, pituus/4.)
    rt(90)
    nelioKoch(min_pituus, pituus/4.)
    
turtle.Screen()
speed(0)   # Suurempi luku on hitaampi
nelioKoch(10,400)  # Fraktaalin piirto. Vaihda näitä lukuja!
turtle.done()
turtle.bye()

