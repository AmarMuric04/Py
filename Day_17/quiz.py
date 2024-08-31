from data import question_data
from question_model import Question

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))


for q in question_bank:
    print(q.text, q.answer)
