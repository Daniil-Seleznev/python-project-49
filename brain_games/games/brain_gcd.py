from brain_games.games.brain_calc import random_number


def get_gcd(a: int, b: int) -> str:
    while b:
        a, b = b, a % b
    return a


def gcd_game() -> tuple[str, str]:
    number1, number2 = random_number(), random_number()
    question = f'{number1} {number2}'
    answer = str(get_gcd(number1, number2))
    return question, answer
