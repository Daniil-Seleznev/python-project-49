from brain_games.engine import game_engine
from brain_games.games.brain_prime import prime_game

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main() -> None:
    game_engine(prime_game, rules)


if __name__ == '__main__':
    main()
