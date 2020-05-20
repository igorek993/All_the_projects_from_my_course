import unittest
from lesson_014.bowling import MoreThan10, EvenNumber, Manager, TwoSpares

game = Manager()


class Bowling(unittest.TestCase):

    def test_normal(self):
        result = game.bowling('X4/34-4')
        self.assertEqual(result, 46)

    def test_numbers(self):
        result = game.bowling('25613234')
        self.assertEqual(result, 26)

    def test_slashes(self):
        result = game.bowling('1/4/7/9/')
        self.assertEqual(result, 60)

    def test_strikes(self):
        result = game.bowling('XXXX')
        self.assertEqual(result, 80)

    def test_dashs(self):
        result = game.bowling('--------')
        self.assertEqual(result, 0)

    def test_even_exception(self):
        self.assertRaises(EvenNumber, game.bowling, '2-244X-')

    def test_even_exception_2(self):
        self.assertRaises(EvenNumber, game.bowling, '25412')

    def test_more_than_ten_exception(self):
        self.assertRaises(MoreThan10, game.bowling, '98745987')

    def test_spare(self):
        self.assertRaises(TwoSpares, game.bowling, '//////')


if __name__ == "__main__":
    unittest.main()
