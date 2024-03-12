from brain_games.scripts.games.brain_calc import random_number
from brain_games.engine import game_engine


def get_gcd(a: int, b: int) -> str:
    while b:
        a, b = b, a % b
    return a


def gcd_game(answer_count: int) -> tuple[str, list[str], list[str]]:
    rules = 'Find the greatest common divisor of given numbers.'
    numbers_pairs = [(random_number(), random_number())
                     for _ in range(answer_count)]
    questions = [f'{number1} {number2}' for number1, number2 in numbers_pairs]
    answers = [str(get_gcd(*question)) for question in numbers_pairs]
    return rules, questions, answers


def main() -> None:
    game_engine(gcd_game)


if __name__ == '__main__':
    main()
