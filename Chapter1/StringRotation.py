import unittest

def StringRotation(s1, s2):
    if len(s2) != len(s1):
        return False
    s = s1 + s1
    if -1 == s.find(s2):
        return False
    return True

class TestStringRotation(unittest.TestCase):
    def driver(self, baseStr, checkStr, expected):
        result = StringRotation(baseStr, checkStr)
        self.assertEqual(result, expected)
    def test_StringRotation(self):
        self.driver("rishi", "ishir", True)
        self.driver("rishi", "ishi", False)
        self.driver("rishi", "hiris", True)
        self.driver("rishi", "hiriy", False)

if __name__ == "__main__":
    unittest.main()


