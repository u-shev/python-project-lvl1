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
     for i in range(MIN_NUMBER_OF_TERMS, MAX_NUMBER_OF_TERMS):
         member_of_progression += common_difference
         progression.append(member_of_progression)
     return progression


"""changing int into a str and searching missing number"""
def make_string_progression(progression, missing_number):
    string_progression = []
    for index in range (0, len(progression) - 1):
       string_progression.append(str(progression[index]))
    string_progression[missing_number] = '..'
    return " ".join(string_progression)


def round_inputs():
    initial_term = randint(MIN_NUMBER, MAX_NUMBER)
    common_difference = randint(MIN_NUMBER, MAX_NUMBER)
    progression = make_progression(initial_term, common_difference)
    missing_number = randint(0, len(progression))
    question = make_string_progression(progression, missing_number)
    correct_answer = str(progression[missing_number])
    return question, correct_answer
