from quiz.data import question_data
from quiz.question_model import Questions
from quiz.quiz_brain import QuizBrain


question_bank = []
data = question_data
for questions in data:
    questions_text = questions['text']
    questions_answer = questions['answer']
    new_questions = Questions(questions_text, questions_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)
quiz.next_question()




