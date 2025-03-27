# Kysytään välin alku ja loppu
alku = int(input("Anna välin alku: "))
loppu = int(input("Anna välin loppu: "))

# Tulostetaan parittomat luvut

print(f"Parittomat luvut välillä {alku} - {loppu}:")

for luku in range(alku, loppu + 1):
    if luku % 2 != 0:
        print(luku)