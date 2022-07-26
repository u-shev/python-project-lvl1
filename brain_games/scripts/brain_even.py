import prompt
def welcome_user1():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name

from random import randint
def even_number():
    name = welcome_user1()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    incorrect_answers = 0
    while correct_answers < 3 or incorrect_answers > 0:
        if correct_answers == 3:
            print('Congratulations, ' + name + '!')
            return correct_answers
        else:
            random_number = randint(1, 100)
            print('Question:' + str(random_number))
            if random_number%2 == 0:
                right_answer = 'Yes'
            else:
                right_answer = 'No'
            answer = input('Your answer: ')
            if answer == 'yes' and random_number % 2 == 0 or answer == 'no' and random_number % 2 > 0:
                print('Correct!')
                correct_answers = correct_answers + 1
            else:
                print("'" + answer + "' is wrong answer ;(. Correct answer was " + right_answer + ".\nLet's try again, " + str(name) + "!")
                incorrect_answers = incorrect_answers + 1
even_number() 
