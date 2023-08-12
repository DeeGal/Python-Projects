from Questions_for_question_prompts import Question

question_prompts = [
    "What colour are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
    "What colour are Bananas?\n(a) Teal\n(b) Violet\n(c) Yellow\n\n"
    "What colour are Strawberries?\n(a) Blue\n(b) Red\n(c) Yellow\n\n"
    "What colour are Grapes?\n(a) Purple\n(b) Orange\n(c) Teal\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    #Question(question_prompts[1], "c"),
    #Question(question_prompts[2], "b"),
    #Question(question_prompts[3], "a"),
]
def run_test(questions):

    score = 0
    for Question in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
    print("YOU GOT " + str(score) + "/" + str(len(questions)) + "CORRECT.")

run_test(questions)
