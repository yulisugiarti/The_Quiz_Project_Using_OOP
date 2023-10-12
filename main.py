from question_model import QuestionModel
from new_data import question_data
from quiz_brain import Quiz

new_data = question_data['results']
question_bank =[]

for item in new_data:
    question = item['question']
    answer = item['correct_answer']
    list_question_answer = QuestionModel(question, answer)
    question_bank.append(list_question_answer)
# print(question_bank)

quiz_beginning = Quiz(question_bank)

# quiz_beginning.question()
quiz_beginning.checking_status()



