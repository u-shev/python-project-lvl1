"""special questions for gcd game"""
from brain_games.engine import get_random_number
from math import gcd


RULES  = 'Find the greatest common divisor of given numbers.'


def round_inputs():
    random_number1 = get_random_number()
    random_number2 = get_random_number()
    correct_answer = str(gcd(random_number1, random_number2))
    question = f'{random_number1} {random_number2}'
    return question, correct_answer
