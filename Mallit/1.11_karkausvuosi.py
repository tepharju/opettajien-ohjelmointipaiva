import calendar

vuosi = int(input("Anna vuosi: "))

if (vuosi % 400 == 0) and (vuosi % 100 == 0):
    print(f"Vuosi {vuosi} on karkausvuosi")


elif (vuosi % 4 ==0) and (vuosi % 100 != 0):
    print(f"Vuosi {vuosi} on karkausvuosi")


else:
    print(f"{vuosi} ei ole karkausvuosi")


#Tällä voi testata karkausvuoden    

print(calendar.isleap(vuosi))