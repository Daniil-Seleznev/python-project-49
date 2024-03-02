from random import choice
from brain_games.utils import (answer_try, random_number,
                               get_answer_of_expression, is_even,
                               get_gcd, rand_arithmetic_progression,
                               is_prime)

retry_count = 3


def even_game(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(retry_count):
        number = random_number()
        right_answer = is_even(number)
        print(f'Question: {number}')
        if not answer_try(right_answer):
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations!, {name}!')


def calc_game(name: str) -> None:
    print('What is the result of the expression?')
    for _ in range(retry_count):
        number1 = random_number()
        number2 = random_number()
        operation = choice(['+', '-', '*'])
        print(f'Question: {number1} {operation} {number2}')
        right_answer = get_answer_of_expression(number1, number2, operation)

        if not answer_try(right_answer):
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations!, {name}!')


def gcd_game(name: str) -> None:
    print('Find the greatest common divisor of given numbers.')
    for _ in range(retry_count):
        number1 = random_number()
        number2 = random_number()
        print(f'Question: {number1} {number2}')
        right_answer = get_gcd(number1, number2)
        if not answer_try(right_answer):
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations!, {name}!')


def progression_game(name: str) -> None:
    print('What number is missing in the progression?')
    for _ in range(retry_count):
        progression, right_answer = rand_arithmetic_progression()
        print(f'Question: {" ".join(map(str, progression))}')
        if not answer_try(str(right_answer)):
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations!, {name}!')


def prime_game(name: str) -> None:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(retry_count):
        number = random_number()
        right_answer = 'yes' if is_prime(number) else 'no'
        print(f'Question: {number}')
        if not answer_try(right_answer):
            print(f'Let\'s try again, {name}!')
            break
    else:
        print(f'Congratulations!, {name}!')
