import json
from json import JSONDecodeError

try:
    with open("question.json", "r+") as file:
        try:
            questions = json.load(file)
        except JSONDecodeError:
            print("JSon file is empty!")
            questions = {}
except FileNotFoundError:
    print("File not found!")
    questions = {}
        
def main():
    while True:
        question = input("Input the question to be added here: ")
        
        if question.lower() == "exit":
            break
        
        answer = input("Input the answer to the question here: ")
        questions[question] = answer
        print("Question added! \n")
        
    with open("question.json", "w") as file:
        file.write(json.dumps(questions, indent=4))
        
if __name__ == "__main__":
    main()
    