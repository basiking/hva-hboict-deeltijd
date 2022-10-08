#Name: Bas van der Vegt | Goal: Practicum5 Opdracht

#Controleer of een waarde tussen een minimum en een maximum zit; argumenten: waarde, min, max; returnwaarde: True of False
def isTussen(waarde, min, max):
    if min <= waarde <= max:
        return True
    else:
        return False

#Laat zien of de waarde gezond is; argumenten: Type, waarde, minimum, maximum
def checkGezondheid(gezondheidsType, gezondheidsWaarde, min, max):
    if isTussen(gezondheidsWaarde, min, max) == True:
        print(f"Uw {gezondheidsType} ({gezondheidsWaarde}) is gezond.")
    else:
        print(f"Uw {gezondheidsType} ({gezondheidsWaarde}) is niet gezond.")

#vraag om waarden van hartslag, lichaamstemperatuur en bovendruk
hartslag = int(input("Vul uw hartslag in: "))
lichaamsTemperatuur = float(input("Vul uw lichaamstemperatuur in: "))
bovendruk = int(input("Vul uw bovendruk in: "))

#check voor elke test de gezondheid
checkGezondheid("hartslag", hartslag, 55, 90)
checkGezondheid("lichaamstemperatuur", lichaamsTemperatuur, 36.3, 37.5)
checkGezondheid("bovendruk", bovendruk, 100, 140)