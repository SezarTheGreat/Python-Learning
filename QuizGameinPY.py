#Python quiz game

questions = (
    "How many elements are there in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in earth's atmosphere?",
    "How many bones are there in a human body?",
    "Which planet in the solar system is hottest?"
)

options = (
    ("A: 116", "B: 117", "C: 118", "D: 119"),
    ("A: Whale", "B: Crocodile", "C: Elephant", "D: Ostrich"),
    ("A: Nitrogen", "B: Oxygen", "C: Carbon-Dioxide", "D: Hydrogen"),
    ("A: 206", "B: 207", "C: 208", "D: 209"),
    ("A: Mercury", "B: Venus", "C: Earth", "D: Mars")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, D): ")
    guess = guess.upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct Answer.")
        score += 1
    else:
        print("Incorrect answer.")
        print(f"The correct answer is {answers[question_num]}.")

    question_num += 1  # Increment the question number

print("-----------------------------")
print("          RESULTS            ")
print("-----------------------------")
print("Answers: ", end='')

for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end='')

for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")
