"""special questions for even game"""

from random import randint


FIRST_RANDOM_NUMBER = 1
LAST_RANDOM_NUMBER = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


"""Calculate if number is even"""


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    else:
        return False


"""Information for the round"""


def get_round_inputs():
    random_number = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    question = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer
