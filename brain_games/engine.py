from brain_games.cli import welcome_user
from brain_games.scripts.main import greeting
from brain_games.utils import answer_try


def game_engine(rules: str, questions: list, answers: list) -> None:
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
