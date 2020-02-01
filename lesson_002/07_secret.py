#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
# Должна получиться фраза на русском языке, например: как два байта переслать.

# Ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Подсказки:
#   В каждом элементе списка защифровано одно слово.
#   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
#   Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

line1 = secret_message[0][3]
line2=secret_message[1][9:13]
line3=secret_message[2][5:15:2]
line4_1= secret_message[3][7:13]
line4= line4_1[::-1]
line5_1=secret_message[4][16:21]
line5= line5_1[::-1]
# TODO 1) Эти переменны содержат слова, а не линии, поэтому лучше назвать их "слово_1"  и т.д.
#  2) secret_message[3][7:13][::-1] тут нужен один слайс, у вас два, один вырезает нужное слово,
#  а второй переворачивает его. То есть -1, надо переместить в первый слайс третьим параметром
#  2) для слайсов у которых срез в обратном порядке (то есть третий параметр отрицательный) указатели
#  (первые два параметра) меняются местами. Дополнительный материал https://issue.life/questions/509211
#  Особенное внимание обратите на это:
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  <------- вот как "работают" параметры start и stop в слайсе, срез берёт то, что между ними
# -6  -5  -4  -3  -2  -1

print(line1+ ' ' + line2+ ' ' + line3+ ' '+ line4+ ' '+ line5)
# TODO print по-умолчанию вставляет пробелы между аргументами (параметрами), поэтому можно просто перечислить в нём
#  переменные
