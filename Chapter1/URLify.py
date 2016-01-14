import unittest

def DetectLen(lstr, lenInput):
    lenOutput = 0
    for i in range(lenInput):
        if lstr[i] == ' ':
            lenOutput += 3
        else:
            lenOutput += 1
    return lenOutput


def URLify(lstr, lenInput):
    lenOutput = DetectLen(lstr, lenInput) - 1
    for i in range(lenInput-1,-1,-1):
        if lstr[i] == ' ':
            lstr[lenOutput] = '0'
            lstr[lenOutput-1] = '2'
            lstr[lenOutput-2] = '%'
            lenOutput -= 3
        else:
            lstr[lenOutput] = lstr[i]
            lenOutput -= 1

class TestURLify(unittest.TestCase):
    def driver(self, inStr, lenInput, expected):
        lstr = list(inStr)
        URLify(lstr, lenInput)
        result = "".join(lstr)
        self.assertEqual(result, expected)

    def test_URLify(self):
        self.driver("Mr. and Mrs. Smith      ",  18, "Mr.%20and%20Mrs.%20Smith")

if __name__ == "__main__":
    unittest.main()
