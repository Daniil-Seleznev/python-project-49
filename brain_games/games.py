from random import choice
from brain_games.utils import (random_number,
                               get_answer_of_expression, is_even,
                               get_gcd, rand_arithmetic_progression,
                               is_prime)
from brain_games.engine import game_engine

QUESTIONS_COUNT = 3


def even_game() -> None:
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = [random_number() for _ in range(QUESTIONS_COUNT)]
    answers = [is_even(number) for number in questions]
    game_engine(rules, questions, answers)


def calc_game() -> None:
    rules = 'What is the result of the expression?'
    expressions = [(random_number(), choice(["+", "-", "*"]), random_number())
                   for _ in range(QUESTIONS_COUNT)]
    questions = [f'{number1} {operation} {number2}'
                 for number1, operation, number2 in expressions]
    answers = [get_answer_of_expression(number1, number2, operation)
               for number1, operation, number2 in expressions]
    game_engine(rules, questions, answers)


def gcd_game() -> None:
    rules = 'Find the greatest common divisor of given numbers.'
    numbers_pairs = [(random_number(), random_number())
                     for _ in range(QUESTIONS_COUNT)]
    questions = [f'{number1} {number2}' for number1, number2 in numbers_pairs]
    answers = [get_gcd(*question) for question in numbers_pairs]
    game_engine(rules, questions, answers)


def progression_game() -> None:
    rules = 'What number is missing in the progression?'
    progressions = [rand_arithmetic_progression()
                    for _ in range(QUESTIONS_COUNT)]
    questions = [' '.join(progression) for progression, _ in progressions]
    answers = [right_answer for _, right_answer in progressions]
    game_engine(rules, questions, answers)


def prime_game() -> None:
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = [random_number() for _ in range(QUESTIONS_COUNT)]
    answers = [is_prime(number) for number in questions]
    game_engine(rules, questions, answers)
