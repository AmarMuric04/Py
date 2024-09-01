class QuizBrain:
    def __init__(self, question_number, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        index = self.question_number
        question = self.question_list[index]
        question_answer = input(f"Q.{index}: {question["text"]} (True/False)")
        if question_answer == question["answer"]:
          print("correct.")
        else:
          print("incorrect.")
