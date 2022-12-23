import prompt


NUMBER_OF_ROUNDS = 3


"""Explaining main game"""


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_round_inputs()
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
