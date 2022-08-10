"""special questions for calculator game"""

from random import randint, choice

MAIN_QUESTION = 'What is the result of the expression?'

def tasks_inputs():
    operation = choice('+-*')
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {operation} {random_number2}'
    correct_answer = ''
    if operation == '+':
        correct_answer = str(random_number1 + random_number2)
    elif operation == '-':
        correct_answer = str(random_number1 - random_number2)
    elif operation == '*':
        correct_answer = str(random_number1 * random_number2)
    return question, correct_answer
