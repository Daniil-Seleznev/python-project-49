from random import randint


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def even_game() -> tuple[int, str]:
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
