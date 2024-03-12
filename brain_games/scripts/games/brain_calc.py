from random import randint, choice
from brain_games.engine import game_engine


def random_number() -> int:
    return randint(1, 100)


def get_answer_of_expression(number1: int, number2: int, operation: str) -> str:
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    else:
        return str(number1 * number2)


def calc_game(answer_count) -> tuple[str, list[str], list[str]]:
    rules = 'What is the result of the expression?'
    expressions = [(random_number(), choice(["+", "-", "*"]), random_number())
                   for _ in range(answer_count)]
    questions = [f'{number1} {operation} {number2}'
                 for number1, operation, number2 in expressions]
    answers = [get_answer_of_expression(number1, number2, operation)
               for number1, operation, number2 in expressions]
    return rules, questions, answers


def main() -> None:
    game_engine(calc_game)


if __name__ == '__main__':
    main()
