import random
from data_list import questions
total_questions = len(list(questions.keys()))
questions_lists = list(questions.keys())
asked_questions = list(questions.keys())
print("...................Quiz App....................")
print(f"You will be asked {total_questions} questions. Pass Marks = 8")
print("Type your answers and press enter.")
score = 0
count = 1
while count <= total_questions:
    ques = random.choice(asked_questions)
    print(count , ques)
    user_ans = input("Enter you answer:")
    if user_ans.lower() == questions[ques]:
        print("Correct Answer")
        score = score + 1
    else:
        print("Incorrect Answer")
    asked_questions.remove(ques)
    count = count + 1
    
print("QUIZ RESULTS")
print("Total Questios:",total_questions)
print("Your correct answers :", score)
print("Your incorrect answers :", total_questions-score)
if score == total_questions:
    print("Wow, you are perfect in python.")
elif score >= 15 and score <= 21:
    print("Excellent")
elif score >= 10 and score <15:
    print("Good")
elif score < 10:
    print("You need to practice more")