#!/usr/bin/env python3
"""Calculator game"""


from brain_games.engine import run
from brain_games.games import calc_game


def main():
    run(calc_game)


if __name__ == '__main__':
    main()
