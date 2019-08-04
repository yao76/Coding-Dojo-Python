import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):

        if len(nums) == 0:
            self.result = num
            return self.result
        if(len(nums)) > 0:
            for elem in nums:
                self.result = self.result + elem
            self.result = self.result + num
            return self.result
        else:
            return 0
    def subtract(self, num, *nums):
        for elem in nums:
            self.result = self.result - elem
        self.result = self.result - num
        return self.result 

class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testAdd(self):
        md = MathDojo()
        x = md.add(6,9,5)
        self.assertEqual(x, 20)
        a = MathDojo()
        y = a.add(6,9,5)
        self.assertEqual(y, 20)
        b = MathDojo()
        z = b.add(10,10,5)
        self.assertEqual(z, 25)
    def testSub(self):
        my = MathDojo()
        x = my.subtract(6,9,5)
        self.assertEqual(x, -20)
        a = MathDojo()
        y = a.subtract(10,10,5)
        self.assertEqual(y, -25)
        b = MathDojo()
        z = b.subtract(10,10,10)
        self.assertEqual(z, -30)
    def setUp(self):
        # add the setUp tasks

        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests