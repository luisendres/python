# #1 ------------------------------------------------------------------------UPDATE VALUES IN DICTIONARIES AND LISTS------------------------------------------------------------------------
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.Change the value of 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]].
x[1][0] = 15
print(x)

#2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students [0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

#3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'][0])

#4.Change the value 20 in z to 30
z[0]["y"] = 30
print(z[0]["y"])

#2 ------------------------------------------------------------------------ITERATE THROUGH A LIST OF DICTIONARIES------------------------------------------------------------------------
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        for key, val in some_list[i].items():
            print(key, "-",val)
            
iterateDictionary(students)

#                                                   Another way to do it 
# def iterateDictionary(some_list):
#     for i in range(0,len(some_list)):
#         output = ""
#         for key,val in some_list[i].items():
#             output += f" {key} - {val},"
#         print(output)

# iterateDictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3 ------------------------------------------------------------------------GET VALUES FROM A LIST OF DICTIONARIES------------------------------------------------------------------------
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#                                                   Another way to do it 
# def iterateDictionary2(key_name, some_list):
#     for key,val in some_list[i].items():
#         if key == key_name:
#             print(val)


#4 ------------------------------------------------------------------------ITERATE THOUGH A DICTIONARY WITH LIST VALUES------------------------------------------------------------------------
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def printInfo(some_dict):
#     for i in some_dict:
#         print(i)
#         for j in range(0,len(some_dict[i])):
#             print(some_dict[i][j])
            
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


#                                                   Another way to do it
# def printInfo(some_dict):
#     for key, val in some_dict.items():
#         print("--------------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])
            
# printInfo(dojo)