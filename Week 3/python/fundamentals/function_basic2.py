#1 Countdown
def countdown(num):
    return list(range(num,-1,-1))

print(countdown(5))

#2 Print and return
def printandreturn(a_list):
    print(a_list[0])
    return a_list[1]

printandreturn([1,2])

#3 First Plus Length
def firstpluslength(a_list):
    return a_list[0] + len(a_list)

print(firstpluslength([1,3,5]))

#4 Values Greater than Second
def values_greater_than_second(a_list):
    new_list = []
    if len(a_list)<2:
        return False
    for x in range(0, len(a_list), 1):
        if a_list[x] > a_list[1]:
            new_list.append(a_list[x])
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5 This Length, That Value
def length_and_value(length, value):
    result = []
    for x in range(length):
        result.append(value)
    return result

print(length_and_value(4,5))
print(length_and_value(6,2))