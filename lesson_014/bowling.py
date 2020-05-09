# -*- coding: utf-8 -*-


class InvalidSymbol(Exception):

    def __init__(self):
        self.message = "Only numbers and '/', 'X', '-' allowed"

    def __str__(self):
        return self.message


def get_score(game_result):
    """
    bowling function
    >>> get_score('X4/34-4')
    46
    """
    score = 0
    n = 2
    for symbol in game_result:
        if symbol == 'X':
            score += 20
            game_result = game_result.replace(symbol, '')
        elif symbol == '-':
            game_result = game_result.replace(symbol, '0')
        elif not symbol.isnumeric() and symbol != '/':
            raise InvalidSymbol
    game_result = [game_result[i:i + n] for i in range(0, len(game_result), n)]
    for pair in game_result:
        if pair.isnumeric():
            score += int(pair[0]) + int(pair[1])
        elif pair[0].isnumeric() and pair[1] == '/':
            score += 15
    return score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
