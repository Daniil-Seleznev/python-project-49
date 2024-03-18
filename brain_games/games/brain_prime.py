from random import randint


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_game() -> tuple[int, str]:
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
