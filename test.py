import unittest
from main import Converter, Conversion

class Test(unittest.TestCase):
    def test_name(self):
        name = "m_to_cm"
        ratio = 100

        c = Conversion(name, ratio)

        self.assertEqual(c.name, name)

    def test_ratio(self):
        name = "m_to_cm"
        ratio = 100
        c = Conversion(name, ratio)

        self.assertEqual(c.ratio, ratio)

    def test_name_cannot_be_empty(self):
        name = ""
        ratio = 100

        self.assertRaises(Exception, Conversion, name, ratio)

if __name__ == "__main__":
    unittest.main()
