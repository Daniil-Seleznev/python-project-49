from brain_games.cli import welcome_user
from brain_games.scripts.main import greeting
import prompt

QUESTIONS_COUNT = 3


def answer_try(right_answer: str) -> bool:
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{right_answer}'.")
        return False


def game_engine(game: callable) -> None:
    rules, questions, answers = game(QUESTIONS_COUNT)
    greeting()
    name = welcome_user()
    print(rules)
    for question, right_answer in zip(questions, answers):
        print(f'Question: {question}')
        if not answer_try(right_answer):
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
