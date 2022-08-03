#!/usr/bin/env python3
"""Calculator game"""


from brain_games.run_game1 import run_game
from brain_games.games.calc import calc


def main():
    run_game(calc)


if __name__ == '__main__':
    main()
