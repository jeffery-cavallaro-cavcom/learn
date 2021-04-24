import unittest

from name_utils import get_formatted_name


class NameTestCases(unittest.TestCase):
    def test_first_last(self):
        full_name = get_formatted_name("JOPLIN", "jAniS")
        self.assertEqual(full_name, "Janis Joplin")

    def test_first_middle_last(self):
        full_name = get_formatted_name("vincent", "jan", "michael")
        self.assertEqual(full_name, "Jan Michael Vincent")


if __name__ == '__main__':
    unittest.main()
