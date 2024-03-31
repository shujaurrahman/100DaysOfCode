class QuizzBrain:
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_has_question(self):
        return self.question_number<len(self.question_list)
        

    def next_question(self):
        while self.question_number<len(self.question_list):
            curret_question=self.question_list[self.question_number]
            self.question_number+=1
            user_answer=input(f"Q.{self.question_number}: {curret_question.text} (True/False): ")
            self.check_answer(user_answer,curret_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}")

