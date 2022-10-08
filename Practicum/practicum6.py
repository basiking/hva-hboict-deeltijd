#Name: Bas van der Vegt | Goal: Practicum6 Opdracht
import random

#Get the amount of numbers the user wants to generate. Make the user try again until they enter a correct number.
numberlist = []
numberAmount = 0
while numberAmount < 5 or numberAmount > 25:
    numberAmount = int(input("Hoe groot moet de lijst getallen zijn [5-25]? "))
    if numberAmount < 5 or numberAmount > 25:
        print("Doe nog een poging.")
    else:
        break

#Add the specified amount of numbers to the list
for number in range(1, numberAmount + 1):
    numberlist.append(random.randint(0,9))

#Print the numbers from the list
print(*numberlist, sep=",")

#Ask the user which number to search for
wantedNumber = -1
while wantedNumber < 0 or wantedNumber > 9:
    wantedNumber = int(input("Welk getal moet ik zoeken? "))
    if 0 <= wantedNumber <= 9:
        break
    else:
        print("Het zoekgetal moet tussen 0 en 9 liggen! Doe nog een poging.")

#Check how many times the wanted number appears in the list
correctNumbers = 0
for i in numberlist:
    if i == wantedNumber:
        correctNumbers += 1

#Calculate the percentage of correct numbers and print it
percentage = round(correctNumbers / len(numberlist) * 100, 1)
print(f"""Het getal {wantedNumber} komt {correctNumbers} keer voor in de lijst.
      Dat betekent dat {percentage}% van de getallen in de lijst gelijk is aan {wantedNumber}.""")