"""special questions for even game"""

from brain_games.engine import get_random_number


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


"""Calculate if number is even"""


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    if random_number % 2 > 0:
        return False


"""Information for the round"""


def round_inputs():
    random_number = get_random_number()
    question = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer
