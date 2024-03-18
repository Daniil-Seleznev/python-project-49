from brain_games.engine import game_engine
from brain_games.games.brain_calc import calc_game

rules = 'What is the result of the expression?'


def main() -> None:
    game_engine(calc_game, rules)


if __name__ == '__main__':
    main()
