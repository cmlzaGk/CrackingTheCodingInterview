from math import ceil
import random
import unittest

def _merge_sort(a, start, end, b):
    if end <= start:
        return
    mid = start + int(ceil((end-start)/2.0))
    _merge_sort(a, start, mid-1, b)
    _merge_sort(a, mid, end, b)
    index1=start
    index2=mid
    indexb=start
    while index1 <= (mid-1) and index2 <= end:
        if a[index1] < a[index2]:
            b[indexb] = a[index1]
            index1 += 1
        else:
            b[indexb] = a[index2]
            index2 += 1
        indexb += 1
    for i in range(index1, mid):
        b[indexb] = a[i]
        indexb += 1
    for i in range(index2, end+1):
        b[indexb] = a[i]
        indexb += 1
    for i in range(start, end+1):
        a[i] = b[i]
    return

def merge_sort(a):
    b = [0 for x in a]
    _merge_sort(a,0,len(a)-1,b)

def _qsort(a, start, end):
    if end <= start:
        return
    pivot = end
    for i in range(start, end):
        if a[i] < a[end] and pivot != end:
            a[i], a[pivot] = a[pivot], a[i]
            pivot += 1
        elif a[i] >= a[end] and pivot == end:
            pivot = i
    a[pivot], a[end] = a[end], a[pivot]
    _qsort(a, start, pivot-1)
    _qsort(a, pivot+1, end)
    return

def qsort(a):
    _qsort(a, 0, len(a)-1)

class Tests(unittest.TestCase):
    def sort_helper(self, func):
        for i in range(100):
            len=random.randint(0,100)
            a = [random.randint(0,100) for i in range(len)]
            b = a[:]
            b.sort()
            func(a)
            self.assertEqual(b,a)
    def test_mergesort(self):
            self.sort_helper(merge_sort)
    def test_qsort(self):
            self.sort_helper(qsort)

if __name__ == '__main__':
    unittest.main()

