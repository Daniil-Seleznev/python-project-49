from brain_games.games.brain_calc import random_number
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


def progression_game() -> tuple[str, str]:
    progression, answer = rand_arithmetic_progression()
    question = ' '.join(progression)
    return question, answer
