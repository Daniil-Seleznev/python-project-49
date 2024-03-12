from brain_games.scripts.games.brain_calc import random_number
from brain_games.engine import game_engine, QUESTIONS_COUNT


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def even_game(answer_count: int) -> tuple[str, list[int], list[str]]:
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = [random_number() for _ in range(answer_count)]
    answers = ['yes' if is_even(number) else 'no' for number in questions]
    return rules, questions, answers


def main() -> None:
    game_engine(*even_game(QUESTIONS_COUNT))


if __name__ == '__main__':
    main()
