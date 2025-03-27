# Tuodaan math-moduuli käyttöön
import math

# Kysytään sivujen a ja b pituudet
a = float(input("Anna sivun a pituus: "))
b = float(input("Anna sivun b pituus: "))

# Lasketaan hypotenuusa kaavalla c = sqrt(a^2 + b^2)
c = math.sqrt(a**2 + b**2)

# Tulostetaan hypotenuusan pituus
print(f"Hypotenuusan pituus on {c}")