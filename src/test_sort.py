import qsort as qs

def sort(numbers):
    #numbers.sort()
    qs.qsort(numbers)

import unittest
import random as rd

class test_sort(unittest.TestCase):
    small = [1,2,3,4,100,80,90,5,10,1,-100,20]
    equal= [1] *100
    equal_ref = []

    asc = [i for i in range(-500, 500)]
    desc = [i for i in range (500, -500, -1)]
    big_random =[]

    asc_ref =[]
    desc_ref =[]
    big_random_ref = []
    small_ref = []

    seed = 477929180

    @classmethod
    def setUpClass(cls):
        cls.small_ref = cls.small.copy()
        cls.small_ref.sort()

        cls.asc_ref = cls.asc.copy()
        cls.asc_ref.sort()

        cls.desc_ref = cls.desc.copy()
        cls.desc_ref.sort()

        cls.equal_ref = cls.equal.copy()
        cls.equal_ref.sort()

        rd.seed(cls.seed)
        cls.big_random = [rd.randint(-(1<<31), (1<<31)) for i in range(0,1000000)]
        cls.big_random_ref = cls.big_random.copy()
        cls.big_random_ref.sort()
        
    def test_small(self):
        sort(self.small)
        self.assertEqual(self.small, self.small_ref)

    #@unittest.skip("demonstrating skipping")        
    def test_equal(self):
        sort(self.equal)
        self.assertEqual(self.equal, self.equal_ref)

    #@unittest.skip("demonstrating skipping")
    def test_asc(self):
        sort(self.asc)
        self.assertEqual(self.asc, self.asc_ref)

    #@unittest.skip("demonstrating skipping")
    def test_desc(self):
        sort(self.desc)
        self.assertEqual(self.desc, self.desc_ref)

    #@unittest.skip("demonstrating skipping")
    def test_big(self):
        sort(self.big_random)
        self.assertEqual(self.big_random, self.big_random_ref)
    
if __name__ == '__main__':
    unittest.main()
        

