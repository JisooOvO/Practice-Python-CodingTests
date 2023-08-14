import unittest
from lib.greedy import coin_split

class TestGreedy(unittest.TestCase):

    def test_coin__split(self) :
        self.assertEqual(coin_split(total_value=1260),6)
        self.assertEqual(coin_split(total_value=660),4)

    #def test_law_of_large_numbers(self) :
    #    self.assertEqual(self.law_of_large_numbers(((5,8,3),(2,4,5,4,6)), 46))

#if __name__ == "__main__" :
#    unittest.main()
