"""special questions for calculator game"""

from random import choice, randint


FIRST_RANDOM_NUMBER = 1
LAST_RANDOM_NUMBER = 100
RULES = 'What is the result of the expression?'


def get_round_inputs():
    operation = choice('+-*')
    random_number1 = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    random_number2 = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    question = f'{random_number1} {operation} {random_number2}'
    correct_answer = ''
    if operation == '+':
        correct_answer = str(random_number1 + random_number2)
    elif operation == '-':
        correct_answer = str(random_number1 - random_number2)
    elif operation == '*':
        correct_answer = str(random_number1 * random_number2)
    return question, correct_answer
