import unittest

def sortString(s):
    temps = list(s)
    temps.sort()
    return "".join(temps)

def isUnique(s):
    s = sortString(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

def isUnique2(s):
    charMap = [False for i in range(128)]
    for chrS in s:
        if charMap[ord(chrS)]:
            return False
        charMap[ord(chrS)] = True
    return True

class TestisUnique(unittest.TestCase):
    def driver(self, s, expected):
        self.assertEqual(isUnique(s), expected)
        self.assertEqual(isUnique2(s), expected)

    def testIsUnique(self):
        self.driver("rishi", False)
        self.driver("maker", True)
        self.driver("patanjali", False)
        self.driver("a", True)
        self.driver("hoo", False)
        self.driver("baker", True)


if __name__ == "__main__":
    unittest.main()
