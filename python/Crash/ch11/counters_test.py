import unittest

from counters import Counters


class CountersTestCase(unittest.TestCase):
    def setUp(self):
        self.counters = Counters()

    def test_empty(self):
        self.assertEqual(self.counters.number, 0)
        self.assertEqual(self.counters.count("zero"), 0)

    def test_one(self):
        self.counters.increment("one")
        self.assertEqual(self.counters.number, 1)
        self.assertEqual(self.counters.count("one"), 1)

    def test_two(self):
        self.counters.increment("two")
        self.counters.increment("two")
        self.assertEqual(self.counters.number, 1)
        self.assertEqual(self.counters.count("two"), 2)

    def test_multiple(self):
        self.counters.increment("one")
        self.counters.increment("two")
        self.counters.increment("two")
        self.assertEqual(self.counters.number, 2)
        self.assertEqual(self.counters.count("zero"), 0)
        self.assertEqual(self.counters.count("one"), 1)
        self.assertEqual(self.counters.count("two"), 2)


if __name__ == '__main__':
    unittest.main()
