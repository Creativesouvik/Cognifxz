def quiz_game():
    questions = \
    [
        {
            "question": "What is the capital of France?",
            "options": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
            "answer": "c"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
            "answer": "c"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
            "answer": "b"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (a/b/c/d): ").lower()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nYour final score is: {score}/{len(questions)}")

quiz_game()