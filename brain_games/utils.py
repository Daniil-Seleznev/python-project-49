import prompt
from random import randint


def answer_try(right_answer):
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{right_answer}'.")
        return False


def even_game(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        right_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        if not answer_try(right_answer):
            break
    else:
        print(f'Congratulations!, {name}!')
