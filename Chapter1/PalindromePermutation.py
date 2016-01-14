import unittest

def PalindromePermutation(inStr):
    mapList = [0 for i in range(128)]
    for c in inStr:
        mapList[ord(c)] += 1
    oddPresent = False
    for charCounter in mapList:
        if charCounter % 2 != 0:
            if oddPresent:
                return False
            oddPresent = True
    return True

def GetIntValue(c):
    if ord(c) < ord('a') or  ord(c) > ord('z'):
        raise Exception("Invalied Input")
    return ord(c) % 26

def PalindromePermutation2(inStr):
    mapInt = 0x0
    for c in inStr:
        ordC = GetIntValue(c)
        bitC = 1 << ordC
        mapInt = (mapInt ^ bitC) & 0xFFFFFFFF
    if mapInt == 0 or (mapInt & (mapInt - 1) == 0):
        return True
    return False

class TestPalindromePermutation(unittest.TestCase):
    def driver(self, inStr, expected):
        result = PalindromePermutation(inStr)
        self.assertEqual(result, expected)
        result = PalindromePermutation2(inStr)
        self.assertEqual(result, expected)

    def testCheckPermutation(self):
        self.driver("rishi", False)
        self.driver("tactcoa", True)

if __name__ == "__main__":
    unittest.main()
