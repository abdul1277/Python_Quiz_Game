# Python Quiz Game - Advanced Version
# Author: Abdul Rauf (Demo Version)
# Features:
# - 50 multiple choice questions
# - Each round 5 questions
# - Round summary: correct/wrong answers
# - Case-insensitive input (a/A accepted)
# - Pure English questions

print("Welcome to Python Quiz Game!")
score = 0
round_number = 1
questions_per_round = 5

# ------------------------
# Questions List (50 questions)
# ------------------------
questions = [
    {"question": "Who invented Python?", "options": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"], "answer": "A"},
    {"question": "What is the latest version of Python?", "options": ["A. 2.7", "B. 3.12", "C. 3.5", "D. 3.10"], "answer": "B"},
    {"question": "Which language is Python inspired from?", "options": ["A. C", "B. Java", "C. ABC", "D. Ruby"], "answer": "C"},
    {"question": "Which keyword is used for function in Python?", "options": ["A. func", "B. define", "C. def", "D. function"], "answer": "C"},
    {"question": "What data type is used to store True or False?", "options": ["A. int", "B. bool", "C. str", "D. float"], "answer": "B"},
    {"question": "Which symbol is used for comments in Python?", "options": ["A. //", "B. #", "C. <!-- -->", "D. **"], "answer": "B"},
    {"question": "How do you create a list in Python?", "options": ["A. {}", "B. []", "C. ()", "D. <>"], "answer": "B"},
    {"question": "Which operator is used for exponentiation?", "options": ["A. **", "B. ^", "C. %", "D. *"], "answer": "A"},
    {"question": "Which function converts string to integer?", "options": ["A. str()", "B. int()", "C. float()", "D. bool()"], "answer": "B"},
    {"question": "Which keyword is used for loops in Python?", "options": ["A. for", "B. loop", "C. iterate", "D. while"], "answer": "A"},
    
    {"question": "Which keyword is used for while loop?", "options": ["A. loop", "B. while", "C. iterate", "D. repeat"], "answer": "B"},
    {"question": "What is the output of 2 ** 3 in Python?", "options": ["A. 5", "B. 6", "C. 8", "D. 9"], "answer": "C"},
    {"question": "Which method adds an element at the end of list?", "options": ["A. add()", "B. append()", "C. insert()", "D. push()"], "answer": "B"},
    {"question": "Which method removes last element from list?", "options": ["A. pop()", "B. remove()", "C. delete()", "D. discard()"], "answer": "A"},
    {"question": "Which operator is used for floor division?", "options": ["A. /", "B. //", "C. %", "D. **"], "answer": "B"},
    {"question": "Which function prints output in Python?", "options": ["A. echo()", "B. print()", "C. output()", "D. write()"], "answer": "B"},
    {"question": "Which keyword is used to handle exceptions?", "options": ["A. try", "B. catch", "C. handle", "D. except"], "answer": "A"},
    {"question": "Which keyword handles exceptions along with try?", "options": ["A. except", "B. catch", "C. finally", "D. handle"], "answer": "A"},
    {"question": "Which symbol is used for multiplication?", "options": ["A. x", "B. *", "C. **", "D. %"], "answer": "B"},
    {"question": "Which symbol is used for modulo operation?", "options": ["A. /", "B. //", "C. %", "D. **"], "answer": "C"},
    
    {"question": "Which method returns length of a list?", "options": ["A. length()", "B. size()", "C. len()", "D. count()"], "answer": "C"},
    {"question": "Which function returns type of variable?", "options": ["A. type()", "B. class()", "C. var_type()", "D. typeof()"], "answer": "A"},
    {"question": "Which method converts string to lowercase?", "options": ["A. lower()", "B. down()", "C. small()", "D. lower_case()"], "answer": "A"},
    {"question": "Which method converts string to uppercase?", "options": ["A. upper()", "B. up()", "C. capitalize()", "D. big()"], "answer": "A"},
    {"question": "Which keyword is used to import modules?", "options": ["A. include", "B. import", "C. require", "D. module"], "answer": "B"},
    {"question": "Which function returns random number?", "options": ["A. random()", "B. randint()", "C. rand()", "D. choice()"], "answer": "B"},
    {"question": "Which keyword is used to define class?", "options": ["A. class", "B. def", "C. object", "D. module"], "answer": "A"},
    {"question": "Which function converts integer to string?", "options": ["A. str()", "B. int()", "C. float()", "D. bool()"], "answer": "A"},
    {"question": "Which method joins list of strings?", "options": ["A. join()", "B. concat()", "C. merge()", "D. combine()"], "answer": "A"},
    {"question": "Which keyword is used to create anonymous function?", "options": ["A. lambda", "B. def", "C. func", "D. anonymous"], "answer": "A"},
    
    {"question": "Which keyword is used to define constant in Python?", "options": ["A. const", "B. final", "C. No keyword", "D. constant"], "answer": "C"},
    {"question": "Which method splits string by delimiter?", "options": ["A. cut()", "B. split()", "C. divide()", "D. separate()"], "answer": "B"},
    {"question": "Which symbol is used for logical AND?", "options": ["A. &&", "B. and", "C. &", "D. AND"], "answer": "B"},
    {"question": "Which symbol is used for logical OR?", "options": ["A. ||", "B. or", "C. |", "D. OR"], "answer": "B"},
    {"question": "Which method removes whitespace from string ends?", "options": ["A. strip()", "B. trim()", "C. clean()", "D. remove()"], "answer": "A"},
    {"question": "Which operator is used to compare equality?", "options": ["A. =", "B. ==", "C. !=", "D. ==="], "answer": "B"},
    {"question": "Which keyword is used for conditional statements?", "options": ["A. if", "B. when", "C. switch", "D. case"], "answer": "A"},
    {"question": "Which function returns absolute value?", "options": ["A. abs()", "B. absolute()", "C. mod()", "D. fabs()"], "answer": "A"},
    {"question": "Which function rounds number to nearest integer?", "options": ["A. round()", "B. ceil()", "C. floor()", "D. approx()"], "answer": "A"},
    {"question": "Which module is used for regular expressions?", "options": ["A. re", "B. regex", "C. pattern", "D. match"], "answer": "A"},
    {"question": "Which keyword is used to exit loop?", "options": ["A. exit", "B. break", "C. stop", "D. quit"], "answer": "B"},
    {"question": "Which keyword skips current iteration in loop?", "options": ["A. skip", "B. continue", "C. pass", "D. next"], "answer": "B"},
    {"question": "Which data type is immutable?", "options": ["A. list", "B. tuple", "C. dict", "D. set"], "answer": "B"},
    {"question": "Which data type allows key-value pairs?", "options": ["A. list", "B. tuple", "C. dict", "D. set"], "answer": "C"},
    {"question": "Which method adds key-value pair to dictionary?", "options": ["A. add()", "B. insert()", "C. update()", "D. append()"], "answer": "C"},
    {"question": "Which keyword is used to ignore code block?", "options": ["A. skip", "B. pass", "C. ignore", "D. null"], "answer": "B"},
    {"question": "Which function reads input from user?", "options": ["A. input()", "B. read()", "C. scan()", "D. get()"], "answer": "A"},
    {"question": "Which function returns type of variable?", "options": ["A. typeof()", "B. type()", "C. class()", "D. var_type()"], "answer": "B"},
    {"question": "Which function generates random float between 0 and 1?", "options": ["A. random()", "B. randint()", "C. uniform()", "D. rand()"], "answer": "A"},
    {"question": "Which method capitalizes first letter of string?", "options": ["A. capitalize()", "B. upper()", "C. title()", "D. cap()"], "answer": "A"},
    {"question": "Which operator is used for not equal?", "options": ["A. !=", "B. <>", "C. =!", "D. =="], "answer": "A"},
    {"question": "Which keyword is used to define infinite loop?", "options": ["A. while True", "B. loop forever", "C. repeat", "D. infinite"], "answer": "A"},
]

# ------------------------
# Game Logic
# ------------------------
total_questions = len(questions)

for i in range(0, total_questions, questions_per_round):
    print(f"\n--- Round {round_number} ---")
    round_score = 0
    round_questions = questions[i:i+questions_per_round]

    for q in round_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"].upper():
            print("Correct!")
            score += 1
            round_score += 1
        else:
            print("Wrong! Correct answer is:", q["answer"])
    
    print(f"\nRound {round_number} Summary: You got {round_score} correct and {len(round_questions)-round_score} wrong.")
    round_number += 1

print("\nYour final score is:", score, "/", total_questions)
print("Thanks for playing!")


