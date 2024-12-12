# python quiz game

questions = ("The following words are often found in definition sentences, exapect?",
            "THe text of the observation an explation and is based on?",
            "Writing in the text of the observation report must be based on?",
            "General statements and reported aspect are the structure of the text",
            "The section that contains an explanation of the opening or introduction to the topic that will be discussed in the observation report text is?")

options = (("A. Is","B. is","C. Which","D. That is"),
        ("A. writing","B. assessment","C. observation","D. opportunity"),
        ("A. penjelasan","B. fact","C. opinion","D. argument"),
        ("A. text procedure","B. text exposition","C. tekt anecdote","D. text reportar hasil observasi"),
        ("A. content section","B. conclusion","C. description section","D. general description"))

answer = ("C","C","B","D","A")
guesses = []
question_num = 0

for question in questions:
    print("-"*90)
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter(A, B, C, D,): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        print("Right")
    else:
        print("No")
        print(f"{answer[question_num]} is the Right answer")
    question_num += 1

print("====================================")
print("              RESULTS             ")
print("====================================")

print("answer: ", end="")

for answer in answer: 
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses: 
    print(guess, end=" ")
print()

print("Thank You Very Much")
