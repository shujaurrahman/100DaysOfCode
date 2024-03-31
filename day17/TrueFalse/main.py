from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank=[]

for question in question_data:
    new_question=Question(question["text"],question["answer"])
    question_bank.append(new_question)
    # print(question["text"])
# print(question_bank[0].text)
    
Quiz=QuizzBrain(question_bank)


while Quiz.still_has_question:
    Quiz.next_question()
    
print("You completed the quiz")
print(f"Final Score of Quiz out of  {Quiz.score}/{len(question_bank)}")
