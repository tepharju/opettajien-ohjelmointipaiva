# Kochin lumihiutale-fraktaali
# Panu Kalliokoski 2019

import turtle

from turtle import fd, rt, lt, bk, speed

# Komennot: 
# lt (60)    # Käänny vasemaan 60 astetta
# rt (60)    # Käänny oikealle 60 astetta
# fd(3)      # Eteenpäin 3 yksikköä
# bk(3)      # Taaksepäin 3 yksikköä

def koch(min_pituus, pituus):
    if pituus < min_pituus:
        fd(pituus)
        return
    koch(min_pituus, pituus/3.)
    lt(60)
    koch(min_pituus, pituus/3.)
    rt(120)
    koch(min_pituus, pituus/3.)
    lt(60)
    koch(min_pituus, pituus/3.)
    
turtle.Screen()

speed(0)   # Suurempi luku on nopeampi

koch(10,450)       # Fraktaalin piirto. Vaihda näitä lukuja!

turtle.done()
turtle.bye()