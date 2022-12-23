"""special questions for progression game"""
from random import randint


RULES = 'What number is missing in the progression?'
MIN_NUMBER_OF_TERMS = 10
MAX_NUMBER_OF_TERMS = 20
MIN_NUMBER = 5
MAX_NUMBER = 15


"""making a progression"""


def make_progression(initial_term, common_difference):
    member_of_progression, progression = initial_term, [initial_term]
    progression_length = randint(MIN_NUMBER_OF_TERMS, MAX_NUMBER_OF_TERMS)
    for i in range(progression_length):
        member_of_progression += common_difference
        progression.append(member_of_progression)
    return progression


"""changing int into a str and searching missing number"""


def stringify_progression(progression, missing_number):
    string_progression = []
    for index in range(0, len(progression)):
        string_progression.append(str(progression[index]))
    string_progression[missing_number] = '..'
    return " ".join(string_progression)


def get_round_inputs():
    initial_term = randint(MIN_NUMBER, MAX_NUMBER)
    common_difference = randint(MIN_NUMBER, MAX_NUMBER)
    progression = make_progression(initial_term, common_difference)
    missing_number = randint(1, len(progression) - 1)
    question = stringify_progression(progression, missing_number)
    correct_answer = str(progression[missing_number])
    return question, correct_answer
