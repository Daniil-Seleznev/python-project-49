from random import randint, choice
from brain_games.utils import answer_try

retry_count = 3


def even_game(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(retry_count):
        number = randint(1, 100)
        right_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        if not answer_try(right_answer):
            break
    else:
        print(f'Congratulations!, {name}!')


def calc_game(name: str) -> None:
    print('What is the result of the expression?')
    for _ in range(retry_count):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operation = choice(['+', '-', '*'])
        print(f'Question: {number1} {operation} {number2}')
        if operation == '+':
            right_answer = str(number1 + number2)
        elif operation == '-':
            right_answer = str(number1 - number2)
        else:
            right_answer = str(number1 * number2)

        if not answer_try(right_answer):
            break
    else:
        print(f'Congratulations!, {name}!')