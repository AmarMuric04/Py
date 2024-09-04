class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        index = self.question_number

        question_answer = input(f"Q.{index}: {question.text} (True/False): ")
        self.check_answer(question_answer, question.answer)
        self.question_number += 1

    def still_has_questions(self):
        print(self.question_number, len(self.question_list))
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("That's incorrect...")
        print(f"The correct answer was: {question_answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print()
