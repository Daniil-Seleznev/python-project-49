from brain_games.scripts.main import greeting
from brain_games.cli import welcome_user
from brain_games.games import gcd_game


def main() -> None:
    greeting()
    name = welcome_user()
    gcd_game(name)


if __name__ == '__main__':
    main()
