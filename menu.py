def mainMenu():
    userInput = 'x'
    while userInput not in ['a','b','c','d']:
        print("""Menu
              a) Quiz spelen
              b) Quiz Aanmaken
              c) Quiz Bewerken
              d) Programma Afsluiten
              """)
        userInput = input("Vul een letter in [a-d] om iets te doen.")
        if userInput == "a":
            print("Quiz afspelen")
        elif userInput == "b":
            print("Quiz aanmaken")
        elif userInput == "c":
            print("Quiz bewerken")
        elif userInput == "d":
            print("Programma Afsluiten")
mainMenu()
print("klaar")