from prime_factor import PrimeFactors
import unittest


class PrimeFactorsTest(unittest.TestCase):

    # def test_one(self):
    #     self.assertEqual([], PrimeFactors.generate(1))

    def test_two(self):
        self.assertEqual([2], PrimeFactors.generate(2))

    def test_three(self):
        self.assertEqual([3], PrimeFactors.generate(3))

    def test_four(self):
        self.assertEqual([2,2], PrimeFactors.generate(4))

    def test_six(self):
        self.assertEqual([2,3], PrimeFactors.generate(6))

    def test_eight(self):
        self.assertEqual([2,2,2], PrimeFactors.generate(8))

    def test_nine(self):
        self.assertEqual([3,3], PrimeFactors.generate(9))

    def test_ten(self):
        self.assertEqual([2,5], PrimeFactors.generate(10))
    

if __name__ == "__main__":
    unittest.main()
