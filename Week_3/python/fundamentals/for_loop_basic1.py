# # print all integers from 0 to 150
# for i in range(151):
#     print(i)

# # Print all the multiples of 5 from 5 to 1,000
# for i in range(5,1001,5):
#     print(i)

#  integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i%10 == 0:
        print("Coding")
    elif i%5 == 0:
        print("Coding Dojo")
    else:
        print(i)

# # Add odd integers from 0 to 500,000, and print the final sum.
# total = 0
# for num in range(0,500000):
#     if num%2 == 1:
#         total = total + num
# print(f"total: {total}")

# # Print positive numbers starting at 2018, counting down by fours.
# for i in range(2018,0,-4):
#     print(i)

# # Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# def flexcount(lowNum, highNum, mult):
#     for i in range(lowNum, highNum+1):
#         if i%mult == 0:
#             print(i)

# flexcount(2,9,3)