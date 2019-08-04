import random
def randInt(min= None, max= None): # default params have to be set to None because the value of the default parameter is set at the time the function is created, not when it is called 
    if min == None and max == None:
        num = random.randrange(0,101)
    elif min != None and max != None:
        if max < min: #edge case max < min
            temp = 0
            temp = max
            max = min
            min = temp
        num = random.randrange(min,max)
    elif min == None and max != None:
        num = random.randrange(0,max)
    elif min != None and max == None:
        num = random.randrange(min,101)
    return num
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=50, max=-48))