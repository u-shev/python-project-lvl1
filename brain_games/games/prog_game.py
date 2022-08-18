"""special questions for progression game"""
from random import randint


MAIN_QUESTION = 'What number is missing in the progression?'


def tasks_inputs():
    start = randint(1, 10)
    step = randint(2, 5)
    progression = [str(start)]
    for _ in range(10):
        progression.append(str(start + step))
        start = start + step
    random_index = randint(0, (len(progression) - 1))
    missing_number = progression[random_index]
    progression[random_index] = str('..')
    question = ' '.join(progression)
    correct_answer = missing_number
    return question, correct_answer
