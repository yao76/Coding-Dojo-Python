import unittest

def reverseList(list):
    return list[::-1]

def palindrome(pal):
    reversed = pal[::-1]
    if pal == reversed:
        return True
    else:
        return False
def coin(amount):
    coins = [25,10,5,1]
    coins_returned = []
    for coin in coins:
        holdingAmount = amount
        amount = amount//coin
        coins_returned.append(amount)
        amount = holdingAmount%coin
    return coins_returned
    #print(f"coins returned:{coins_returned}")


    

class IsReversedList(unittest.TestCase):
    def testreversedlist(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
        self.assertEqual( reverseList([1,3,5]), [5,3,1] )
        self.assertEqual( reverseList([51,31,15]), [15,31,51] )
        self.assertEqual( reverseList([11,33,55]), [55,33,11] )
        self.assertEqual( reverseList([2,2,5]), [5,2,2] )
    
    def testispallindrone(self):
        self.assertTrue(palindrome("ava"))
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("abccba"))
        self.assertFalse(palindrome("abca"))
        self.assertFalse(palindrome("rabcr"))
        self.assertFalse(palindrome("abcdee"))
        self.assertTrue(palindrome("abcdeeeedcba"))

    def testcoin(self):
        self.assertEqual( coin(87), [3,1,0,2] )
        self.assertEqual( coin(88), [3,1,0,3] )
        self.assertEqual( coin(100), [4,0,0,0] )
        self.assertEqual( coin(24), [0,2,0,4] )
        self.assertEqual( coin(26), [1,0,0,1] )
        self.assertEqual( coin(6), [0,0,1,1] )

        # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests