import unittest


class MathTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 3, 5)

    def test_sub(self):
        self.assertEqual(5 - 3, 2)

    def test_sub2(self):
        self.assertEqual(5 - 1, 2)


if __name__ == '__main__':
    unittest.main()
