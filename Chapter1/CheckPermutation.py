import unittest

def CheckPermutation(baseStr, checkStr):
    if len(baseStr) != len(checkStr):
        return False
    mapSet = [0 for i in range(128)]
    for c in baseStr:
        mapSet[ord(c)] += 1
    for c in checkStr:
        if mapSet[ord(c)] == 0:
            return False
        mapSet[ord(c)] -= 1
    return True

class TestCheckPermutation(unittest.TestCase):
    def driver(self, baseStr, checkStr, expected):
        result = CheckPermutation(baseStr, checkStr)
        self.assertEqual(result, expected)
    def testCheckPermutation(self):
        self.driver("rishi", "rosjo", False)
        self.driver("rishi", "ishir", True)
        self.driver("a", "aa", False)
        self.driver("aa", "a", False)
        self.driver("a","a", True)

if __name__ == "__main__":
    unittest.main()
