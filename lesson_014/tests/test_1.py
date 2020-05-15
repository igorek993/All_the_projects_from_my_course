import unittest
from lesson_014.bowling import get_score, MoreThan10, EvenNumber


class Bowling(unittest.TestCase):

    def test_normal(self):
        result = get_score('X4/34-4')
        self.assertEqual(result, 46)

    def test_numbers(self):
        result = get_score('25613234')
        self.assertEqual(result, 26)

    def test_slashes(self):
        result = get_score('1/4/7/9/')
        self.assertEqual(result, 60)

    def test_strikes(self):
        result = get_score('XXXX')
        self.assertEqual(result, 80)

    def test_dashs(self):
        result = get_score('--------')
        self.assertEqual(result, 0)

    def test_even_exception(self):
        self.assertRaises(EvenNumber, get_score, '2-244X-')

    def test_more_than_ten_exception(self):
        self.assertRaises(MoreThan10, get_score, '98745987')


if __name__ == "__main__":
    unittest.main()
