"""special questions for calculator game"""

from brain_games.engine import get_random_number
from random import choice


RULES = 'What is the result of the expression?'


def round_inputs():
    operation = choice('+-*')
    random_number1 = get_random_number()
    random_number2 = get_random_number()
    question = f'{random_number1} {operation} {random_number2}'
    correct_answer = ''
    if operation == '+':
        correct_answer = str(random_number1 + random_number2)
    elif operation == '-':
        correct_answer = str(random_number1 - random_number2)
    elif operation == '*':
        correct_answer = str(random_number1 * random_number2)
    return question, correct_answer
