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


# def get_score(game_result):
#     allowed_symbols = ['/', 'X', '-']
#     current_pair = str()
#     score = 0
#     for symbol in game_result:
#         if not symbol.isnumeric() and symbol not in allowed_symbols:
#             raise InvalidSymbol
#         elif current_pair and symbol == 'X':
#             raise EvenNumber
#         elif symbol == 'X':
#             score += 20
#             continue
#         elif current_pair:
#             current_pair += symbol
#             if symbol == '/':
#                 score += 15
#                 current_pair = str()
#                 continue
#             for i in current_pair:
#                 if i == '-':
#                     current_pair = current_pair.replace('-', '0')
#             if int(current_pair[0]) + int(current_pair[1]) <= 9:
#                 score += int(current_pair[0]) + int(current_pair[1])
#             else:
#                 raise MoreThan10
#             current_pair = str()
#         else:
#             current_pair += symbol
#     return score
#
#
# if __name__ == "__main__":
#     import doctest
#
#     doctest.testmod()


class Logic:

    def __init__(self):
        self.allowed_symbols = ['/', 'X', '-']


class Manager(Logic):

    def bowling(self, result):
        current_pair = str()
        current_state, score = ShotOne(), 0
        for symbol in result:
            current_state, points, pair = current_state.get_score(symbol, current_pair)
            current_pair = pair
            score += points
        return score


class ShotOne(Logic):

    def get_score(self, symbol, current_pair):
        if not symbol.isnumeric() and symbol not in self.allowed_symbols:
            raise InvalidSymbol
        elif symbol == 'X':
            return ShotOne(), 20, current_pair
        else:
            current_pair += symbol
            return ShotTwo(), 0, current_pair


class ShotTwo(Logic):

    def get_score(self, symbol, current_pair):
        if current_pair and symbol == 'X':
            raise EvenNumber
        else:
            current_pair += symbol
            if symbol == '/':
                current_pair = str()
                return ShotOne(), 15, current_pair
            for i in current_pair:
                if i == '-':
                    current_pair = current_pair.replace('-', '0')
            if int(current_pair[0]) + int(current_pair[1]) <= 9:
                points = int(current_pair[0]) + int(current_pair[1])
                current_pair = str()
                return ShotOne(), points, current_pair
            else:
                raise MoreThan10
