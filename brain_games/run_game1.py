"""explaining main game"""

import prompt

def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.MAIN_QUESTION)
    for _ in range(3):
        question, correct_answer = game.tasks_inputs()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was " + str(correct_answer) + ".\nLet's try again, " + name + "!")
            return
    print('Congratulations, {}!'.format(name))
