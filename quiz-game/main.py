from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_number = 0
# score = 0
# for question in question_data:
#     user_answer = input(f"Q.{question_number}: {question['question']} (True/ False): ")
#     question_number += 1
#     if user_answer.lower() == question["correct_answer"].lower():
#         score += 1
#         print("You got it right!")
#     else:
#         print("That's wrong.")
#     print(f"The correct answer was {question['correct_answer']}.")
#     print(f"Your current score is {score}/{question_number}")
#     print("\n")
# print("You've completed the quiz")
# print(f"Your final score was: {score}/{question_number}")
# exit(0)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

