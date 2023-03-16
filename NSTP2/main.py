import random
import json

with open("question.json", "r") as f:
    questions: dict[str: str] = json.load(f)
    
def get_random_question(questions: str) -> str:
    return random.choice(questions)

def main():
    max_score: int = len(questions)
    score: int = 0
    questions_presented = 0
    while questions_presented < max_score:
        question: str = get_random_question(questions)
        answer: str = questions[answer].lower()
        user_input = input(f"{question}:")
        if user_input == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}!")
        
        questions_presented += 1
        
    print("That's the end of the review!")
    print(f"Your score is {score} out of {max_score}.")
    input("Press enter to exit the program.")
    
if __name__ == "__main__":
    main()
    
            
        