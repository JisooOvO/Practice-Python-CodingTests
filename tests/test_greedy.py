import unittest

from src.greedy import (coin_split,
                        law_of_large_numbers,
                        count_with_three_in_time,
                        k_knight)


class TestGreedy(unittest.TestCase):
    def test_coin_split(self):
        self.assertEqual(coin_split(total_value=1260), 6)
        self.assertEqual(coin_split(total_value=660), 4)

    def test_law_of_large_numbers(self):
        self.assertEqual(law_of_large_numbers((5,8,3),[2,4,5,4,6]),46)
        self.assertEqual(law_of_large_numbers((5,3,3),[2,4,5,4,6]),18)

    def test_count_with_three_in_time(self):
        self.assertEqual(count_with_three_in_time(5),11475)

    def test_k_knight(self):
        self.assertEqual(k_knight("a1"),2)