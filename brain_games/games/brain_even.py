from brain_games.games.brain_calc import random_number


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def even_game() -> tuple[int, str]:
    question = random_number()
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
