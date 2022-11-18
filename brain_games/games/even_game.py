"""special questions for even game"""

from random import randint


MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def tasks_inputs():
    random_number = randint(1, 100)
    question = f'{random_number}'
    if random_number % 2 == 0:
        correct_answer = 'yes'
    if random_number % 2 > 0:
        correct_answer = 'no'
    return question, correct_answer
