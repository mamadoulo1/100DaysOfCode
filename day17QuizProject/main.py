from question_model import *
from data import *
from quiz_brain import *

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))


quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quizz")
print(f"Your final score was: {quizz.score}/{len(question_bank)}")