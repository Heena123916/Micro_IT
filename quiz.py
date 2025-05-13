import time

# Sample quiz questions by category
quiz_data = {
    "Geography": [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which ocean is the largest?",
            "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
            "answer": "C"
        }
    ],
    "Science": [
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Venus", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"],
            "answer": "D"
        }
    ]
}

def ask_question(q, time_limit=10):
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    start = time.time()
    answer = input(f"Your answer (A/B/C/D) - You have {time_limit} seconds: ").upper()
    end = time.time()

    time_taken = end - start
    if time_taken > time_limit:
        print("Time's up!")
        return False, q["answer"]
    elif answer == q["answer"]:
        print("Correct!")
        return True, q["answer"]
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")
        return False, q["answer"]

def run_quiz():
    print("Welcome to the Quiz Game!")
    print("Available Categories:")
    for i, cat in enumerate(quiz_data.keys(), 1):
        print(f"{i}. {cat}")
    
    try:
        category_choice = int(input("Choose a category number: "))
        category = list(quiz_data.keys())[category_choice - 1]
    except:
        print("Invalid choice. Exiting.")
        return

    print(f"\nYou chose: {category}")
    questions = quiz_data[category]
    score = 0
    total = len(questions)
    correct_answers = []

    for q in questions:
        correct, ans = ask_question(q)
        if correct:
            score += 1
        correct_answers.append((q["question"], ans))

    print(f"\nQuiz Over! You scored {score} out of {total}.")
    print("\nAnswer Review:")
    for q, a in correct_answers:
        print(f"Q: {q}\nCorrect Answer: {a}\n")

run_quiz()