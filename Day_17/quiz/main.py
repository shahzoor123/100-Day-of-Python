from data import question_data
from question_model import Questions

question_bank = []
data = question_data
for questions in data:
    questions_text = questions['text']
    questions_answer = questions['answer']
    new_questions = Questions(questions_text, questions_answer)
    question_bank.append(new_questions)
print(question_bank[2].answer)
