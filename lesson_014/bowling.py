# -*- coding: utf-8 -*-


class InvalidSymbol(Exception):

    def __init__(self):
        self.message = "Only numbers and '/', 'X', '-' allowed"

    def __str__(self):
        return self.message


class MoreThan10(Exception):

    def __init__(self):
        self.message = "Can't be more than 10 points per frame"

    def __str__(self):
        return self.message


class EvenNumber(Exception):

    def __init__(self):
        self.message = "Can't be an odd number"

    def __str__(self):
        return self.message


def get_score(game_result):
    allowed_symbols = ['/', 'X', '-']
    current_pair = str()
    score = 0
    for symbol in game_result:
        if not symbol.isnumeric() and symbol not in allowed_symbols:
            raise InvalidSymbol
        elif current_pair and symbol == 'X':
            raise EvenNumber
        elif symbol == 'X':
            score += 20
            continue
        elif current_pair:
            current_pair += symbol
            if symbol == '/':
                score += 15
                current_pair = str()
                continue
            for i in current_pair:
                if i == '-':
                    current_pair = current_pair.replace('-', '0')
            if int(current_pair[0]) + int(current_pair[1]) <= 10:  # todo Тут на деле не должно быть более 9, так как
                                                                   #  если все кегли сбиты, то это spare - /
                score += int(current_pair[0]) + int(current_pair[1])
            else:
                raise MoreThan10
            current_pair = str()
        else:
            current_pair += symbol
    return score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
