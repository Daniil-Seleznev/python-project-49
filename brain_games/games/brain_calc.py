from random import randint, choice


def get_answer_of_expression(number1: int, number2: int, operation: str) -> str:
    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    else:
        return str(number1 * number2)


def calc_game() -> tuple[str, str]:
    number1, operation, number2 = (randint(1, 100), choice(["+", "-", "*"]),
                                   randint(1, 100))
    question = f'{number1} {operation} {number2}'
    answer = get_answer_of_expression(number1, number2, operation)
    return question, answer
