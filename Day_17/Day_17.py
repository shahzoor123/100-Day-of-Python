from quiz.data import question_data
from quiz.question_model import Questions
from quiz.quiz_brain import QuizBrain


question_bank = []
data = question_data
for questions in data:
    questions_text = questions['question']
    questions_answer = questions['correct_answer']
    new_questions = Questions(questions_text, questions_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz your final score is {quiz.score}/{quiz.question_number}")






