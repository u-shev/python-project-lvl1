"""special questions for gcd game"""
from random import randint
from math import gcd


FIRST_RANDOM_NUMBER = 1
LAST_RANDOM_NUMBER = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_round_inputs():
    random_number1 = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    random_number2 = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    correct_answer = str(gcd(random_number1, random_number2))
    question = f'{random_number1} {random_number2}'
    return question, correct_answer
