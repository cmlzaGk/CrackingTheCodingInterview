import unittest

def determineLength(inStr):
    olen = 0
    curlen = 0
    for indx in range(len(inStr)):
        curlen += 1
        if indx + 1 < len(inStr) and inStr[indx] == inStr[indx+1]:
            continue
        olen += 1 + len(str(curlen))
        curlen = 0
    return olen

def StringCompression(inStr):
    olen = determineLength(inStr)
    if olen > len(inStr):
        return inStr
    olst = [0 for i in range(olen)]
    curlen = 0
    curindex = 0
    for indx in range(len(inStr)):
        curlen += 1
        if indx + 1 < len(inStr) and inStr[indx] == inStr[indx+1]:
            continue
        olst[curindex] = inStr[indx]
        curindex += 1
        curstr = str(curlen)
        for c in curstr:
            olst[curindex] = c
            curindex += 1
        curlen = 0
    return "".join(olst)

class TestStringCompression(unittest.TestCase):
    def driver(self, inStr, expected):
        result = StringCompression(inStr)
        self.assertEqual(result, expected)
    def testCheckPermutation(self):
        self.driver("aabbbbbcccccccccccccccccccccd", "a2b5c21d1")

if __name__ == "__main__":
    unittest.main()
 
