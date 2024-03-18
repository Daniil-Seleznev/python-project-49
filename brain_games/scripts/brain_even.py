from brain_games.engine import game_engine
from brain_games.games.brain_even import even_game

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def main() -> None:
    game_engine(even_game, rules)


if __name__ == '__main__':
    main()
