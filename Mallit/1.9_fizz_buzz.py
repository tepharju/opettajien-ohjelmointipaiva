# Kysytään käyttäjältä luku
luku = int(input("Anna kokonaisluku: "))

# Tarkistetaan jaollisuus sekä kolmella että viidellä ensin
if luku % 3 == 0 and luku % 5 == 0:
    print("FizzBuzz")
elif luku % 3 == 0:
    print("Fizz")
elif luku % 5 == 0:
    print("Buzz")
else:
    print(luku)