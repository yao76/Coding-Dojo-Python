# 1 Biggie Size
def biggie_size(num_list):
    for i in range(0, len(num_list)):
        if num_list[i] < 0:
            num_list[i] = "big"
    return(num_list)


print(biggie_size([-1, 2, 3, -4]))

# 2 Count Positives


def count_positives(num_list):
    count = 0
    for num in num_list:
        if num > 0:
            count += 1
    num_list[-1] = count
    return(num_list)


print(count_positives([-1, 1, 1, 1]))

# 3 Sum Total


def sum_total(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum


print(sum_total([1, 2, 3, 4]))

# 4 Average


def average(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum/len(num_list)


print(average([1, 2, 3, 4]))

# 5 Length


def length(num_list):
    return len(num_list)


print(length([37, 2, 1, -9]))
print(length([]))

#6 Minimum
def minimum(num_list):
    if len(num_list) == 0:
        return False
    else:
        min = num_list[0]
        for num in num_list:
            if num < min:
                min = num
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

#7 Maximum
def maximum(num_list):
    if len(num_list) == 0:
        return False
    else:
        max = num_list[0]
        for num in num_list:
            if num > max:
                max = num
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

#8 Ultimate Analysis
def ultimate_analysis(num_list):
    result = {
        'sumTotal': None,
        'average': None,
        'minimum': None,
        'maximum': None,
        'length': None,
                }
    sum = 0
    average = 0
    min = num_list[0]
    max = num_list[0]

    for num in num_list: #sum
        sum += num
    result['sumTotal'] = sum

    average = sum/len(num_list) #average
    result['average'] = average

    if len(num_list) == 0: #minimum and maximum
        return False
    else:
        for num in num_list:
            if num < min:
                min = num
            if num > max:
                max = num
    
    result['minimum'] = min
    result['maximum'] = max
    result['length'] = len(num_list)

    return(result)
    
print(ultimate_analysis([37,2,1,-9,-10,-10,38,38]))


#9 Reverse list
def reverse_list(num_list):
    return num_list[::-1]
print(reverse_list([37,2,1,-9]))