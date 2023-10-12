class Quiz:
    def __init__(self, question_list):
        self.number = 0
        self.question_list = question_list
        self.score = 0

    def question_process(self):
        current_question = self.question_list[self.number].text
        true_answer = self.question_list[self.number].answer
        self.number += 1
        user_answer = input(f"Q{self.number}. {current_question} is it (True/False) ")
        self.checking_answer(true_answer, user_answer)

    def checking_answer(self, right_answer, their_answer):
        if their_answer.lower() == right_answer.lower():
            self.score += 1
            print("That's Right!")
        else:
            print("You're Wrong")
        print(f"the right answer is {right_answer}")
        print(f"Your current score compare to the answered questions is {self.score}/{self.number}")
        print("\n")

    def checking_status(self):
        while self.number < len(self.question_list):
            self.question_process()
        print(f"Your score is {self.score}/{self.number}")







