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


class Manager:
    def get_score(self, symbol):
        allowed_symbols = ['/', 'X', '-']
        score = 0
        current_pair = str()
        for symbol in symbol:
            if not symbol.isnumeric() and symbol not in allowed_symbols:
                raise InvalidSymbol
            elif current_pair and symbol == 'X':
                raise EvenNumber
            elif symbol == 'X':
                return 20
            elif current_pair:
                current_pair += symbol
                if symbol == '/':
                    score += 15
                    current_pair = str()
                    continue
                for i in current_pair:
                    if i == '-':
                        current_pair = current_pair.replace('-', '0')
                if int(current_pair[0]) + int(current_pair[1]) <= 9:
                    score += int(current_pair[0]) + int(current_pair[1])
                else:
                    raise MoreThan10
                current_pair = str()
            else:
                current_pair += symbol
        return score


class ShotOne(Manager):

    def __init__(self):
        pass


class ShotTwo(Manager):

    def __init__(self):
        pass


def bowling(result):
    current_state, score = ShotOne(), 0
    for symbol in result:
        current_state, points = current_state.get_score(symbol)
        score += points


print(bowling('X4/34-4'))
