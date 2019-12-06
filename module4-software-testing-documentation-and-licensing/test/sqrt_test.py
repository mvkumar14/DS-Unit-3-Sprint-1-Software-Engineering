#import unittest package, and functions we want to test.
import unittest
from sqrt import sqrt, builtin_sqrt

class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square root functions"""
    def test_sqrt9(self):
        self.assertEqual(sqrt(9),3)
    def test_sqrt2(self):
        self.assertEqual(sqrt(2),builtin_sqrt(2))
    #You can also do almost equals:
    def test_sqrt2_almost(self):
        self.assertAlmostEquals(sqrt(2),1.41421356)
    def test_sqrt2_almost2(self):
        self.assertAlmostEqual(sqrt(2),1.41421356)

if __name__ == '__main__':
    unittest.main()
