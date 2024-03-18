from brain_games.engine import game_engine
from brain_games.games.brain_gcd import gcd_game

rules = 'Find the greatest common divisor of given numbers.'


def main() -> None:
    game_engine(gcd_game, rules)


if __name__ == '__main__':
    main()
