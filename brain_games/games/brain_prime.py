from brain_games.games.brain_calc import random_number


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_game() -> tuple[int, str]:
    question = random_number()
    answers = 'yes' if is_prime(question) else 'no'
    return question, answers
