import random

class Question:
    def __init__(self, title, answer, fakeAnswer, questionType="open"):
        self.title = title
        self.answer = answer
        self.fakeAnswer = fakeAnswer
        self.questionType = questionType
    
    def ShowQuestion(self):
        
        if self.questionType == "mpc":
            print(f"Vraag: {self.title}")
            #make list of answers and add correct answer to it
            answers = []
            answers.append(self.answer)

            #add fakeanswers to list of answers
            for f in self.fakeAnswer:
                answers.append(f)
        
            #Put questions in random order and print them
            random.shuffle(answers)
            x = 1
            y = 0
            for a in answers:
                print(f"{x}. {a}")
                if a == self.answer:
                    y = str(x)
                x += 1

            userAnswer = input("Vul hier uw antwoord in: ")
            if userAnswer == self.answer or y == userAnswer:
                print(f"Dat klopt. Het juiste antwoord was: {self.answer} ({y}).")
            else:
                print(f"Dat klopt niet. Het juiste antwoord was: {self.answer} ({y}).")
            
        elif self.questionType == "truefalse":
            pass
        elif self.questionType == "mpc":
            pass
        


# def CheckAnswer(answer):
#     #check if the answer from the user is correct
#     userAnswer = input("Vul hier uw antwoord in: ")
#     if userAnswer == answer:
#         print("Uw antwoord is correct. \U0001F44D")
#         return True
#     else:
#         print("Uw antwoord is fout. \U0001F44E")
#         print(f"Het goede antwoord was: \"{answer} \".")
#         return False

# def ShowResults(correctAnswers, falseAnswers):
#     #calculate the percentage of correctly answered questions from the quiz
#     totalAnswersAmount = correctAnswers + falseAnswers
#     percentage = correctAnswers / totalAnswersAmount * 100
    
#     print(f"U heeft {correctAnswers} vragen van de {totalAnswersAmount} vragen goed beantwoord.")
#     print(f"Dit is een percentage van {percentage}%.")
#     #check if the user answered enough questions to earn a passing grade
#     if percentage >= 55:
#         print(f"Gefeliciteerd! U heeft een voldoende behaald (u heeft tenminste 55% van de vragen goed beantwoord).")
#     else:
#         print(f"Helaas! U heeft een onvoldoende behaald (u heeft minder dan 55% van de vragen goed beantwoord") 
  
# def PlayQuiz(quiz):
#     correctAnswers = 0
#     falseanswers = 0
#     for question in quiz:
#         if question.ShowQuestion() == True:
#             correctAnswers += 1
#         else:
#             falseanswers += 1
#     print(correctAnswers)        

q1 = Question("Wat is 2 + 2?", "Dat is 4.", ["Dat is 5.", "Dat is 6", "Dat is 7"], "mpc")
q1.ShowQuestion()
q2 = Question("Wat is 10 * 2?", "Dat is 20.", ["Dat is 4.", "Dat is 9", "Dat is 18"], "mpc")
q2.ShowQuestion()

# quiz = [q1, q2]
# PlayQuiz(quiz)


#check for questions -> for each question showQuestion->CheckAnswer  ShowResults
#MAIN MENU LOOP: 1. SPEEL QUIZ 2. MAAK QUIZ 3. BEWERK QUIZ 4. AFSLUITEN
# SPEEL QUIZ -> SELECTEER QUIZ -> LOOP(VUL VRAAG IN -> CHECK VRAAG MET ANTWOORD -> RETURN RESULTAAT)
# MULTIPLE CHOICE -> LAAT TITEL ZIEN: 
#
#
#
#
#
