from brain_games.engine import game_engine
from brain_games.games.brain_progression import progression_game

rules = 'What number is missing in the progression?'


def main() -> None:
    game_engine(progression_game, rules)


if __name__ == '__main__':
    main()
