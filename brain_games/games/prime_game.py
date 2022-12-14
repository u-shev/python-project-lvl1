"""special questions for prime game"""

from brain_games.engine import get_random_number


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

"""cheking if number is prime"""


def is_prime(number):
    """Check if number is prime or not."""
    if number < 2 or not number % 2:
        return False
    counter = 2
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 1
    return True


"""question and correct answer"""


def round_inputs():
    number = get_random_number()
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return (question, correct_answer)
