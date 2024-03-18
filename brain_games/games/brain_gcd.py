from random import randint


def get_gcd(a: int, b: int) -> str:
    while b:
        a, b = b, a % b
    return a


def gcd_game() -> tuple[str, str]:
    number1, number2 = randint(1, 100), randint(1, 100)
    question = f'{number1} {number2}'
    answer = str(get_gcd(number1, number2))
    return question, answer
