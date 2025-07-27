# Author: Somya Jain
# Demonstration of Python Datatypes, Operations, and Core Concepts

# =========================================
# Variable Declaration 
# =========================================

MyName = "somya"  #Pascal way
myName = "somya"  #camel way
My_name = "somya" #snake way

# =========================================
# Data Type
# =========================================
# Datatype : string , int, float , Boolean 
# strings
"""
name = "somya"
print(name)
print("Hello" + " " + name)

#int
a = 10
a = a+1
print(a)
print(type(a))
print("age is" + " " + str(a)) # typecasting

#Float
a = 2.45
print(a)

#Boolean
girl = True
print("you are a girl :" + " " + str(girl))

# Mutliple assignment
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

"""

# =========================================
# String Methods
# =========================================
"""
a = "somya"
print(len(a))
print(a.find("o"))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.isdigit())
print(a.isalpha())
print(a.count("s"))
print(a.replace("s" , "S"))
print(a*3)

"""
# =========================================
# Typecasting
# =========================================
"""
x = 1
y = 2.0
z = "som"
print(type(x))
print(type(y))
print(type(z))

y = int(y)
print(type(y))
print(y)
"""
# =========================================
# User Input (Commented for reference)
# =========================================
"""
name = input("What is your name? :")
print("Hello" + " " +name)
age = int(input("What is your age? :"))
print("Your age is :" + " "+str(age))

"""
# =========================================
#  Math Funtion
# =========================================
"""
import math
pi =3.14
x=2
y = -3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(int(math.sqrt(81)))
print(abs(x))
print(max(x,y))
print(min(x,y))
print(abs(y))
print(pow(pi,2))
"""
# =========================================
#  Indexing
# =========================================
# To find n digit from starting , Staring index= 0 : stop index= n+1
# name[start:stop:step]
"""
name= "somya jain"
print(name[0:5])
print(name[6:])
print(name[0:9:2]) #count every second character includinf first

#reverse String
name="Somya"
print(name[::-1])
"""
# =========================================
#  slicing
# =========================================
# slicing : slice is used to create the substring which will  be reusable later on.
# slice(start,stop,step)
#negative index from right starts with -1 
"""
name = "Somya Jain from Illinois institute"
ins_slice= slice(16,-9)
print(name[ins_slice])
"""

# =========================================
# conditional statement
# =========================================
#if statement = block will execute if condition is true.
"""
a = 0
b = 0
if a>b:
    a = a + 1
elif a<b:
    b = b+1
elif a == 0 and b == 0:
    a = 1
    b = 1
else:
    a = a-1
    b = b+1
    
print(a,b)
"""


# =========================================
# Logical Operators
# =========================================
# And = both should be true , OR = any one should be true
"""
temp = int(input("Enter todays temperature : "))
if temp>=10 or temp ==30:
    print("temp is good outside")
elif temp<=0 and temp>=-10:
    print("temp is really cold")
else:
    print("No comments")
    

if not(temp>=10 and temp <=30):
    print("temp is not good outside")
"""
# =========================================
# While Loop
# =========================================
# loop control statment
# break : used to terminate the loop entirely
# continue : skips to the next iteration of the loop
# pass: does nothing acts as a placeholder
""" while True:
    name = input("Enter name : ")
    if name == "":
        continue
    elif name == "xyz":        
        print("enter correct name")
        continue
    elif name == "somya":
        print("enter new name")
        pass
    else:
        print("hello "+ name)
        break  """
"""
import time  
n = 10
print(n)
while n>1:
    n=n-1
    print(n)
    time.sleep(1)
print("Happy new year")
 """   

# =========================================
# For Loop
# =========================================
# while = unlimited , for loops = limited
"""
for i in range(10,101,2):
    print(i)

import time  
for sec in range(10,0,-1):
    print(sec)
    time.sleep(1)
print("Happy New Year")
"""



# =========================================
# Lists
# =========================================
# used to store multiple element in single variable
# square bracket , can be editable at any time even after assigning.
""" food = ["pizza" ,"cake", "burger","sushi"]
print(food[0]) #indexing
food.append("sss") #add at last index
food.pop() #last element
food.remove("pizza") 
food.insert(2, "pasta")
food.sort()
print(food) """

# 2d list
"""
Food =  ["burger", "pizza" , "fries"]
Drinks = ["Coffe" , "Soda", "Tea"]
party = [Food , Drinks]
print(party[0 ])
print(party[1][2])
"""
# =========================================
# Comprehensions
# =========================================
# List, Dictionary, and Set comprehensions
"""
sums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
even_squares = [x for x in squares if x % 2 == 0]

"""

# =========================================
# Tuple ()
# =========================================
# Tuple (): ordered collection , unchangable

""" student = ("somya" , 21 , "female")
#methods
print(student.count("somya"))
print(student.index("female"))

for somya in student:
    print("true") """
    
# aaccessing or ranges in tuples
# Caps_ltr = ( "A" , "B", "C")

# To add value in tuple we don't have direct method like list, so convert tuple into list or add the elememt 
# else make a new tuple and add that tuple to first one
""" Caps_ltr = ( "A" , "B", "C")
small_ltr = ("a","b","c")
Caps_ltr += small_ltr
print(Caps_ltr) """

# second way
""" letter =  ( "A" , "B", "C")
ltr_2 = list(letter)
ltr_2.append("D")
print(ltr_2) #list , ones you convert to list uh can apply append , remove 
letter = tuple(ltr_2)
print(letter) #tuple """


# =========================================
# Set {}
# =========================================
# cannot refered by index , unordered , no duplicate item.
# add, remove, clear 
# union , intersection, differences
"""
set1 = {"apple", "banana", "cherry"}
print(set1)

set2 = {"apple", "mango", "cherry" , "apple"} # it will print apple only ones.
set1.update(set2)
print(set1)
"""

# =========================================
# Dictionary
# =========================================
#changeable, unordered collection of key value pair.
"""
capitals = {'India':'Delhi' ,
            'USA': 'Washington',
            'Russia': 'Moscow'}
print(type(capitals))
print(capitals['India'])
print(capitals.get('germany')) #to check if the key exists
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'germany': 'value'})
print(capitals)
"""

# =========================================
# Zip Function
# =========================================
"""
names = ["A", "B", "C"]
ages = [20, 25, 30]
for name, age in zip(names, ages):
    print(name, age)
"""

# =========================================
# Index
# =========================================
#index operators [] : use to create substring , access the character of the string.
"""
name = 'somya jain'
first_name = name[0:5].upper()
last_name = name[6:].lower()
print(first_name,last_name)
"""


# =========================================
# Functions
# =========================================
# function : Block of code is executed only when defined.
"""
def aboutyou(f_name,l_name):
    print("My name is "+ f_name + " " + l_name)

aboutyou('somya', 'jain')


def add(f_num,scnd_num):
    add = f_num + scnd_num
    return add
print(add(2,3)) 
"""
#scope
#local scope = declare inside the funstion , Global scope = outside the function
#global variable and local variable can have same name.
"""
add = 2
def add_no(f_num,scnd_num):
    add = f_num + scnd_num
    return add
add_no(2,3) #access local variable
print(add) #access Global variable
"""
# *args = pack all the arhuments into tuple, in this way fuction will allow multiple arguments.
# * is imp , we can write *num , *stuffs etc
"""
def multiply(*args):
    val = 1
    for i in args:
        val = val * i
    return val
print(multiply(1,2,3,4))

# **kwargs (keyword arguments) = pack all parameter in dictionary , useful so that function can accept varying amount of keywords arguments.
def hllo(**kwargs):
    print("Hello",end = " ")
    for i,j in kwargs.items():  #kwargs is name of dic, it be anything 
        print(j,end = " ")
        
hllo(title="Miss",f_name="Somya",l_name="jain")
"""
#str format: optional method that give users more conteol while display the o/p
"""
name ="Sam!!"
print("\nMy name is {}".format(name))

num = 3067
print("The number pi is {:.2f}".format(num))
print("The number pi is {:b}".format(num))

"""
#random
"""
import random
dice = [1,2,3,4,5,6]
random.shuffle(dice)
print(dice)

x = random.sample(dice,3)
print(x)
"""
#Exception Handling
"""
try:
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))
    c= a/b
except Exception as e:
    print("Oopss Error!!")
    print(e)
else:
    print(c)
finally:
    print("It will always execute")
"""

# File management
"""
text ="have a great day\n"

with open('test.txt','w') as file:
    print(file.write(text))

with open('test.txt') as file:
    print(file.read())
    
print(file.closed)

import shutil

shutil.copyfile('test.txt','copy.txt')
"""


from oops import Cars

car_1 = Cars("Audi","Q5","2022")
car_1 = Cars("Ford","Mustang","2021")
    
car_1.drive()
