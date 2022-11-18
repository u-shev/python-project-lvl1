"""special questions for prime game"""

from random import randint

MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

"""cheking if number is prime"""

def is_prime(number):
    """Check if number is prime or not."""
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True

"""question and correct answer"""

def tasks_inputs():
    number = randint(1, 100)
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return (question,correct_answer)
