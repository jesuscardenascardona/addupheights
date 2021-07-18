target = __import__("addupheights")
addupheights = target.addupheights
import unittest

class TestHeights(unittest.TestCase):
    def test_number(self):
        number = 139
        result = addupheights(number)
        self.assertEqual(result, [("Brevin Knight","Nate Robinson"),("Nate Robinson","Mike Wilks")])

if __name__ == '__main__':
    unittest.main()
