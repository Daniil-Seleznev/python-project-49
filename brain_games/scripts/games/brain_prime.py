from brain_games.scripts.games.brain_calc import random_number
from brain_games.engine import game_engine


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_game(answer_count: int) -> tuple[str, list[int], list[str]]:
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = [random_number() for _ in range(answer_count)]
    answers = ['yes' if is_prime(number) else 'no' for number in questions]
    return rules, questions, answers


def main() -> None:
    game_engine(prime_game)


if __name__ == '__main__':
    main()
