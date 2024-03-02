import prompt
from random import randint


def answer_try(right_answer: str) -> bool:
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{right_answer}'.")
        return False


def random_number() -> int:
    return randint(1, 100)


def get_answer_of_expression(number1: int, number2: int, operation: str) -> str:
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    else:
        return str(number1 * number2)


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_gcd(a: int, b: int) -> str:
    while b:
        a, b = b, a % b
    return str(a)
