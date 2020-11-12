import unittest

"""
Pay attention to the naming conventions for test classes and
functions. The unittest library relies on them.
"""


class TestTest(unittest.TestCase):
    def test_sample(self):
        """ Sample Test Case """
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
