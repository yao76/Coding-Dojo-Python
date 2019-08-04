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
# create an instance:
md = MathDojo()
# to test:
#x = md.add(2).add(2,5,1).subtract(3,2).result
x = md.add(6,9,5)
#y = md.subtract(30)
#print(f"add total: {x}")	# should print 5
print(f"add total: {x}")	# should print 5
#print(f"sub total: {y}")	# should print 5
# run each of the methods a few more times and check the result!