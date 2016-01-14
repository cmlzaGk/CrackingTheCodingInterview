import unittest

def oneAway(firstStr, secondStr):
    if len(firstStr) < len(secondStr):
        firstStr, secondStr = secondStr, firstStr
    if len(firstStr) - len(secondStr) >= 2:
        return 2
    for indx in range(len(firstStr)):
        if indx >= len(secondStr):
            return 1
        if firstStr[indx] != secondStr[indx]:
            if firstStr[indx:] == secondStr[indx+1:]:
                return 1
            if firstStr[indx+1:] == secondStr[indx:]:
                return 1
            if firstStr[indx+1:] == secondStr[indx+1:]:
                return 1
            return 2
    return 0

class TestOneAway(unittest.TestCase):
    def driver(self, firstStr, secondStr, expected):
        result = oneAway(firstStr, secondStr)
        self.assertEqual(result, expected)
    def test_OneAway(self):
        self.driver("pale", "ple", 1)
        self.driver("pale", "pales", 1)
        self.driver("pale", "bale", 1)
        self.driver("pale", "bake", 2)
        self.driver("pale", "pale", 0)

if __name__ == "__main__":
    unittest.main()
