#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}, 'Ronaldo', 'Rooney'
z = [ {'x': 10, 'y': 20} ]

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

#3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory[0]['soccer'] = ['Andres', 'Ronaldo', 'Rooney']
print(sports_directory[0]['soccer'])

#4 Change the value of 20 in z to 30
z[0]['y'] = 20
print(z)

#2 Iterate Through a List of Dictionaries
students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for student in students:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students) 

#3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    # for student in students:
    #     if key_name == 'first_name':
    #         print(f"first_name - {student['first_name']}")
    #     elif key_name == 'last_name':
    #         print(f"last_name - {student['last_name']}")
    for key in some_list:
        if key_name:
            print(f"{key[key_name]}")

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for k in some_dict:
        length = len(some_dict[k])
        print(f"{length} {k}".upper())
        for i in some_dict[k]:
            print(i)
    

printInfo(dojo)