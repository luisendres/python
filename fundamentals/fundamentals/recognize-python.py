num1 = 42   #- variable declaration, initialize Number
num2 = 2.3  #- variable declaration, initialize Number
boolean = True  #- variable declaration, initialize Boolean
string = 'Hello World' #- variable declaration, initialize String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #- variable declaration, initialize List, initialize String
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #- variable declaration, initialize Dictionary 
fruit = ('blueberry', 'strawberry', 'banana')   #- variable declaration, initialize Tuples 
print(type(fruit))  #- log statement, type check, access Tuple value
print(pizza_toppings[1])    #- log statement, access List value
pizza_toppings.append('Mushrooms') #- List add value, add List value 
print(person['name'])   #- log statement, access Dictionary value
person['name'] = 'George'   #- access Dictionary value, change Dictionary value
person['eye_color'] = 'blue'     #- access Dictionary value, change Dictionary value
print(fruit[2]) #- log statement

if num1 > 45:
    print("It's greater")   #- log statement
else:
    print("It's lower") #- log statement

if len(string) < 5:
    print("It's a short word!") #- log statement
elif len(string) > 15:
    print("It's a long word!")   #- log statement
else:
    print("Just right!")     #- log statement

for x in range(5):
    print(x)     #- log statement
for x in range(2,5):
    print(x)     #- log statement
for x in range(2,10,3):
    print(x)     #- log statement
x = 0
while(x < 5):
    print(x)     #- log statement
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)    #- log statement
person.pop('eye_color')
print(person)    #- log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')  #- log statement
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')   #- log statement

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')   #- log statement

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')   #- log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)