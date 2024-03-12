from brain_games.scripts.games.brain_calc import random_number
from brain_games.engine import game_engine
from random import randint
from typing import Union


def rand_arithmetic_progression() -> tuple[list, str]:
    start = random_number()
    step = randint(1, 10)
    len_progression = randint(5, 10)
    progression: list[Union[int, str]] = \
        [str(start + step * i) for i in range(len_progression)]
    hidden_index = randint(0, len_progression - 1)
    right_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, right_answer


def progression_game(answer_count: int) -> tuple[str, list[str], list[str]]:
    rules = 'What number is missing in the progression?'
    progressions = [rand_arithmetic_progression()
                    for _ in range(answer_count)]
    questions = [' '.join(progression) for progression, _ in progressions]
    answers = [right_answer for _, right_answer in progressions]
    return rules, questions, answers


def main() -> None:
    game_engine(progression_game)


if __name__ == '__main__':
    main()
