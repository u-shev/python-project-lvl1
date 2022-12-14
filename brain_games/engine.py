import prompt
from random import randint


FIRST_RANDOM_NUMBER = 1

LAST_RANDOM_NUMBER = 100

NUMBER_OF_ROUNDS = 3

"""Explaining main game"""
def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.round_inputs()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name}!")
            return
    print('Congratulations, {}!'.format(name))


"""Getting random number from range"""
def get_random_number():
    random_number = randint(FIRST_RANDOM_NUMBER, LAST_RANDOM_NUMBER)
    return random_number
