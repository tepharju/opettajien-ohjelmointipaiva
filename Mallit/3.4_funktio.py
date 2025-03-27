# Määritellään funktio
def funktio(x):
    return 2 * x**2 + 3 * x - 5

# Pyydetään käyttäjältä x:n arvo
x_arvo = float(input("Anna muuttujan x arvo: "))

# Lasketaan funktion arvo
tulos = funktio(x_arvo)

# Tulostetaan tulos
print(f"Funktion arvo kohdassa x = {x_arvo} on {tulos}.")