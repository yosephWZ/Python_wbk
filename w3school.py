# @#$!@#$@!#$Progress### << ///Feb_2024..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$
# !!!!! don't stay at one part for more than 1 weekds...!!!!
# !!!!! proceed as you go through by commenting .. for furhter refirinement..
# //..//...//..//...//..//..//..//...//
# //..//..Code explanation.//..use...//.ChatGPT.//..//..//...//
# //..//...//..//..codeChalenge..//..//..//..//..sololearn..//



''' sololearn practice


exit()
a,b,*c,d=1,2,3
print(c)

exit()
print(6>6.0)

exit()
str1="5"
str2="6"
print(str1<str2)

exit()

ls=[0,1,2]
for i, v in enumerate(ls):
    print(v+i,end ="")


exit()



print("htis can be used as a libarary for your future purose by the way")


exit()

print(3*7//5*10%4) #operation ,,precedace..
print(3*7//5*10)
print(40%4)


exit()

def spam(x):
    return str(x).zfill(3)
print(spam(1))

exit()

l1=[5,8,2]
l2=[2,7]
l3=l1+l2
l3=list(set(l3))
l3.sort()
print(l3[2])

exit()


def func(n):
    y='+'.join(str(x) for x in range(n))
    return(eval(y))
print(func(7))

exit()

print(3**1**2**4)

exit()
x=5
print(x>>2<<x)

exit()



exit()


'''



'''______Codecoach Challenges 

'''



'''_______ Python Get Started        

print("Hello, World!")

exit()

'''



'''_______ Python Syntax             
#Python Indentation

if 5 > 2:
  print("Five is greater than two!")
exit()
# exit()
# Syntax Error:

if 5 > 2:
print("Five is greater than two!") 

exit()

exit()
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")  #You have to use the same number of spaces 

exit()

# exit()
# Syntax Error:

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
exit()


# Python Variables


# exit()

x = 5
y = "Hello, World!"
exit()

# You will learn more about variables in the Python Variables chapter.

      
'''



'''_______ Python Variables          

# Creating Variables

x = 5
y = "John"
print(x)
print(y)
exit()

exit()

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
exit()

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
exit()

# Get the Type

x = 5
y = "John"
print(type(x))
print(type(y))
exit()


# Single or Double Quotes?


exit()
x = "John" # is the same as
x = 'John'

# Case-Sensitive
# This will create two variables:

a = 4
A = "Sally" #A will not overwrite a
exit()    

# int x, y, z;
x = y = z = 50;
print('%d', x + y + z);
exit()



my_num=1234
a=str(my_num//1000%10) #print(1%10)
b=str(my_num//100%10) #print(12%10)
c=str(my_num//10%10) #print(123%10)
d=str(my_num//1%10) #print(1234%10)
print(d+c+b+a)

exit()


val=3
print(val is None)

exit()

x = 10
y = 20
expression = 'x + y'  # This is a string representing a Python expression
result = eval(expression)  # Evaluating the expression using eval()
print(result)  # Output will be 30 (since x + y = 10 + 20)



# Variable Names

# Rules for Python variables:
#     must start with a letter or the underscore character
#     cannot start with a number
#     only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     case-sensitive (age, Age and AGE are three different variables)


# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# exit()

# Illegal variable names:
try
    2myvar = "John"
except:
    print("error naming")

my-var = "John"
my var = "John"


# Multi Words Variable Names

# Camel Case

myVariableName = "John"

# Pascal Case

MyVariableName = "John"

# Snake Case

my_variable_name = "John"

# Python Variables - Assign Multiple Values

# Many Values to Multiple Variables

exit()

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

exit()


# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

exit()

# Unpack a Collection

# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

exit()

# Python - Output Variables
# Output Variables

x = "Python is awesome"
print(x)
exit()

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

exit()

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
exit()


# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

exit()

x = 5
y = "John"
print(x + y)

exit()


x = 5
y = "John"
print(x, y)

exit()

# Python - Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()
exit()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
exit()

# The global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

exit()

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

exit()

# Python - Variable Exercises
# Test Yourself With Exercises

'''




'''______ Python Data Types 

# Built-in Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Getting the Data Type

# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

Setting the Data Type

exit()


Example	Data Type	Try it

x = "Hello World"	str	
print(type(x))
exit()

x = 20	int	
print(type(x))
exit()

x = 20.5	float	
print(type(x))
exit()

x = 1j	complex	
print(type(x))
exit()

x = ["apple", "banana", "cherry"]	list	
print(type(x))
exit()

x = ("apple", "banana", "cherry")	tuple	
print(type(x))
exit()

x = range(6)	range	
print(type(x))
exit()

x = {"name" : "John", "age" : 36}	dict	
print(type(x))
exit()

x = {"apple", "banana", "cherry"}	set	
print(type(x))
exit()

x = frozenset({"apple", "banana", "cherry"})	frozenset	
print(type(x))
exit()

x = True	bool	
print(type(x))
exit()

x = b"Hello"	bytes	
print(type(x))
exit()

x = bytearray(5)	bytearray	
print(type(x))
exit()

x = memoryview(bytes(5))	memoryview	
print(type(x))
exit()

x = None	NoneType	
print(type(x))
exit()


# Setting the Specific Data Type


x = str("Hello World")	str	
print(type(x))
exit()

x = int(20)	int	
print(type(x))
exit()

x = float(20.5)	float	
print(type(x))
exit()

x = complex(1j)	complex	
print(type(x))
exit()

x = list(("apple", "banana", "cherry"))	list	
print(type(x))
exit()

x = tuple(("apple", "banana", "cherry"))	tuple	
print(type(x))
exit()

x = range(6)	range	
print(type(x))
exit()

x = dict(name="John", age=36)	dict	
print(type(x))
exit()

x = set(("apple", "banana", "cherry"))	set	
print(type(x))
exit()

x = frozenset(("apple", "banana", "cherry"))	frozenset	
print(type(x))
exit()

x = bool(5)	bool	
print(type(x))
exit()

x = bytes(5)	bytes	
print(type(x))
exit()

x = bytearray(5)	bytearray	
print(type(x))
exit()

x = memoryview(bytes(5))	memoryview
print(type(x))
exit()



'''




'''_______  Python Numbers         


x = 1    # int
y = 2.8  # float
z = 1j   # complex
# To verify the type of any object in Python, use the type() function:
exit()

print(type(x))
print(type(y))
print(type(z))

exit()

# Int __ Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
exit()
# Float __Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

exit()

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
exit()

# Complex __ Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
exit()

# Type Conversion __ You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))  # Note: You cannot convert complex numbers into another number type.
exit()

# Random Number __Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))


print(7//2) # floor quoteent
print(13%2) # modular operator remainder
print("Welcome to the Code Playground")            #https://peps.python.org/pep-0008/

print("this is one");print("this is again")
exit()


print("#working with Numberical data") #6.17. Operator precedence  #https://docs.python.org/3/reference/expressions.html
print(6/2*3**2)
print(6/2*3)
print(5+6/2*3)
print(7-5+6/2*3)

exit()

a=range(6)
r=a[3+1]*4%3    #operator precedance..?? Multiply after modulo
print(r)

exit()

print(pow(2,2,3))#(same as (2 * 2 * 2) % 5):
print("Workign with Text data")
exit()


from fractions import Fraction
frac=Fraction(2,5)
print(frac*10)
exit()

a=1
B=a+1
print(B,end="")
print(B,a,sep="0")
print(int(1+2-3*4/5%6))
exit()

import random
x=random.randint(0,120)%55
print(x)
exit()

print(int(abs(5j+1)))# complex number
print("".join(['h','i']))
exit()

x=1024
print(isinstance(x,str))
exit()

h="234"
i=2
print("{}{}".format(*['h','i']))
exit()


a=2
b=3;
c="{a}{b}{ab}";
d=c.format(a=4,b=5,ab=a*b);
print(d)

exit()

print("shdfdf"[3])
exit()

print("helower"+"pyton user")
exit()

str="3434 this is a string"

print(str.partition('is'))  # creates a partition.. add to tuples..
exit()

print(True+ False)
exit()
s="hello"
print(*s)
exit()

s='abc'   
i=iter(s)
print(next(i))   #https://www.geeksforgeeks.org/python-next-method/
print(next(i))
print(next(i))
exit()

print("Mixing things up")
print(9 + 4 - 7)
print(9//4) #divide 9 how much to 4....that is...becomes...2
print(9%2)  #modular..///remander.. left for 9 to 2.. that is becomes...1
print(1%2)
exit()

# #data types... 
print(type("0"))
print(type(2.04))
print(type(2))
print(float(4))       #float
print(str(6)+str(5))  #string
print(int(5.0))       #integer 
print(chr(71))        # chr() builtin function
print("hey man"+ "i am good") #concatination
exit()

import math
a=pow(6,7)
b=math.pow(6,7)
print(a)
print(b)
exit()

print("Balance", 5000,sep=":")
print(4%5) #is 4 .. any thing less than ... would be itself
exit()

a=list(range(6))
print(a[4])

exit()


x=(1,2,3)
print(*x)
print(*x,sep="1")
print(*x,sep="1",end="3")

exit()

print("Iron", "Man", sep ="-")


exit()
print("Labeling, Storing and Handling Data with Variables")
x = 42       #integer
y = "Hello"  #string
z = 3.14     #float
exit()

print(type(1J))   # complex number

 exit()
from math import sqrt as sty
print(sqrt(4))
print(sty(4))

name="palul"
print("his {0} is ".format(name))

exit()


name = "palul"
print("his {0} is".format(name))

name = "palul"
print(f"his {name} is")

exit()


exit()
x="2"
print(int(x)) #convert to string
print(float(x)) # convert to float
print(int(9.04)) # convert to int

# examples
# print((1j**2).real)
# exit()

# a=chr(65)
# b=ord("a") 
# print(a==chr(b))

# exit()


# print(int('sdfd')) # error types
# exit()
# # print(type({})==type({1})) # why is this?
# print(type([])==type([1]))  #??
# print(type(())==type((1,2)))    #??

# exit()


# x="slooealrn"
# y=x[:]
# print(id(x)==id(y))

# exit()


# val=3
# print(val is None)

# print(int('sdfd')) # error types
# exit()
# print(None==None)


'''



'''_______ Python Casting            

# Python Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

exit()

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
exit()

# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

'''



''' __________ Python String 

# Strings

# 'hello' is the same as "hello".


print("Hello")
print('Hello')
exit()

# Assign String to a Variable

a = "Hello"
print(a)
exit()

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

# Get the character at position 1 

a = "Hello, World!"
print(a[1])
exit()

# Looping Through a String



# Loop through the letters in the word "banana":

for x in "banana":
  print(x)
exit()


# String Length

a = "Hello, World!"
print(len(a))
exit()

# Check String

# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
exit()


# Use it in an if statement:


# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

exit()


# Check if NOT

# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
exit()


# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

exit()


# Python - Slicing Strings

# You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5])
exit()

# Note: The first character has index 0.

b = "Hello, World!"
print(b[:5])
exit()

# Slice To the End

b = "Hello, World!"
print(b[2:])
exit()

# Negative Indexing


b = "Hello, World!"
print(b[-5:-2])
exit()



# Python - Modify Strings

# Upper Case

# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
exit()

# Lower Case


a = "Hello, World!"
print(a.lower())
exit()


# Remove Whitespace 
# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
exit()


# Replace String

# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
exit()


# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
exit()



# String Methods

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)
exit()



a = "Hello"
b = "World"
c = a + " " + b
print(c)
exit()


# Python - Format - Strings
# String Format



age = 36
txt = "My name is John, I am " + age
print(txt)
exit()


# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
exit()


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
exit()



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
exit()



# Python - Escape Characters
# Escape Character




txt = "We are the so-called "#"Vikings" from the north."
exit()


txt = "We are the so-called \"Vikings\" from the north."
exit()


# Escape Characters



# Python - String Methods

# capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)
exit()
# casefold()	Converts string into lower case
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)
exit()
# center()	Returns a centered string
txt = "banana"

x = txt.center(20)

print(x)

exit()
txt = "banana"

x = txt.center(20, "O")

print(x)

exit()
# count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
exit()
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)
exit()
# encode()	Returns an encoded version of the string
txt = "My name is Ståle"

x = txt.encode()

print(x)
exit()
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
exit()
# endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

exit()
txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)
exit()
# expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)
exit()
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
exit()
# find()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

exit()
txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)

exit()
txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)
exit()
txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))
exit()
# format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
exit()
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

exit()
# format_map()	Formats specified values in a string

exit()
# index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)
exit()
txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))

exit()
# isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Company 12"

x = txt.isalnum()

print(x)
exit()

# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"

x = txt.isalpha()

print(x)
exit()
txt = "Company10"

x = txt.isalpha()

print(x)
exit()
# isdecimal()	Returns True if all characters in the string are decimals
txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)
exit()
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

exit()
# isdigit()	Returns True if all characters in the string are digits
txt = "50800"

x = txt.isdigit()

print(x)
exit()
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())
exit()
# isidentifier()	Returns True if the string is an identifier
txt = "Demo"

x = txt.isidentifier()

print(x)
exit()
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
exit()
# islower()	Returns True if all characters in the string are lower case
txt = "hello world!"

x = txt.islower()

print(x)
exit()
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())
exit()
# isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"

x = txt.isnumeric()

print(x)
exit()
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
exit()
# isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)
exit()
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
exit()
# isspace()	Returns True if all characters in the string are whitespaces
txt = "   "

x = txt.isspace()

print(x)
exit()

txt = "   s   "

x = txt.isspace()

print(x)
exit()
# istitle()	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

exit()
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
exit()
# isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)
exit()
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())
exit()
# join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
exit()
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
exit()
# ljust()	Returns a left justified version of the string
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
exit()
txt = "banana"

x = txt.ljust(20, "O")

print(x)
exit()
# lower()	Converts a string into lower case
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)
exit()
# lstrip()	Returns a left trim version of the string
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
exit()
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
exit()
# maketrans()	Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
exit()
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
exit()
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
exit()
# partition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
exit()
txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)
exit()

# replace()	Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

exit()
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)
exit()
# rfind()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

exit()
txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)
exit()
txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))
exit()
# rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.rindex("e")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.rindex("e", 5, 10)

print(x)
exit()
txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))
exit()
# rjust()	Returns a right justified version of the string
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
exit()
txt = "banana"

x = txt.rjust(20, "O")

print(x)
exit()

# rpartition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)
exit()
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)
exit()
# rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)
exit()
txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)
exit()
# rstrip()	Returns a right trim version of the string
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")
exit()
txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)
exit()
# split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"

x = txt.split()

print(x)
exit()
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
exit()
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
exit()
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)
exit()
# splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
exit()
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)
exit()
# startswith()	Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)
exit()
txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)
exit()
# strip()	Returns a trimmed version of the string
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
exit()
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
exit()

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
exit()
# title()	Converts the first character of each word to upper case
txt = "Welcome to my world"

x = txt.title()

print(x)
exit()
txt = "Welcome to my 2nd world"

x = txt.title()

print(x)
exit()
txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)
exit()
# translate()	Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
exit()

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
exit()

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
exit()

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
exit()

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
exit()
# upper()	Converts a string into upper case
txt = "Hello my friends"

x = txt.upper()

print(x)
exit()

# zfill()	Fills the string with a specified number of 0 values at the beginning
txt = "50"

x = txt.zfill(10)

print(x)

exit()
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
exit()


print("gameofdice"[::2])

exit()


print("joining by converting each string to ord of \"hello world\"")
s = "hello world"
print(''.join(str(ord(c)) for c in s))

exit()



print(len(str(8/2**2**2)))
exit()
x=0b0010
print(x)
exit()


str1="5"
str2="6"
print(str1<str2)
exit()



s='think'
s=''.join(sorted(list(s)[:4]))
print(s)
exit()

a='solo'
print(a.zfill(6))
exit()


print("joining by converting each string to ord of \"hello world\"")
s = "hello world"
print(''.join(str(ord(c)) for c in s))
exit()

str1="5"
str2="6"
print(str1<str2)
exit()



s='think'
s=''.join(sorted(list(s)[:4]))
print(s)
exit()


a='solo'
print(a.zfill(6))
exit()



strt = "Hello world!"
print(strt[6])
exit()


'''
   


'''_______ Python Boolean            

# Python Booleans


# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)
exit()


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
exit()

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,



print(bool("Hello"))
print(bool(15))
exit()

# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
exit()

# Most Values are True
# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
exit()

# Some Values are False


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
exit()


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
exit()

# Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction())
exit()

# You can execute code based on the Boolean answer of a function:

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
exit()


# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

exit()

print("alphabetical order of their component letters")
print("ord('a')",ord('a'))
print("ord('b')",ord('b'))
print("'a' > 'b'",'a' > 'b')

print("\"Bob\" > \"Dave\"","Bob" > "Dave")

exit()

x = (7 > 5)
print("int(7 > 5)",int(x))
print("int not(7 > 5)",int(not x))
exit()


print("# # Booleans  and comparision")
exit()

print("2==3",2 == 3)           #equal.......... not assign
print("2 > 3 and 2<2",2 > 3 and 2<2)    #and 
print("2 > 3 and 2==2",2 > 3 and 2==2)   #lessthan ..... greaterthan ......comparative
print("2 == 3 or 2>=2",2 == 3 or 2>=2)   #greater or equal
print("0== 0 or 2 != 3",0== 0 or 2 != 3)  #the not equal to operator

exit()

print("0  == 0 or True)",0  == 0 or True)#2 <>3)   #the not equal to operator
exit()

print(3.0==3) 
print(0.0==0) 

print("#and")
print("1 == 1 and 2 == 2",1 == 1 and 2 == 2)
print("1 == 1 and 2 == 3",1 == 1 and 2 == 3)
print("1 != 1 and 2 == 2",1 != 1 and 2 == 2)
print("2 < 1 and 3 > 6",2 < 1 and 3 > 6)
exit()

print("#or")
print( "1 == 1 or 2 == 2",1 == 1 or 2 == 2)
print( "1 == 1 or 2 == 3 ",1 == 1 or 2 == 3 )
print( "1 != 1 or 2 == 2 ",1 != 1 or 2 == 2 )
print( "2 < 1  or 3 > 6 ",2 < 1  or 3 > 6 )
exit()
print(" Boolean Not")

print("not 1 == 1",not 1 == 1)

exit()
print(" Boolean Operator preccedance      NOT > XOR > AND > OR    derived from C")
print(not True and True)
print("2>3 and 4<2 or 3>3 and 2>3 or not(3>3)",2>3 and 4<2 or 3>3 and 2>3 or not(3>3))
exit()



Operator
a=8
b=6
c=a%b

# print(c)

d=int(a/c)




# logical operator
print('p' == 'p',[]is[])
print('p' == 'p',[]is[])
# print([]is[])

exit()


print(1 or 2)
print(1 or 0 and 2)
print(0 and 2)

exit()


print("alphabetical order of their component letters")
print("ord('a')",ord('a'))
print("ord('b')",ord('b'))
print("'a' > 'b'",'a' > 'b')

print("\"Bob\" > \"Dave\"","Bob" > "Dave")

exit()

x = (7 > 5)
print("int(7 > 5)",int(x))
print("int not(7 > 5)",int(not x))
exit()


print("# # Booleans  and comparision")
exit()

print("2==3",2 == 3)           #equal.......... not assign
print("2 > 3 and 2<2",2 > 3 and 2<2)    #and 
print("2 > 3 and 2==2",2 > 3 and 2==2)   #lessthan ..... greaterthan ......comparative
print("2 == 3 or 2>=2",2 == 3 or 2>=2)   #greater or equal
print("0== 0 or 2 != 3",0== 0 or 2 != 3)  #the not equal to operator

exit()

print("0  == 0 or True)",0  == 0 or True)#2 <>3)   #the not equal to operator
exit()

print(3.0==3) 
print(0.0==0) 
print("#and")
print("1 == 1 and 2 == 2",1 == 1 and 2 == 2)
print("1 == 1 and 2 == 3",1 == 1 and 2 == 3)
print("1 != 1 and 2 == 2",1 != 1 and 2 == 2)
print("2 < 1 and 3 > 6",2 < 1 and 3 > 6)

exit()

print("#or")
print( "1 == 1 or 2 == 2",1 == 1 or 2 == 2)
print( "1 == 1 or 2 == 3 ",1 == 1 or 2 == 3 )
print( "1 != 1 or 2 == 2 ",1 != 1 or 2 == 2 )
print( "2 < 1  or 3 > 6 ",2 < 1  or 3 > 6 )
exit()

print(" Boolean Not")

print("not 1 == 1",not 1 == 1)

exit()
print(" Boolean Operator preccedance      NOT > XOR > AND > OR    derived from C")
print(not True and True)
print("2>3 and 4<2 or 3>3 and 2>3 or not(3>3)",2>3 and 4<2 or 3>3 and 2>3 or not(3>3))
exit()


# logical operator
print('p' == 'p',[]is[])
print('p' == 'p',[]is[])
print([]is[])


a='abcd'
b='defg'
c=''
for i in a:
    if i not in b:
        c+=i
print(c)

a=0 or 1
print(a)
b=0 or 2
print(b)
exit()
c=a or b
print(a+b+c)

exit()

print(1 or 2)
print(1 or 0 and 2)
print(0 and 2)

x = 10
y = 20
expression = 'x + y'  # This is a string representing a Python expression

result = eval(expression)  # Evaluating the expression using eval()

print(result)  # Output will be 30 (since x + y = 10 + 20)


'''




'''_______ Python Opertors           

# Python Operators

# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
# Python Arithmetic Operators

# Arithmetic operators
# +	Addition	x + y	
x = 5
y = 3
print(x + y	)
exit()
# -	Subtraction	x - y	
x = 5
y = 3
print(x - y	)
exit()

# *	Multiplication	x * y	
x = 5
y = 3
print(x *y	)
exit()

# /	Division	x / y	
x = 5
y = 3
print(x / y	)
exit()

# %	Modulus	x % y	
x = 5
y = 3
print(x%y)
exit()

# **	Exponentiation	x ** y	
x = 5
y = 3
print(x **y)
exit()

# //	Floor division	x // y	
x = 5
y = 3
print(x // y)
exit()


# Python Assignment Operators

# =	x = 5	x = 5	
x = 5	
print(x)
exit()

x=5
x += 3	#x = x + 3	
print(x)
exit()

x=5
x -= 3	#x = x - 3	
print(x)
exit()

x=5
x *= 3	#x = x * 3	
print(x)
exit()

x=5
x /= 3	#x = x / 3	
print(x)
exit()

x=5
x %= 3	#x = x % 3	
print(x)
exit()

x=5
x //= 3	#x = x // 3	
print(x)
exit()

x=5
x **= 3	#x = x ** 3	
print(x)
exit()

x=5
x &= 3	#x = x & 3	
print(x)
exit()

x=5
x |= 3	#x = x | 3	
print(x)
exit()

x=5
x ^= 3	#x = x ^ 3	
print(x)
exit()

x=5
x >>= 3	#x = x >> 3	
print(x)
exit()

x=5
x <<= 3	#x = x << 3	
print(x)
exit()


# Python Comparison Operators

x = 5
y = 3
print(x == y)  # ==	Equal	x == y	)
exit()
x = 5
y = 3
print(x != y)  # !=	Not equal	x != y	)

exit()
x = 5
y = 3
print(x > y	)  # >	Greater than	x > y	)

exit()
x = 5
y = 3
print(x < y	)  # <	Less than	x < y	)

exit()
x = 5
y = 3
print(x >= y)  # >=	Greater than or equal to	x >= y	)
exit()

x = 5
y = 3
print(x <= y)   # <=	Less than or equal to	x <= y	)
exit()



# Python Logical Operators
x = 5
print(x < 5 and  x < 10)# and 	Returns True if both statements are true	x < 5 and  x < 10)
exit()
x = 5
print(x < 5 or x < 4	)# or	Returns True if one of the statements is true	x < 5 or x < 4	)
exit()
x = 5
print(not(x < 5 and x < 10)	)# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	)
exit()

# Python Identity Operators

# is 	Returns True if both variables are the same object	x is y	

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
exit()

print(x is y) # returns False because x is not the same object as y, even if they have the same content
exit()

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
exit()

exit()

# is not	Returns True if both variables are not the same object	x is not y	
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)# returns False because z is the same object as x
exit()

print(x is not y) # returns True because x is not the same object as y, even if they have the same content
exit()


print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
exit()




# Python Membership Operators

x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list

exit()

x = ["apple", "banana"]
print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list

exit()


# Python Bitwise Operators


x = 5
y = 3
print(x &  y)  # & 	AND	Sets each bit to 1 if both bits are 1
exit()

x = 5
y = 3
print(x | y)  # |	OR	Sets each bit to 1 if one of two bits is 1
exit()

x = 5
y = 3
print(x ^ y)  # ^	XOR	Sets each bit to 1 if only one of two bits is 1
exit()

x = 5
y = 3
print(x ~ y)  # ~ 	NOT	Inverts all the bits
exit()

x = 5
y = 3
print(x << y)   # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
exit()
x = 5
y = 3
print(x >> y)   # >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
exit()


print("#In-Place Operator")
x = 2
print(x)

x += 3
print("x+=2",x)
exit()

x *= 3
print("x*=2",x)
exit()

x **= 3
print("x**=2",x)
x %= 2
print("x%=2",x)
exit()

exit()
x = "spam"
print("x = \"spam\"",x)
exit()

x += "eggs"
print("x = \"egg\"",x)
exit()

x = "a"
x *= 3
print("x *= 3",x)


exit()

print(5**5%5+9*9)
rint=5**5
print(rint%5+9*9)

if 2&0:
    print("yes")
else:
    print("No")

exit()



a=b=c=2
print(a==b==c)


exit()
#send to string operation
x="slooealrn"

y=x[:]
print(id(x)==id(y))

exit()

a=0 or 1
print(a)
b=0 or 2
print(b)

c=a or b
print(a+b+c)


print(7*(3+4-2)//5)
exit() 

print(abs(3+4j))
exit()



a=b=c=2
print(a==b==c)


exit()
#send to string operation


a=8
b=6
c=a%b
print(c)

d=int(a/c)


print(len(str(8/2**2**2)))
exit()
x=0b0010
print(x)
exit()

print((1j**2).real)
exit()

a=chr(65)
b=ord("a") 
print(a==chr(b))

exit()


print(7*(3+4-2)//5)
exit() 

print(abs(3+4j))
exit()



my_num=1234
a=str(my_num//1000%10) #print(1%10)
b=str(my_num//100%10) #print(12%10)
c=str(my_num//10%10) #print(123%10)
d=str(my_num//1%10) #print(1234%10)
print(d+c+b+a)
exit()

'''




'''_______ Python Lists              

exit()
mylist = ["apple", "banana", "cherry"]

# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
exit()

# List Items

# Ordered

# Changeable

# Allow Duplicates



# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
exit()

# List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
exit()


# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
exit()


# A list can contain different data types:
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
exit()

# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
exit()

# The list() Constructor


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
exit()

# Python Collections (Arrays)

# Python - Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
exit()



# Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
exit()

# Range of Indexes


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
exit()



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
exit()


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
exit()

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
exit()

# Check if Item Exists


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
exit()


# Python - Change List Items


# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
exit()

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
exit()


# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
exit()


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
exit()

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
exit()

# Python - Add List Items
# Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
exit()

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
exit()

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
exit()

# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

exit()

# Python - Remove List Items

Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
exit()


# The pop() method removes the specified index.


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
exit()



# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
exit()


# The del keyword also removes the specified index:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
exit()

# The del keyword can also delete the list completely.


thislist = ["apple", "banana", "cherry"]
del thislist
exit()


# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
exit()

# Python - Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

exit()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

exit()



# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
exit()

# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
exit()

# Python - List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
exit()


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
exit()


# The Syntax
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]

exit()

# With no if statement:

newlist = [x for x in fruits]
exit()

# Iterable
newlist = [x for x in range(10)]
exit()

newlist = [x for x in range(10) if x < 5]
exit()

# Expression

newlist = [x.upper() for x in fruits]
exit()


newlist = ['hello' for x in fruits]
exit()


newlist = [x if x != "banana" else "orange" for x in fruits]
exit()


# Python - Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
exit()

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
exit()

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
exit()

# Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
exit()

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
exit()

# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
exit()


# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
exit()


# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
exit()

# Python - Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
exit()



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
exit()


# Python - Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
exit()

# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
exit()


# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
exit()


# Python - List Methods

# append()	Adds an element at the end of the list

exit()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
exit()
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
exit()
# clear()	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
exit()
# copy()	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
exit()

# count()	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
exit()
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
exit()
# extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
exit()
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
exit()
# index()	Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
exit()
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
exit()
# insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
exit()

# pop()	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

exit()
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
exit()
# remove()	Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
exit()
# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
exit()
# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
exit()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

exit()
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

exit()



exit()
a=[8,0,4,6,1]
if (a is a[:]):#(a == a[:]):
    print(True)
else:
    print(False)
    
print(a[:])



x=[2,3,4]
y=x
print(y is x)
y=x[:]
print(y is x)

exit()




a=[[1,2],[2,3],[3,4]]
b=[x for x in a for x in x]
print(b)


arr=[1,(2,3),4]
n=len(arr)
if (2 in arr):
    n=n+len(arr[1])
print(n)


a="Hello !"
newHello=[]
for hi in a:
   for by in range(2):
    newHello.append(hi)
    print(newHello)
print(len(newHello))

exit()


list
x=[i for i in range(3,15,3)]
y=x
print(x)
y.append([i for i in range(2,14,3)])
print(y)
print(x)
print(len(x)/1)
exit()

x=[1,3,5]
print(x in x)
exit()
a=[1,2,4,5]
print(a[1:5])#=[1]
a[1:5]=[1]
print(a)
exit()

a=0
b=0
x=[a,b]
y=(1,2)
x=y
print(x,a,b)

exit()
lst=[].append(5)
print(lst)
exit()
a={1,3,5}
b={2,4,6}



exit()
x=[i for i in range(3,15,3)]
y=x
print(x)
y.append([i for i in range(2,14,3)])
print(y)
print(x)
print(len(x)/1)

exit()

x=[1,3,5]
print(x in x)
exit()

a=[1,2,4,5]
print(a[1:5])#=[1]
a[1:5]=[1]
print(a)
exit()

a=0
b=0
x=[a,b]
y=(1,2)
x=y
print(x,a,b)

exit()

lst=[].append(5)
print(lst)
exit()


x=[2,3,4]
y=x
print(y is x)
y=x[:]
print(y is x)

exit()


a=[[1,2],[2,3],[3,4]]
b=[x for x in a for x in x]
print(b)
exit()

arr=[1,(2,3),4]
n=len(arr)
if (2 in arr):
    n=n+len(arr[1])
print(n)
exit()

a="Hello !"
newHello=[]
for hi in a:
   for by in range(2):
    newHello.append(hi)
    print(newHello)
print(len(newHello))

exit()


words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

ar=[2,1,3]#,"a",3]
ar.sort()
print(ar)

exit()

a=[1,2,3,4]
b=a.copy()
print(b)
b.append(a)
print(b)
a.append(b)
print(a)
print(len(a))
print(len(b))
exit()

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print(m)
exit()

# # iterate throguh a list and dump the list

x=[2,8]#,7,1,0,124,8897,55,3,67,99]
nums=0


y=[x if x==1 else x*2 for x in ["1","2"]][0]

print([x if x==1 else x*2 for x in ["1","2"]])

exit()

a=[2,4,6,8]
b=a
print(b)

b[0]=7
a[3]=9

print(a)

b.append(5)


print(a)

exit()

a,b=[0],[0]
a,b=b,a





L=list(range(10))

print(L)
print(L.pop())#remove the last
print(L)
print(max(L))
exit()

word="bringback"
print(word[::-2])

exit()
# iterate throguh a list and dump the list
x=[1,3,4,5,8]
for nums in len(x):
    nums+=1
  
# iterate throguh a list and dump the list
print(list(range(len(x))))
exit()

games=['tennis','footballes','cricket']
for item in games:
    if 'ball' in item:
        print(item)


exit()

#diffrence b/n list and map>>???
abc=list(range(5))
sq=list(map(lambda x:x**2,range(5)))
print(abc)
print(sq)
exit()

for i in range(len(x)):
    print(x[i])
    i+=i 
exit()

# iterate throguh a list find cummmulative
sum=0
for num in x:
    sum+=num
    
print(sum)

exit()
# to add all odd nubmer in list...

b=[1,2,3,4,5]
print(b[1:-2])
print(b[1:-1])
exit()

nums = [1,2,3,4]
res=0

for x in nums:
    if x%2==nums:
        continue
    else:
        print(x)    #res+=x #res = res+x
        res+=x      #res = res+x
        
print(res)

exit()

i=list(range(1,4))
# i=list(range(4))
print(i)
exit()

# s=list(map(lambda x:x**2,i)) 
s=list(filter(lambda x:x**2,i))
print(s)
print(sum(s))
exit()

my_list=["apples","tomatoes","banana","orange","melons"]
my_list.sort(key=lambda x:x[-2])
print(my_list[1])
exit()


# Python next() method
list=[1,2,3,4]
a=(i**2 for i in list)
print(a)
print(next(a),next(a))  #https://www.geeksforgeeks.org/python-next-method/
exit()


fib=[0,1,1,2,3,5,8,13]
# print(fib[::2])
print(fib[2::2])

exit()


# https://www.geeksforgeeks.org/python-range-function/       #Syntax of Python range() function

# Syntax: range(start, stop, step)
# In the given exit(), we are printing the number from 0 to 4.

for i in range(5):
	print(i, end=" ")
exit()

# The remove method working 
l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
['Bob', 'Charlie', 'Bob', 'Dave']
exit()

# In this exit(), we are printing the number from 0 to 5. We are using the range function in which we are passing the stopping of the loop... printing first 6  whole number
for i in range(6):
	print(i, end=" ")
exit()


for i in range(5, 20): # printing a naturar number from 5 to 20
	print(i, end=" ")

exit()

for i in range(0, 10, 2): # exit() of Python range (start, stop, step)
	print(i, end=" ")
exit()



for i in range(0, 30, 4): #incremented by 4
	print(i, end=" ")
exit()


for i in range(25, 2, -2): #incremented by -2
	print(i, end=" ")
exit()



for i in range(3.3): #using a float number
	print(i)
exit()
# Concatenation of two range() functions using itertools chain() method

from itertools import chain

# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
	print(i, end=" ")

exit()


ele = range(10)[0]  # Accessing range() with an Index Value
print("First element:", ele)
exit()

ele = range(10)[-1]
print("\nLast element:", ele)
exit()

ele = range(10)[4]
print("\nFifth element:", ele)
exit()

# range() function with List in Python

fruits = ["apple", "banana", "cherry", "date"]

for i in range(len(fruits)):
	print(fruits[i])

exit()

# Return Type in range() vs xrange()
# initializing a with range()

a = range(1, 10000)

# initializing a with xrange()
x = xrange(1, 10000)

# testing the type of a
print("The return type of range() is : ")
print(type(a))
exit()

# testing the type of x
print("The return type of xrange() is : ")
print(type(x))
exit()

# Speed of xrange() and range() Function
import sys

# initializing a with range()
a = range(1,10000)

# initializing a with xrange()
x = xrange(1,10000)

# testing the size of a
range() takes more memory
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))
exit()

# testing the size of x
xrange() takes less memory
print ("The size allotted using xrange() is : ")
print (sys.getsizeof(x))
exit()


# Operations Usage of xrange() and range() Function
# initializing a with range()
a = range(1,6)

# initializing a with xrange()
x = xrange(1,6)

# testing usage of slice operation on range() prints without error
print ("The list after slicing using range is : ")
print (a[2:5])
exit()

# testing usage of slice operation on xrange() raises error
print ("The list after slicing using xrange is : ")
print (x[2:5])
exit()

# Python – Test if List contains elements in Range


# Method #1 : 
    # Using loop This is brute force method in which this task can be performed. In this, we just check using if condition if element falls in range, and break if we find even one occurrence out of range. 

# Python3 code to demonstrate 
# Test if List contains elements in Range
# using loop

# Initializing loop 
test_list = [4, 5, 6, 7, 3, 9]

# printing original list 
print("The original list is : " + str(test_list))

# Initialization of range 
i, j = 3, 10

# Test if List contains elements in Range using loop
res = True
for ele in test_list:
	if ele < i or ele >= j :
		res = False
		break

# printing result 
print ("Does list contain all elements in range : " + str(res))

exit()

# Method #2 : 
    # Using all() This is alternative and shorter way to perform this task. In this we use check operation as a parameter to all() and returns True when all elements in range. 


# Python3 code to demonstrate 
# Test if List contains elements in Range
# using all()

# Initializing loop 
test_list = [4, 5, 6, 7, 3, 9]

# printing original list 
print("The original list is : " + str(test_list))

# Initialization of range 
i, j = 3, 10

# Test if List contains elements in Range
# using all()
res = all(ele >= i and ele < j for ele in test_list) 

# printing result 
print ("Does list contain all elements in range : " + str(res))
exit()


# Method #3 : Using list comprehension and len()

# Python3 code to demonstrate
# Test if List contains elements in Range
# using List Comprehension and len()
# Initializing list


test_list = [4, 5, 6, 7, 3, 9]

# printing original list
print("The original list is : " + str(test_list))

# Initialization of range
i, j = 3, 10

# Test if List contains elements in Range
# using List Comprehension and len()
out_of_range = len([ele for ele in test_list if ele < i or ele >= j])==0

# printing result
print ("Does list contain all elements in range : " + str(out_of_range))
exit()

# Python3 code to demonstrate
# Test if List contains elements in Range
# using any()

# Initializing list and range boundaries
test_list = [4, 5, 6, 7, 3, 9]
i, j = 3, 10

# Checking if any element in the list is within the range
res = any(i <= x < j for x in test_list)

# Printing the result
print("Does list contain any element in range: " + str(res))
exit()

# Method 5: Using filter() function

# Python3 code to demonstrate
# Test if List contains elements in Range
# using filter()

# Initializing list and range boundaries
test_list = [4, 5, 6, 7, 3, 9]
i, j = 3, 10
exit()

# Function to check if x lies within the given range
def in_range(x):
	return i <= x < j
exit()
# Filtering out the elements that lie within the range
# filtered_list = list(filter(in_range, test_list))

# Checking if the filtered list is not empty
res = bool(filtered_list)

# Printing the result
print("Does list contain any element in range: " + str(res))
exit()

# Python – Test if elements of list are in Min/Max range from other list


# Method #1 : Using loop + min() + max()
# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using loop + min() + max()

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original lists
print("The original list is : " + str(test_list))
exit()

# initializing range_list
range_list = [4, 7, 9, 6]

res = True
for ele in range_list:

	flag off list in case of any off range element
	if ele max(test_list):
		res = False
		break

# printing result
print("Are all elements in min/max range? : " + str(res))



# Method #2 : Using all() + min() + max()

# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using all() + min() + max()

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original lists
print("The original list is : " + str(test_list))
exit()

# initializing range_list
range_list = [4, 7, 9, 6]

# checking for all values in range using all()
res = all(ele >= min(test_list) and ele <= max(test_list)
		for ele in range_list)

# printing result
print("Are all elements in min/max range? : " + str(res))


# Method #3: Using set intersection


# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using set intersection

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original lists
print("The original list is : " + str(test_list))
exit()

# initializing range_list
range_list = [4, 7, 9, 6]

# using set intersection to find common elements between test_list and range_list
# common_elements = set(test_list).intersection(set(range_list))

# checking if all common elements are within the range

res = all(ele >= min(test_list) and ele <= max(test_list)
		for ele in common_elements)

# printing result
print("Are all elements in min/max range? : " + str(res))
exit()

# Method #4: Use list comprehension

# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using list comprehension

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original list
print("The original list is : " + str(test_list))
exit()

# initializing range list
range_list = [4, 7, 9, 6]

# filtering range list to remove elements outside of min/max range
# filtered_list = [x for x in range_list if min(test_list) <= x <= max(test_list)]

# checking if filtered list is the same as range list
res = filtered_list == range_list

# printing result
print("Are all elements in min/max range? : " + str(res))
exit()



# Python | Generate random numbers within a given range and store in a list

import random


print("Random integers between 0 and 9: ")
for i in range(4, 15):
	y = random.randrange(9)
	print(y)

# Method 1: Generate random integers using random.randrange() method
import random


print("Random integers between 0 and 9: ")
for i in range(4, 15):
	y = random.randrange(9)
	print(y)
exit()

# Method 2: Generate random integers using random.uniform() method
import random


print("Random integers between 0 and 9: ")
for i in range(4, 11):
	y = random.uniform(4, 10)
	print(y)
exit()


# Method 3: Generate random integers using randbelow() method
from secrets import randbelow

for _ in range(3, 9):

	print(randbelow(15))

exit()

# Method 4: Generate random integers using the random.randint() method

# Python code to generate
# random numbers and
# append them to a list





def Rand(start, end, num):
	res = []

	for j in range(num):
		res.append(random.randint(start, end))

	return res


Driver Code
num = 10
start = 20
end = 40
print(Rand(start, end, num))
exit()


# Using random.sample() function:
import random

num = 10
start = 20
end = 40

result = random.sample(range(start, end + 1), num)

print(result)



# Python | Contiguous Boolean Range


# Method #1 : Using enumerate() + zip() + list comprehension By using combination of above three functions, this task can easily be accomplished. The enumerate function handles the role of iteration, zip function groups the like values and the logic part is handled by list comprehension. 
# Python3 code to demonstrate
# Contiguous Boolean Ranging
# using enumerate() + zip() + list comprehension

# initializing list 
test_list = [True, True, False, False, True,
			True, True, True, False, True]

# printing the original list 
print ("The original list is : " + str(test_list))
exit()

# using enumerate() + zip() + list comprehension
# for Contiguous Boolean Ranging
# res = [x for x, (i , j) in enumerate(zip( [2]
		# + test_list, test_list + [2])) if i != j]

# printing result
print ("The boolean range list is : " + str(res))

exit()

  # Method #2 : Using sum() + accumulate() + groupby() The above three functions can also be clubbed together to achieve the particular task, as they use the iterators to achieve it. The sum function counts each value, groupby groups each one and all together are accumulated by the accumulate function. 

# Python3 code to demonstrate
# Contiguous Boolean Ranging
# using sum() + accumulate() + groupby()
# from itertools import accumulate, groupby

# initializing list 
test_list = [True, True, False, False, False,
			True, True, True, False, False]

# printing the original list 
print ("The original list is : " + str(test_list))
exit()

# using sum() + accumulate() + groupby()
# for Contiguous Boolean Ranging
# res = [0] + list(accumulate(sum(1 for i in j) 
			# for i, j in groupby(test_list)))

# printing result
print ("The boolean range list is : " + str(res))

exit()

# Method #3 : Using looping


# Python3 code to demonstrate
# Contiguous Boolean Ranging
# using for loop and if statement

# initializing list 
test_list = [True, True, False, False, False,
			True, True, True, False, False]

# printing the original list 
print("The original list is:", test_list)

exit()

# using for loop and if statement
# for Contiguous Boolean Ranging

res = []
for i, v in enumerate(test_list):
	if i == 0 or v != test_list[i-1]:
		res.append(i)
res.append(len(test_list))
# printing result
print("The boolean range list is:", res)
# This code is contributed by Edula Vinay Kumar Reddy
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

exit()

k=list(range(0,6,2)) #covnert to list range
print(len(k))
exit()

a=[1,2,3,4]
b=a
print(b)
exit()

import copy
a = [[1],[2],[3]]
b = copy.deepcopy(a) ## this will copy the list a to list b

print(b)

exit()
a=[1,2,3,4]
print(a[2:2])


a='python'[::-1]
print(a)
exit()

a='python'[::-1].endswith('y')
print(a)
exit()

a='python'[::-1][::-1]
print(a)
exit()

a='python'[::-1][::-1].endswith('n')
print(a)
exit()

mylist=list(range(5))
n=id(mylist)
mylist[:]=[x for x in mylist if x%2]
print(id(mylist)==n)
exit()


a=[8,0,4,6,1]
print(a == a[:])
exit()
print(a is a[:])
# print('a'is 'b')
if(a is a[:]):
    print(True)
else:
    print(False)
    
exit()


num=5
my_list=[0,1,5,4]

print(my_list[:-1])
exit()
print(my_list[:-2])

exit()
print(my_list if num > 7 else my_list[:-2])
exit()
print(list(range(0,5)))
exit()
print(list(range(5)))
exit()
x="hello!"
for i in range(0,len(x)-1):
    print((x[i]))

exit()

List=[]
List.append(1)
List.extend(2)
print(List)


exit()
a=[1]
a*=2
print(a)
a[0]=3
print(sum(a))

exit()
# list
l1=[1,2,3,4] 
l2=list(map(lambda x:x+2 if x>2 else x-2,l1))
print(l2)

k=[[1,2,3,4,5,6]]
k.append(7)
k.insert(1,8)
print(k)
print(len(k))

exit()
print(sum(list(range(0,4)))) #
my_list=[i for i in range(8)]
for i in my_list:
    my_list.remove(i)
print(sum(my_list))


print(list(range(4,7,2)))
exit()

my_list=["car","plane","train","bike","rocket"]
newlist=sorted(my_list)
print(newlist)
print(newlist[-1])
newlist=sorted(my_list,key=lambda x:x[-2])
print(newlist)

exit()


# list
x='abcde'
y=x[-1:]
print(y)
print(len(y))
#list
a=[1,2,3]
b=[4,5]
a.append(b)
a.extend(b)

print(a)

#list 
l=['a','b','c']
print('d'.join(l))
exit()


exit()



L=[[]]*3
print(L)
L[0]+=[[]]
print(L)
print(L[0]==L[1])
print(L[0]is L[1])
print(len(L[0])==bool(L[0]))


nums={1,2,3,4,5,6}
nums={0,1,2,3}&nums
nums=filter(lambda x:x>1, nums)
print(len(list(nums)))



exit()

#List
a=[1,2,3,4,6,7,8]
b=a[:4]
b.append(5)

print(b)

exit()

lar_num=0
print(list(range(0,10,3)))
exit()
for i in range(0,10,3):
    if lar_num>=6:
        break
    if i > lar_num:
        lar_num=i%2
print(lar_num)


exit()

r=['red','orange','yellow','green','blue','indigor']
p=[c[0] for c in r if len(c)<6]
print('_'.join(p))


arr=[0,1,2,3,4,5]
##r=[#,1,#,3,#,5]
n=0
for _ in arr:
    print(_)  # refers from arr
    # del arr[n] # method is only to delete okay
    # print(arr[n])
    n+=1
    # print(n)
    del arr[n]  # method is only to delete okay
    print("loop")
    # del arr[n] # method is only to delete okay

a=[2,4,5]
print(list(range(1,3)))

for i in range(1,3):
    print(i)
    a[i]=a[i-1] #[1,1]..[2,2]
    print(a[i],end='')
    print(i)


a=[2,1,2,4]
a[1:].remove(2)
print(sum(a))


A=[1,2,3,4,5,6,7]
G=iter(A)
next(G)
for num in G:
    print(num)
    next(G)
    next(G)

a=[1,2,3]
b=a
b.append(3)
print(b[3]==a[-1])

print({1,2,3}is{1,2,3})
print({1,2,3}=={1,2,3})

L=[[]]*3
# print(L)
print(L[0]==L[1])
print(L[0] is L[1])
print(len(L[0])==bool(L[0]))

# arr=[2,1,"a",3]
arr=["b","a"]
arrL=[2,1,2,3]
arrL.sort()
arr.sort()
print(arrL) #with letter and nubmer mixed up..it gifes error
print(arr)



my_list=[1,5,1,0,1,9,9,5]
new_list=my_list[-1:-4:-1]#[-1::-1] #for start.. then undrestand
print(new_list)

print(list[::-1]) #one way of doing reversing
print(list(reversed(list(range(5)))))
print([i for i in list(range(5))])

print(bool([])+1)


s=list(reversed(list("hewer")))
print(s)



s=reversed("sdfd")
print(s) # address of object s..


print(''.join(list(reversed(list("sdfsd")))))


x="abc"
x=list(x)
x.insert(1,"d")
x=''.join(x)
x=x[2:0:-1]
print(x)



a=[1,2,3]
del(a[0])
# print(del(a[0]))
print(a)
print(len(a[1:]))


a=[1,2,3,5,8,13]
print(a[2:2])
exit()

arr=[1,0,1,0]
a=all(arr)
s=sum(arr)
if a or s:
    print(a or s)
else:
    pass
exit()


squares=[0,1,4,8,16]
quaras=squares
squares[3]=0
print(quaras)
exit()

nums=[11,22,33,44,55]
res=list(filter(lambda x:not(x%2==0),nums))
print(res)
exit()



a=["c","b","a"]
a=a[::-1]
print(a[1])
exit()


exit()

arr=[0,1,1,0]
for val in arr:
    if val==0:
        arr[val]=1
print(arr)
exit()


num1=[1,3,4,5]
num2=num1
num2[0]=5
print(num1[0])
exit()

exit()

mylist=[1,2,3,4,5,6]
print(mylist[2:5])
mylist[2:5]=[]
print(mylist)
print(len(mylist))
exit()


print("sololearn"[:1])
exit()



a=[1,2,3]
b=[4,5]
a.append(b)
a.extend(b)
print(a)
exit()


a,b,*c=[x for x in range(0,12,3)]
print(*c)
exit()

A=[8,0,-4,-6,1]
for n in A:
    if n<0:
        A.append(abs(n))
    x=n
print(x)    
exit()


strList=['1','2','3','4','a']
intList=[]
for i in strList:
    try:
        intList.append(int(i))
    except ValueError:
        intList=['something not int']
    finally:
        inList=[]
print(str(len(intList)))
exit()



arr=[4,3,2][1]
print(arr)
exit()



a={0:1,1:2}
_sum=0
for b in a: _sum+=b-1    
print(_sum + b) 
exit()




a={1:'a',2:'b'}
b={2:'c',3:'d'}
c={**a,**b}
print(c[2])
exit()


exit()
a=[i//2 for i in range(50) if i//2==20]
print(len(a))
exit()
x=0
for i in range(2,20,3): # [2, 5, 8, 11, 14, 17]
    if i%2 ==0:
        print(x)
        x+=1
print(x)

exit()
list1=[1,2]
list2=list1
list3=list1[:]  # python hates beign assigned to ..[] values for list
a=list2 is list1
b=list3 is list1
# print(b)
print(a,b)

exit()
arr=['b','c','d']   #converting list to dictionar bu assiend keys
x={1:'a'}
n=1
for x[n] in arr:
    print(x)
    n+=1
print(x)


exit()
n=0
a=5
b=3
while a>0:
    b+=1
    a-=1
    n+=1
print(n) #5,4,3,2,1
exit()
def rec(x,y):
    if(x==0):
        return y;
    if(x!=0):
        return rec(x-1,y+1);    
print(rec(3,4));

exit()
I=[]
for i in range(17):
    I.append(i*2) #print(I) find all even interger b/n 0-(17-1)*2
m=[x|1 for x in I] #bitwise OR
k=[x&1 for x in I] #bitwise AND
p=[x^1 for x in I] #bitwise XOR
n=[~x for x in I] #bitwise NOT
print(sum(m))
print(sum(k))
print(sum(p))
print(sum(n))

exit()
x=1
while x<5:
    x*=2
print(x)

exit()

a=[]
b=[a,a,a]
print(b)
for x in b:
    n=len(x)
    # print(n)
    x.append(n)
    print(x)
print(b)
print(b[0])
exit()

exit()
A=[8,0,-4,-6,1]
for n in A:
    if n<0:
        print(n)
        A.append(abs(n))
    print(n)
    x=n
print(x)



a=(0)
b=[0],[[0]],{0},[(0)]
print(b)

for i in b:
    print(a in i)



Lh=[1,2,3,4]
print(Lh)
Lh[0]=4
print(Lh)

spam={i:i%3+i for i in range(1,11)}
print(spam)
print(spam[2])
print(spam[4])
print(spam[spam[2]])


print(type(1,))
print(type((1,2)))



paris=[(x,x**2)for x in range(1,5)]
print(paris)
print(paris[2][1])
exit()

# Quick examples of range to a list

# Example 1: Range to list 
# Using * unpacking Operator
myrange = range(5, 10, 1)
mylist = [*myrange]

# Example 2: Range to List using list()
mylist = list(range(10, 20))

# Example 3: Using list() function
mylist = range(10, 20, 1)

# Example 4: Using list comprehension
mylist = [x for x in range(10, 21)]

# Example 5: Range to list 
# Using for loop
myrange = range(5, 15, 2)
my_list = []
for x in myrange:
    my_list.append(x)

# Example 6: Using extend() function
myrange = range(5, 20, 3)
my_list = []
my_list.extend(myrange)

# Example 7: Create an empty list
my_list = []
start, end = 5, 10  
# Check if start value
# smaller than end value
if start < end:
    my_list.extend(range(start, end))
    my_list.append(end)  
    
    

rang=range(20)
mylist=[*rang]
print(mylist)

my="one","tw","thre"

print(my[0])


lst=[]
for val in gen():
    lst.append(int(a==val))
print(sum(lst))


'''





'''_______ Python Tuples             


mytuple = ("apple", "banana", "cherry")
exit()


# Tuples are used to store multiple items in a single variable.



#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
exit()

# Tuple Items
# Ordered
# Unchangeable
# Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
exit()


# Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
exit()

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))
exit()

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
exit()


# Tuple Items - Data Types


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
exit()




tuple1 = ("abc", 34, True, 40, "male")
type()
exit()

# What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
exit()


# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
exit()

# Python Collections (Arrays)

# Python - Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
exit()


# Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
exit()

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
exit()

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
exit()

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
exit()

# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
exit()

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

exit()

# Python - Update Tuples
# Change Tuple Values
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

exit()

# Add Items


# 1. Convert into a list: 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
exit()

# 2. Add tuple to a tuple. 

# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
exit()

# Remove Items
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
exit()


# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

exit()

# Python - Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
exit()



# Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
exit()


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

exit()

# Python - Loop Tuples


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
exit()

# Loop Through the Index Numbers


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
exit()

# Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
exit()

# Python - Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
exit()

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
exit()

# Python - Tuple Methods

# count()	Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
exit()



# index()	Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
exit()


print(b,a)
print(a)
print(b)
print(a is b)
if (a is b):
    print(True)
else:
    print(False)


exit()


t1=(1,2,3)
t2=('a','b','c')
print(tuple(zip(t1,t2)))#[1][0])
print(tuple(zip(t1,t2))[1][0])



tuple .. list
ans=(1,2,3,4)[1]
print(ans)

becha tupples are immitible lets see them in more lively projects 
# okay that is the onlyw ay to udnertstand them..


gh=(1,2,3,4)
print(gh)
# gh(0)=12  # since tuples are immutabligty .. here 
print(gh[0])
gh=(12,2,3,4)
print(gh)




a=("la")
b=("g")
c=a+"o"+b
print(c[::-1])
exit()

# Python Tuple _Immutability example
immutable_string = "Hello"
# The line below creates a new string, it doesn't modify the original one
new_string = immutable_string + " World"


# Python Tuple _Immutability example
immutable_tuple = (1, 2, 3)
# The line below would result in an error since tuples are immutable
# immutable_tuple[0] = 4


# Python Tuple _Immutability example
immutable_number = 42
# The line below creates a new number, it doesn't modify the original one
new_number = immutable_number + 10

'''




'''_______ Python Sets               


# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)
exit()

# Set Items
# Unordered
# Unchangeable
# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
exit()


# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
exit()

# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
exit()

# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))
exit()

# The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
exit()

# Python Collections (Arrays)
# Python - Access Set Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
exit()

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
exit()

# Change Items


# Python - Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
exit()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
exit()

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
exit()

# Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
exit()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
exit()

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
exit()


# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
exit()

# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
exit()

# Python - Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
exit()

# Python - Join Sets

# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
exit()

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
exit()


# Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
exit()


# Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
exit()


# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
exit()

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

exit()

# Python - Set Methods

# add()	Adds an element to the set
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

exit()
fruits = {"apple", "banana", "cherry"}

fruits.add("apple")

print(fruits)
exit()
# clear()	Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
exit()

exit()
# copy()	Returns a copy of the set
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
exit()

exit()
# difference()	Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
exit()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)
exit()
# difference_update()	Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
exit()

exit()
# discard()	Remove the specified item
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
exit()

exit()
# intersection()	Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
exit()
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
exit()
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
exit()
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
exit()
# isdisjoint()	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
exit()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print(z)
exit()
# issubset()	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
exit()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)
exit()
# issuperset()	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
exit()
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
exit()
# pop()	Removes an element from the set
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
exit()
fruits = {"apple", "banana", "cherry"}

x = fruits.pop()

print(x)
exit()
# remove()	Removes the specified element
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
exit()

exit()
# symmetric_difference()	Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
exit()

exit()
# symmetric_difference_update()	inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
exit()

exit()
# union()	Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
exit()
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)
exit()
# update()	Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
exit()

exit()





nums=set([1,1,2,3,3,4])

print(len(nums))

exit()


set={1,3,5,6,8,8,3,2}
print(len(set))   # repetation is not allowed.. 
print(len(set)+int("3"))
exit()


a=[1,5,13,4,19,14]
b=[5,12,48,6,14,1]
c=len(set(a)&set(b))
print(c)

exit()

'''




'''_______ Python Dictionary         


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionary

# Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
exit()

# Dictionary Items




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
exit()

# Ordered or Unordered?
# Changeable
# Duplicates Not Allowed



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
exit()

# Dictionary Length


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(len(thisdict))
exit()



# Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
exit()

# Python Collections (Arrays)
# Python - Access Dictionary Items


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:

exit()

# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
exit()

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.




car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change
car["color"] = "white"

print(x) #after the change
exit()

# Get Values
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
exit()

# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
exit()

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
exit()

# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
exit()

# Check if Key Exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

exit()

# Python - Change Dictionary Items
# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
exit()


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
exit()


# Python - Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
exit()


# Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
exit()


# Python - Remove Dictionary Items
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
exit()

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
exit()

# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
exit()

# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
exit()

# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
print(thisdict)
exit()


# Python - Loop Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
exit()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(thisdict[x])
exit()

# You can also use the values() method to return values of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.values():
  print(x)
exit()

# You can use the keys() method to return the keys of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.keys():
  print(x)
exit()

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


# Python - Copy Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
exit()

# Another way to make a copy is to use the built-in function dict().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
exit()

# Python - Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


exit()


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
exit()

# Python Dictionary Methods

# clear()	Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
exit()

exit()

# copy()	Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)
exit()

exit()

# fromkeys()	Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
exit()
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
exit()

# get()	Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
exit()

# items()	Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)
exit()

# keys()	Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)
exit()

# pop()	Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)
exit()

# popitem()	Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)
exit()

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
exit()

# update()	Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)
exit()

exit()

# values()	Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
exit()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)
exit()




person={"Name":"Sarah","Age":"18"}
person["Name"]="Sia"
person["Age"]="18+"
if "18+" not in person:
    print("a")
else:
    print("b")


exit()



a={1,3,5}
b={2,4,6}
for i in range(7):
    if i not in a and i not in b:
        print(False)
        break
    else:
        print(True)

exit()


person={"Name":"Sarah","Age":"18"}
person["Name"]="Sia"
person["Age"]="18+"
if "18+" not in person:
    print("a")
else:
    print("b")

exit()


# print(type({})==type({1})) # why is this?
print(type([])==type([1]))  #??
print(type(())==type((1,2)))    #??

exit()



# to convert list to dictoinary..
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

t1=(1,2,3)
t2=('a','b','c')
print(tuple(zip(t1,t2))[1][0])



contacts=dict(contacts)    #let it be taught/ treated...as dictonary.. ignoring .get(amanda)
name=input()
if name in contacts:
    print(name, 'is', contacts[name])
else:
    print('not found')

my_dict={"bill":"Gates","steve":"jobs"}
L=[]
# print(my_dict.items()) # .items().. dictionary.. 
# my_dict.append("rich_gy") # . you can' t apend in dictionary

for i,j in my_dict.items():
    L.append(i)
    print(L)
    L.append(j)
    print(L)
# print(len(L))




# method -1 append to list ...coloraly to deicitonary
my_dict = {'key1': 'value1', 'key2': 'value2'}
# Adding a new key-value pair
my_dict['key3'] = 'value3'
print(my_dict)

# method -2 append to list ...coloraly to deicitonary
my_dict = {'key1': 'value1', 'key2': 'value2'}
# Adding/Updating multiple key-value pairs
my_dict.update({'key3': 'value3', 'key4': 'value4'})

print(my_dict)

# method -3 append to list ...coloraly to deicitonary
my_dict = {'key1': 'value1', 'key2': 'value2'}
# Adding/Updating multiple key-value pairs
my_dict.update({'key3': 'value3', 'key4': 'value4'})
print(my_dict)




a={1:[1,2,3]}
b=a.copy()
a[1].append(4)
print(a)
print(a==b)




exit()
dic={1:'X',3:'Y',2:'z'}
for item in dic:
    print(dic[item])
    # print(item)

exit()


my_dict={"Bill":"Gates","Steve":"Jobs"}
L=[]
for i,j in my_dict.items():
    L.append(i)
    L.append(j)
print(len(L))
print(L)

exit()


'''



'''_______ Python If..Else           

# Python If ... Else

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")
exit()

# Indentation

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
exit()

# Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
exit()



# Else



a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
exit()



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
exit()

# Short Hand If

# if a > b: print("a is greater than b")

# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
exit()


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
exit()

# And

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
exit()

# Or

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
exit()

# Nested If



x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
exit()

# The pass Statement

a = 33
b = 200

if b > a:
  pass

exit()

D=3
d=2 if D>0 else 7
print(D)# d=2 if D>0 else 7

exit()


if statments

whq=12      #wht/(ht**2)
whq=wht/(ht**2)

if whq < 18.5:
    print("under wight")     #..// find this caracter.. it is not compatable to sololearns.. 
elif whq > 18.5 and whq<25 :
    print("Normal")
elif whq > 25 and whq<30:
    print("over weight")
elif whq>30:
    print("obesity")


exit()


print("if #condition:")
print("   #statements    ")

x = 42
if x > 5:
    print("x is greater than 5")


exit()

print(" else statment")
exit()

x = 4
if x == 5:
    print("Yes")
else:
    print("No")



exit()   

if d==25//b:
    print(str(d)+str(c))
    
else:
    print("dc")

print("# Boolean Logic")
exit()   

print("if #condition:")
print("   #statements    ")

x = 42
if x > 5:
    print("x is greater than 5")


exit()

print(" else statment")
exit()

x = 4
if x == 5:
    print("Yes")
else:
    print("No")



exit()   

if d==25//b:
    print(str(d)+str(c))
    
else:
    print("dc")
'''



'''_______ Python While Loops        

# Python While Loops

i = 1
while i < 6:
  print(i)
  i += 1
exit()


# The break Statement

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
exit()

# The continue Statement

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
exit()

# The else Statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

exit()  
  

count=0
while(count<5):
    print(count)
    if(count>1):
        count+=1
        break
    else:
        count+=1

x=1
while (x<=5):
    x+=x #x=x+x
   
exit()

i = 1
while i <=5:
   print(i)
   i = i + 1

exit()

#cummulative finder
sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)

exit()


x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

exit()

#"break statment")
i = 0
while True:
  print(i)
  i = i + 1
  
  if i >= 5:
    print("Breaking")
    break

print("Finished")
exit()
#
"continue statment")

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)

exit()



print(" Now this could be considered perfect:  # ticket issue ")
print(" While loop exit problem.... help .. for calculator .. a sorth.. tinkitner")

i = 1
ticket_cost = 100 
total = 0 


print("input 5  numbers")
while i<=5: 
    age = int(input()) 
    if age < 3: 
        i += 1
        continue 
    # break 
    else: 
        total += ticket_cost 
        #print("$" + str(total)) 
        i += 1
print(total) 


i=1
while i<=10:
    print(i+1)
    i*=2

i=1
while i<=10:
    if i==4:
        break
    i+=i
print(i)

exit()


i=1
while i<=10:
    print(''.join(map(str,list(range(i+1)))))
    i*=2

exit()


count=0
while(count<5):
    print(count)
    if(count>1):
        count+=1
        break
    else:
        count+=1
        


x=1
while (x<=5):
    x+=x #x=x+x
    
print(x)

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

exit()

print("cummulative finder")
sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)


exit()


x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

  exit()

print(" # break continue")
exit()

print("break statment")
i = 0
while True:
  print(i)
  i = i + 1
  
  if i >= 5:
    print("Breaking")
    break

print("Finished")
exit()
print("continue statment")

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)

exit()


i = 1
ticket_cost = 100 
total = 0 


print("input 5  numbers")
while i<=5: 
    age = int(input()) 
    if age < 3: 
        i += 1
        continue 
    # break 
    else: 
        total += ticket_cost 
        #print("$" + str(total)) 
        i += 1
print(total) 




i=1
while i<=10:
    print(i+1)
    i*=2


i=1
while i<=10:
    print(''.join(map(str,list(range(i+1)))))
    i*=2

exit()

i=1
while i<=10:
    if i==4:
        break
    i+=i
print(i)

exit()



i=1
while i<=5:
    print(i)
    i+=1


'''




'''_______ Python For Loops          

# Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
exit()


# Looping Through a String

for x in "banana":
  print(x)
exit()

# The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
exit()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
exit()

# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
exit()

# The range() Function

for x in range(6):
  print(x)
exit()


for x in range(2, 6):
  print(x)
exit()



for x in range(2, 30, 3):
  print(x)

exit()

# Else in For Loop


for x in range(6):
  print(x)
else:
  print("Finally finished!")
exit()


# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loops


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
exit()

# The pass Statement

for x in [0, 1, 2]:
  pass

exit()

a=(0)
b=[0],[[0]],{0},[(0)]

for i in b:
    print(a in i)
# [0]  =(0) T
# [[0]]=(0) F
# {0}  =(0) T
# [(0)]=(0) T

exit()


for i in range(5):
    i=i+i
    
print(i)

# other possilble way
exit()
i=0
for x in range(8):
    if x%2==0:
        # print(x)
        i+=x
     # i+=1   

print(i)

num = int(input())
# def printValues():
l = list()
for i in range(0,21):
    l.append(i**2)

for i in l[:num]:
    print(i)

print(l[-num:])


exit()
import itertools as it
for i in it.count(1):
    if(100-i==0):
        break
    print(i)


for i in range(10):
    # print(i)
    if i%2==0:
        continue
        print(i)
    else:
        pass
        print(i)

exit()



a='abcd'
b='defg'
c=''
for i in a:
    if i not in b:
        c+=i
print(c)



for i in range(2):
    print(i)
for i in range(4,6):
    print(i)


exit()

for i in range(7):
    if i not in a and i not in b:
        print(False)
        break
    else:
        print(True)

exit()

for loops
x="hello!"
for i in range(0,len(x)-1):
    print(x[i])

exit()


for i in range(5):
    i=i+i
    
print(i)

# other possilble way
exit()
i=0
for x in range(8):
    if x%2==0:
        # print(x)
        i+=x
     # i+=1   

print(i)

num = int(input())
# def printValues():
l = list()
for i in range(0,21):
    l.append(i**2)

for i in l[:num]:
    print(i)

# print(l[-num:])



exit()
import itertools as it
for i in it.count(1):
    if(100-i==0):
        break
    print(i)


for i in range(10):
    print(i)
if i%2==0:
    continue
    print(i)
else:
    pass
    print(i)

exit()

for i in range(2):
    print(i)
for i in range(4,6):
    print(i)

exit()



x="hello!"
for i in range(0,len(x)-1):
    print(x[i])

exit()
for i in range (10):
    if i>10:
        print("nope")
    else:
        print("done" + str(i))


'''


'''_______ Python Functions          

# Python Functions

# Creating a Function

def my_function():
  print("Hello from a function")
exit()

# Calling a Function

def my_function():
  print("Hello from a function")
exit()
my_function()


# Arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
exit()



# Parameters or Arguments?
# Number of Arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

exit()


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
exit()


# Arbitrary Arguments, *args



def my_function(*kids):
  print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

exit()


# Keyword Arguments



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
exit()



# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
exit()



# Default Parameter Value


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
exit()


# Passing a List as an Argument


exit()
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
Return Values
To let a function return a value, use the return statement:

exit()
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
exit()

# The pass Statement

def myfunction():
  pass
exit()


# Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion exit() Results")
tri_recursion(6)
exit()

def fun():
    pass
x=fun()
print(x=={})

exit()

def Myfunc(num):
    for i in range(5):
        yield num

i=Myfunc(7)
exit()

def calc(x):
    #your code goes here
    return (x*4,x**2)

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))



def func(n):
    y='+'.join(str(x)for x in range(n))
# print('+'.join(str(x)for x in range(7)))
    return (eval(y))
print(func(7))



def func1():
    pass
def func2(n):
    if n%2==0:
        return None
print(func1())
print(func2(3))#6 #3


def sum(a,b):   
    if a==0 or b==0:
        return 0    #exit
    return 1+sum(a-1,b-1) #3,1..1>>2,0..0
    # 1+1+1...
print(sum(23,2))



#from challenges..Function..??
a=()
def func(n):
    k=()
    k=k+n
    return k
    return k
for i in range(0,5,2):
    a+=func((i,i+1))
print(len(a))


def count(n=0):
    while True:
        yield(yield n)
        n+=1
a=count()
next(a)
print(a.send(5),end="")
print(a.send('a'))

def gen():
    global a
    for num in [2,4,8]:
        a+=1
        yield (num*0.5)
a=0.0

# print(gen())


lst=[]
for val in gen():
    lst.append(int(a==val))
print(sum(lst))



def fun(n):
    if(n>100):
        return n-5
    return fun(fun(n+11))

print(fun(2))
# print(fun(105))



Use Pop In Python to Remove an Item and Return It

a=list(range(0,100))
def function(x):
    a.pop(x-1):
    return(a)
for i in range(0,100):
    n=101-i
    function(n)
print(len(a))



cars = ['Mercedes Benz', 'BMW', 'Jeep', 'Mahindra', 'Maserati']

print(cars)

# Using pop() and storing the return value

ret_val = cars.pop(2)

print('The return value is:', ret_val)

# Updated List

print('The updated list is:', cars)



def f(x,a=[]):
    for i in range(x):
        a.append(i*i)
    print(a)

f(2)





def testFunc(x,y=[]):
    y.append(x)
    return y
a= testFunc(1)
b= testFunc(2,[])
c= testFunc(3)
print(c)


a=([{}])
print(a[0])
print(len({}))
print(len(a))
exit()

def fun(arr):
    if len(arr)>0:
        return 1 +fun(arr[0])
    return  1
    
print(fun(a))


def swap(x,y):
    x=x+y;  #14
    y=x-y;  #14-9   5
    x=x-y;  #14-5   9
    return(x,y);
    
print(swap(5,9))
exit()

def f(s1,s2,s3):
    return (int(s1)+int(s2))*str(s3)
    
print(f("1","3",3))


def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
exit()
 
def evens(max):
    v=0
    while v<=max:
        # return v
        yield v
        v+=2
evens(2)
exit()

def my_code():
    return 0
    print(4)
    
print(my_code())
exit()

y=[]
def loop(x):
    for i in x:
        try:
            y.append(int(i))
        except:
            pass
        return y 
print(loop([1.0,"1.0",y,abs(5j+1)]))


def fs(ls,fil):
    f=lambda x:not any(p in x for p in fil)
    return list(filter(f,lst))
f=['$','%']
lst=['$dollar','@at','%modulu']
print(fs(lst,f))
exit()

a=([{}])
a=([])
print(len(a))
# print(a[0])
exit()

def fun (arr):
    if len(arr)>0:
        return 1+fun(arr[0])
    return 1
print(fun(a))
exit()


def fun():
    for x in range(10,0,-1):
        yield(x)
x=fun()
exit()

for a in range(6):
    next(x)

print(next(x))
exit()

def func_a(a,b,c):
    a+=b
    b=a*c
    print(b)
a=10
b=15
c=5.0
func_a(a,b,c) #
exit()


def f(r):
    j=range(r)
    e=eval("*".join([str(i+1)for i in j]))
    return e

print(f(5))
exit()


def search(a,b,*c):
    length=len(c)
    if length is not None:
        print("The variable C holds {} items".format(length))
search(1,2,3,4,5,6,7,8,9,10)


k=0
var="abcb"
for i in var:
    print(i,k)
    k+=1
    
def counts(var):
    for i in var:
        if var.count(i)>1:
            return i
            break

print(counts(var))


exit()

exit()
def f(q,mylist=[]):
    mylist=mylist+q
    return mylist
a=[1]
print(f(a))
a=[2]
print(f(a))
exit()


def a(x):
    return(x*7//5*10%4)
nums=[2,4,8,3,1]
print(a(nums[3]))
exit()


def cm():
    return [lambda x:i*x for i in range(3)]

for m in cm():
    print(m(2),end='')

exit()
def f(x):
    return g(x)+3%2
def g(x):
    return x**2+2
print(f(g(1)))   



exit()

def fun(a):
    x=range(a)
    y=eval('*'.join([str(i+1) for i in x])) #1*,2*3*4*5*6
    return y
x=range(6)
y=[str(i+1) for i in x]
y='*'.join([str(i+1) for i in x])
print(y)
print(fun(6))

exit()


def sub(x,y):
    return(x-y)
def mult(x,y):
    return x*y
def pr(f1,f2,d):
    print(f1(f2(d+1,d),d))
pr(mult,sub,4)

exit()
def f(x):
    return(2*x+1)
def g(x):
    return (x-1)
print(g(f(2))-f(g(2)))

exit()
def f(q,mylist=[]):
    mylist=mylist+q
    return mylist
a=[1]
print(f(a))
a=[2]
print(f(a))

exit()

def guess(list1):
    list2=list1
    list2.append(4)
    list1=[5,6,7]
list1=[1,2,3]
guess(list1)
print(sum(list1))
exit()


def dec(x):
    def f(a,b):
        print("Solo",end="")
        if b==0:
            print("Learn",end="")
            return
        return dec(a,b)
    return f
@dec
def dec(a,b):
    return a/b
dec(3,0)


'''



'''_______ Python Lambda             

# Python Lambda

x = lambda a : a + 10
print(x(5))
exit()

# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))
exit()

# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
exit()


def myfunc(n):
  return lambda a : a * n
exit()

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))
exit()

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
exit()



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

exit()

func=lambda x:x%2==0
abc=list(filter(func,range(8)))
print(sum(abc))
exit()


func=lambda x:x%2==0
abc=list(filter(func,range(8)))
print(sum(abc))
exit()



'''



'''_______ Python Arrays             

# Python Arrays

cars = ["Ford", "Volvo", "BMW"]

# Get the value of the first array item:
x = cars[0]
cars[0] = "Toyota"

# The Length of an Array

x = len(cars)
# Looping Array Elements

print(x)

for x in cars:
  print(x)
exit()

# Adding Array Elements

cars.append("Honda")
exit()

# Removing Array Elements

cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
exit()

# You can also use the remove() method to remove an element from the array.

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
exit()


# Note: The list's remove() method only removes the first occurrence of the specified value.

# Array Methods



# append()	Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
exit()
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
exit()
# clear()	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
exit()

exit()
# copy()	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
exit()

exit()
# count()	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
exit()
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
exit()
# extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
exit()
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
exit()
# index()	Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
exit()
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
exit()
# insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
exit()

exit()
# pop()	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)
exit()
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
exit()
# remove()	Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
exit()

exit()
# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
exit()

exit()
# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
exit()




'''



'''_______ Python Classes/Objects    

# Create a Class


class MyClass: # Create a class named MyClass, with a property named x:
  x = 5
exit()

# Create Object

# Create an object named p1, and print the value of x:

class MyClass: 
  x = 5
p1 = MyClass()
print(p1.x)
exit()


# The __init__() Function

# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
exit()

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Object Methods
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
exit()



# The self Parameter
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
exit()

# Modify Object Properties

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)


p1.age = 40

exit()


# Delete Object Properties
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
del p1.age
exit()

# Delete Objects
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
del p1
exit()


# The pass Statement


class Person:
  pass
exit()



class myclass():
    n=0
    def __init__(self):
        myclass.n+=1
    def __del__(self):
        myclass.n-=1
a=myclass()
print(a.n)
b=myclass()
print(b.n)
a=myclass()
print(b.n)

exit()


class spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
s=spam()
print(s.__egg)

exit()

#os.close(f) # close the descritor f

class myclass:
    def __iter__(self):
        self.x=1
        return obj
    def __next__(self):
        y=self.x
        self.x+=1
        return y
obj=myclass()
it=iter(obj)
print(next(it))
print(next(it))
    
exit()


#send to class object orinted prorgramming.. 
class Class:
    n=3
    def __init__(self,n):
        self.n=n%2
a=Class(5)

print(a.n)
class tower():
    def __init__(self,x=100):
        self.hp=x
A=tower()
B=tower(90)
C=tower()
print(A.hp+B.hp-C.hp)

exit()



def tripler(org_func):
    def my_function(orig_val):
        return(org_func(orig_val)*3)
    return(my_function)

@tripler
def doubler(user_input):
    return(user_input*2)
print(doubler(5))

exit()

class A:
    def __init___(self,value):
        self.a=value
class B(A):
    def __init__(self,value=2):
        super().__init__()
ab=B(8)
print(ab)
# print(ab.a)
exit()


class vec:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vec(self.x+ other.x,self.y+other.y)
v1=vec(3,4)
v2=vec(1,2)
r=v1+v2
print(r.x)
print(r.y)
print(r.x*r.y)

exit()


class foo:
    def bar(self):
        pass

print(foo.bar.__name__)

exit()

from functools import reduce
mul = lambda n1, n2: n1 * n2
class cls:
    def __enter__(self):
        # Return a function that calculates factorial
        def f(n):
            return reduce(mul, range(2, n + 1), 1)
        return f  # Return the factorial function

    def __exit__(self, *args):
        pass

with cls() as a:
    print(a(5))  # Call the returned function a(5) to calculate factorial

exit()

class A:
    @staticmethod
    def sample(self):
        print("static method")
    @classmethod
    def sample(self):
        print("class method")
A.sample()
exit()


class J(str):
    def __init__(self, j):
        self.j=j
    def __add__(self,other):
        self.j+other.j
x=J(5)
y=J(7)
print(x+y)
exit()

exit()
add=lambda x,y: x+y
class Add:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        if type('')in (type(self.n),type(other)):
            return add(str(self.n),str(other))
        return add(self.n,other)

print(Add(7)+'4')

exit()


class Go:
    def __call__(self,x):
        return x
print(Go()(5))
exit()
try:
    print(Go()(5))
except:
    print(0)
exit()





class A:
    def __init__(self):
        self.a=0
    def change(self,n):
        a=n
obj=A()
obj.change(2)
print(obj.a)

'''



'''_______ Python Inheritance        


# Python Inheritance


# Parent class 

# Child class 



# Create a Parent Class


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
exit()

# Create a Child Class

class Student(Person):
  pass
exit()

# Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()
exit()


# Add the __init__() Function
# Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

exit()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
exit()



# Use the super() Function



class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

exit()



# Add Properties

# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

exit()

# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
exit()

# Add Methods

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

exit()




'''


'''_______ Python Itertors           

# Python Iterators  

# An iterator is an object that contains a countable number of values.


# Iterator vs Iterable


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
exit()

# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
# Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
exit()

# Iterate the characters of a string:

mystr = "banana"

for x in mystr:
  print(x)

exit()



# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

exit()

# StopIteration

# Stop after 20 iterations:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

exit()

'''



'''_______ Python Scope              


# Local Scope

# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()
exit()


# Function Inside Function


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
exit()


# Global Scope


# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
exit()


# Naming Variables

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
exit()

# Global Keyword


def myfunc():
  global x
  x = 300

myfunc()

print(x)
exit()




x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

exit()



'''


'''_______ Python Modules            


# What is a Module?

# A file containing a set of functions you want to include in your application.

# Create a Module

def greeting(name):
  print("Hello, " + name)
exit()

# Use a Module

import mymodule
mymodule.greeting("Jonathan")
exit()

# Variables in Module



Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
exit()

# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)
exit()

# Naming a Module


# Re-naming a Module

import mymodule as mx

a = mx.person1["age"]
print(a)
exit()

# Built-in Modules


import platform

x = platform.system()
print(x)
exit()


import platform

x = dir(platform)
print(x)
exit()



# Import From Module

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print (person1["age"])

exit()



'''


'''_______ Python Dates              

# Python Datetime

import datetime
x = datetime.datetime.now()
print(x)
exit()

# Date Output

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
exit()

# Creating Date Objects

Create a date object:

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
exit()



# The strftime() Method

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
exit()

# A reference of all the legal format codes:

# %a	Weekday, short version	Wed	
import datetime

x = datetime.datetime.now()

print(x.strftime("%a"))

exit()

# %A	Weekday, full version	Wednesday	
import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))

exit()

exit()
# %w	Weekday as a number 0-6, 0 is Sunday	3	
import datetime

x = datetime.datetime.now()

print(x.strftime("%w"))

exit()

exit()
# %d	Day of month 01-31	31	
import datetime

x = datetime.datetime.now()

print(x.strftime("%d"))

exit()

exit()
# %b	Month name, short version	Dec	
import datetime

x = datetime.datetime.now()

print(x.strftime("%b"))

exit()

exit()
# %B	Month name, full version	December	
import datetime

x = datetime.datetime.now()

print(x.strftime("%y"))

exit()

exit()
# %m	Month as a number 01-12	12	
import datetime

x = datetime.datetime.now()

print(x.strftime("%m"))

exit()

exit()
# %y	Year, short version, without century	18	
import datetime

x = datetime.datetime.now()

print(x.strftime("%y"))

exit()

exit()
# %Y	Year, full version	2018	
import datetime

x = datetime.datetime.now()

print(x.strftime("%Y"))

exit()

exit()
# %H	Hour 00-23	17	
import datetime

x = datetime.datetime.now()

print(x.strftime("%H"))

exit()

exit()
# %I	Hour 00-12	05	
import datetime

x = datetime.datetime.now()

print(x.strftime("%I"))

exit()

exit()
# %p	AM/PM	PM	
import datetime

x = datetime.datetime.now()

print(x.strftime("%p"))

exit()

exit()
# %M	Minute 00-59	41	
import datetime

x = datetime.datetime.now()

print(x.strftime("%M"))

exit()

exit()
# %S	Second 00-59	08	
import datetime

x = datetime.datetime.now()

print(x.strftime("%S"))

exit()

exit()
# %f	Microsecond 000000-999999	548513	
import datetime

x = datetime.datetime.now()

print(x.strftime("%f"))

exit()

# %j	Day number of year 001-366	365	
import datetime

x = datetime.datetime.now()

print(x.strftime("%j"))

exit()

exit()
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
import datetime

x = datetime.datetime.now()

print(x.strftime("%U"))

exit()

exit()
# %W	Week number of year, Monday as the first day of week, 00-53	52	
import datetime

x = datetime.datetime(2018, 5, 31)

print(x.strftime("%W"))

exit()

exit()
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
import datetime

x = datetime.datetime.now()

print(x.strftime("%c"))

exit()

exit()
# %C	Century	20	
import datetime

x = datetime.datetime.now()

print(x.strftime("%C"))

exit()

exit()
# %x	Local version of date	12/31/18	
import datetime

x = datetime.datetime.now()

print(x.strftime("%x"))

exit()

exit()
# %X	Local version of time	17:41:00	
import datetime

x = datetime.datetime.now()

print(x.strftime("%X"))

exit()

exit()
# %%	A % character	%	
import datetime

x = datetime.datetime.now()

print(x.strftime("%%"))

exit()

exit()
# %G	ISO 8601 year	2018	
import datetime

x = datetime.datetime.now()

print(x.strftime("%G"))

exit()

exit()
# %u	ISO 8601 weekday (1-7)	1	
import datetime

x = datetime.datetime.now()

print(x.strftime("%u"))

exit()

exit()
# %V	ISO 8601 weeknumber (01-53)	01
import datetime

x = datetime.datetime.now()

print(x.strftime("%V"))

exit()

exit()


import time
print(time.sleep(1))    ## used for threading
exit()

'''



'''_______ Python Math               

# Python Math

# Built-in Math Functions



x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
exit()
# The abs() function returns the absolute (positive) value of the specified number:


x = abs(-7.25)
print(x)
exit()




x = pow(4, 3)
print(x)
exit()

# The Math Module



import math

x = math.sqrt(64)
print(x)
exit()



import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1
exit()



exit()
import math
x = math.pi
print(x)

# Complete Math Module Reference


'''


'''_______ Python JSON               

# Python JSON


# JSON is text, written with JavaScript object notation.




# Import the json module:
# Convert from JSON to Python:

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
exit()





# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
exit()


# Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
exit()


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
exit()

# Format the Result


# The json.dumps() method has parameters to make it easier to read the result:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json.dumps(x, indent=4)
exit()



exit()

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result


exit()



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json.dumps(x, indent=4, sort_keys=True)
exit()

'''



''' _______ Python RegEx              


# RegEx Module


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
exit()
# RegEx Functions

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string
# Metacharacters

# []	A set of characters	"[a-m]"	

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

exit()
# #	Signals a special sequence (can also be used to escape special characters)	"\\d"	

 
 


import re


txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\\d", txt)
print(x)

exit()

# .	Any character (except newline character)	"he..o"	



import re
txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

exit()

# ^	Starts with	"^hello"	
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

exit()

# $	Ends with	"planet$"	
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

exit()

# *	Zero or more occurrences	"he.*o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

exit()

# +	One or more occurrences	"he.+o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

exit()

# ?	Zero or one occurrences	"he.?o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

exit()

# {}	Exactly the specified number of occurrences	"he.{2}o"	
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# |	Either or	"falls|stays"	




import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# ()	Capture and group	 	 

exit()



# Special Sequences



# #A	Returns a match if the specified characters are at the beginning of the string	"\\AThe"	
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

exit()

# #b	Returns a match where the specified characters are at the beginning or at the end of a word
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\\bain"
import re

txt = "The rain in Spain"

# Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain#b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# r"ain#b"	
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain#B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()


# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\\Bain"
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\\r", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# r"ain#B"	


# #d	Returns a match where the string contains digits (numbers from 0-9)	"\\d"	
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()


# #D	Returns a match where the string DOES NOT contain digits	"\\D"	
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #s	Returns a match where the string contains a white space character	"\\s"	
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #S	Returns a match where the string DOES NOT contain a white space character	"\\S"	
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\\w"
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #W	Returns a match where the string DOES NOT contain any word characters	"\\W"	

exit()


# #Z	Returns a match if the specified characters are at the end of the string	"Spain#Z"	
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain#Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

exit()



# Sets


# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [^arn]	Returns a match for any character EXCEPT a, r, and n	
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
import re

txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [0-9]	Returns a match for any digit between 0 and 9	
import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
import re

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

 
# The findall() Function



# Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
exit()


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
exit()
# The search() Function



import re

txt = "The rain in Spain"
x = re.search("\\s", txt)
print(x)
# print("The first white-space character is located in position:", x.start())
exit()



import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
exit()
 
# The split() Function



import re

txt = "The rain in Spain"
x = re.split("\\s", txt)
print(x)
exit()






import re

txt = "The rain in Spain"
x = re.split("\\s", txt, 1)
print(x)
exit()
 
# The sub() Function



import re

txt = "The rain in Spain"
x = re.sub("\\s", "9", txt)
print(x)
exit()


import re

txt = "The rain in Spain"
x = re.sub("\\s", "9", txt, 2)
print(x)
exit()
 
# Match Object

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
exit()

# .span() returns a tuple containing the start-, and end positions of the match.
import re

txt = "The rain in Spain"
x = re.search(r"\\bS#w+", txt)
print(x.span())
exit()

# .string returns the string passed into the function
import re

txt = "The rain in Spain"
x = re.search(r"\\bS#w+", txt)
print(x.string)
exit()

# .group() returns the part of the string where there was a match
import re

txt = "The rain in Spain"
x = re.search(r"\bS#w+", txt)
print(x)

exit()



import re
w="coder"
if re.match(w,"code"):
    print("a")
else:
    print("b")

exit()

    


def square_numbers(n):
    for i in range(n):
        yield i ** 2

# Using the generator to iterate over the sequence of squared numbers
my_generator = square_numbers(5)

for num in my_generator:
    print(num)
exit()


import itertools as it
for i in it.count(1):
    if (100-i==0):
        break
    print(i)


A=[1,2,3,4,5,6,7]
G=iter(A)
next(G)
for num in G:
    print(num)
    next(G)
    next(G)
exit()


import re
pattern = r"[\\d]+"
x=re.search(pattern,"good luck in 2017!")
y=x.group()
print(int(y)%100+3)
exit()


import random
print(random.randint(1,20))
exit()


import time
print(time.sleep(1))    ## used for threading
exit()





 '''




'''_______ Python PIP                

# Python PIP

# PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
# A package contains all the files you need for a module.



# Check if PIP is Installed

# pip --version

# Install PIP
# pip install 


# Download a package named "camelcase":

# pip install camelcase

# Using a Package

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

exit()

# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package

# pip uninstall camelcase

# List Packages

# pip list

'''



'''_______ Python Try..Except        

# Python Try Except

# Exception Handling




The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
exit()


# This statement will raise an error, because x is not defined:

print(x)
exit()

# Many Exceptions


exit()
Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Else
# In this exit(), the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
exit()


# Finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
exit()

# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


# Raise an exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
exit()


# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

exit()

from math import sqrt as math
try:
    print(math(4))
except TypeError:
    print("TypeError occured")
except:
    print("An error occured")

exit()
#error handling..exception
try:
    str="Python"
    int=42
    print(int//str)
except TypeError:
    int=12
finally:
    print(int+8)

exit()

try:
    if("hello world"/0==1):
        print(0)
    except ZeroDivisionError:
        print(1)
    except SyntaxError:
        print(2)
    except TypeError:
        print(3)
    finally:    
        print(9)

exit()
a=[4,5,6,7]
try:
    print(a[True])
except:
    print(0)

'''



'''_______ Python User Input         

# Python User Input

username = input("Enter username:")
print("Username is: " + username)
exit()

# Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)
exit()

print("# taking user Input")
hey=input()
print(hey,"<<< this is string don't forget that")
exit()

#working with input
print("input weight:")
wht=float(input())
exit()

print("input height:")
ht=float(input())
exit()

print("name:")
name =input()
print("age:")
age=input()
print(name+ "is"+ age)
exit()

'''


'''_______ Python String Formatting  

# Python String Formatting


# String format()
# The format() method allows you to format selected parts of a string.

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

exit()
# Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"

exit()

# String format() Method.


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))



# Definition and Usage


# The Placeholders



txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

# Formatting Types


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

exit()
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

exit()
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

exit()
#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))

exit()
#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))

exit()
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))

exit()
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))

exit()
#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))

exit()
#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))

exit()
#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))

exit()
#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

exit()
#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

exit()
#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))

exit()
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))

exit()
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))

exit()
#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))

exit()
#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))

exit()
#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))

exit()
#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))

exit()

# Multiple Values

print(txt.format(price, itemno, count))
exit()

# And add more placeholders:


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
exit()

# Index Numbers



quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
exit()


# Also, if you want to refer to the same value more than once, use the index number:


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
exit()

# Named Indexes

myorder = "I have a {carname}, it is a {model}."

print(myorder.format(carname = "Ford", model = "Mustang"))
exit()

'''


'''_______ Python File Handling      

# Python File Open

# File Handling

# "r" - Read 

# "a" - Append 

# "w" - Write 

# "x" - Create

# "t" - Text - Text mode

# "b" - Binary - Binary mode (e.g. images)


# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
exit()

# The code above is the same as:

f = open("demofile.txt", "rt")
exit()


# Note: Make sure the file exists, or else you will get an error.

'''


'''_______ Python Read files         

# exit()
# Python File Open

f = open("demofile.txt", "r")
# f = open("D:\\cNG\\pyth_wbk\\GUI\\demofile.txt", "r")
print(f.read())

exit()

# Open a file on a different location:

f = open("D:\\cNG\\pyth_wbk\\GUI\\demofile.txt", "r")
print(f.read())
# exit()


# Read Only Parts of the File


exit()
# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))
exit()


# Read Lines

# Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())
exit()

# Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
exit()




# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)

exit()

# Close Files
# Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()
exit()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# '''


'''_______ Python Write/Create files 

# Write to an Existing File


# "a" - Append 

# "w" - Write 


# Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
exit()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
exit()

# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
exit()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
exit()



# Create a New File


# "x" - Create 
             
# "a" - Append 
             
# "w" - Write -


# Create a file called "myfile.txt":

f = open("myfile.txt", "x")
exit()

# Result: a new empty file is created!

# Create a new file if it does not exist:

f = open("myfile.txt", "w")
exit()

'''



'''_______ Python Delete files       


# Delete a File



# Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
exit()

# Check if File exist:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
exit()

# Delete Folder

# Remove the folder "myfolder":

import os
os.rmdir("myfolder")
exit()

# Note: You can only remove empty folders.

'''


''' _______ Python Numpy

import numpy as np
 # b=np.array([[2,5],[3,7]])
ak=np.array([[11,[2,2],[2,2],34],[34,34,3]])
ak=ak.transpose();
print(ak)
ar1=np.array([[2,5],[3,7]])
ar1=ar1.transpose();
print(ar1)
exit()


arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
exit()


import numpy as np
a=np.array([1,2,3,5,8])
b=np.array([0,3,4,2,1])
c=a+b
print(c)
c=c*a
print(c)



import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr1=arr1.transpose();
print(arr1[1][0]);
exit()



import numpy as np
a = np.array([[1,2,3],[0,1,4]])
print(a.size)
exit()


import numpy as np
a = np.arange(0, 8, 2)
b = np.arange(1, 8, 3)
print(a[2] == b[1])
exit()


'''


# w3 rsourece
# https://www.w3resource.com/python-exercises/



'''Python Basic (Part -I


#1.Write a Python program to print the following string in a specific format (see the output).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#2.Write a Python program to get the Python version you are using.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-2.html



#3.Write a Python program to display the current date and time
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-3.html



#4.Write a Python program which accepts the radius of a circle from the user and compute the area.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-4.html



#5.Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-5.html



#6.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-6.html



#7.Write a Python program to accept a filename from the user and print the extension of that.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-7.html



#8.Write a Python program to display the first and last colors from the following list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-8.html



#8.Write a Python program to display the first and last colors from the following list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-8.html



#9.Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#10.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#11.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#12.Write a Python program to print the calendar of a given month and year
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#13.Write a Python program to print the following here document.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#14.Write a Python program to calculate number of days between two dates
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#15.Write a Python program to get the volume of a sphere with radius 6
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#16.Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#17.Write a Python program to test whether a number is within 100 of 1000 or 2000.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#18.Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#19.Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#20.Write a Python program to get a string which is n (non-negative integer) copies of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#21.Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#22.Write a Python program to count the number 4 in a given list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#23.Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#24.Write a Python program to test whether a passed letter is a vowel or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#25.Write a Python program to check whether a specified value is contained in a group of values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#26.Write a Python program to create a histogram from a given list of integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#27.Write a Python program to concatenate all elements in a list into a string and return it.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#28.Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#29.Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#30.Write a Python program that will accept the base and height of a triangle and compute the area.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#31.Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#32.Write a Python program to get the least common multiple (LCM) of two positive integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#33.Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#34.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#35.Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#36.Write a Python program to add two objects if both objects are an integer type.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#37.Write a Python program to display your details like name, age, address in three different lines.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#38.Write a Python program to solve (x + y) * (x + y).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#39.Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#40.Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#41.Write a Python program to check whether a file exists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#42.Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#43.Write a Python program to get OS name, platform and release information.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#44.Write a Python program to locate Python site-packages.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#45.Write a python program to call an external command in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#46.Write a python program to get the path and name of the file that is currently executing.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#47.Write a Python program to find out the number of CPUs using.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#48.Write a Python program to parse a string to Float or Integer.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#49.Write a Python program to list all files in a directory in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#50.Write a Python program to print without newline or space.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#51.Write a Python program to determine profiling of Python programs.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#52.Write a Python program to print to stderr.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#53.Write a python program to access environment variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#54.Write a Python program to get the current username
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#55.Write a Python to find local IP addresses using Python's stdlib
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#56.Write a Python program to get height and width of the console window.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#57.Write a program to get execution time for a Python method.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#58.Write a python program to sum of the first n positive integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#59.Write a Python program to convert height (in feet and inches) to centimeters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#60.Write a Python program to calculate the hypotenuse of a right angled triangle.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#61.Write a Python program to convert the distance (in feet) to inches, yards, and miles.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#62.Write a Python program to convert all units of time into seconds.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#63.Write a Python program to get an absolute file path.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#64.Write a Python program to get file creation and modification date/times.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#65.Write a Python program to convert seconds to day, hour, minutes and seconds.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#66.Write a Python program to calculate body mass index.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#67.Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#68.Write a Python program to calculate the sum of the digits in an integer.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#69.Write a Python program to sort three integers without using conditional statements and loops.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#70.Write a Python program to sort files by date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#71.Write a Python program to get a directory listing, sorted by creation date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#72.Write a Python program to get the details of math module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#73.Write a Python program to calculate midpoints of a line.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#74.Write a Python program to hash a word.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#75.Write a Python program to get the copyright information.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#76.Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#77.Write a Python program to test whether the system is a big-endian platform or little-endian platform.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#78.Write a Python program to find the available built-in modules.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#79.Write a Python program to get the size of an object in bytes.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#80.Write a Python program to get the current value of the recursion limit.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#81.Write a Python program to concatenate N strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#82.Write a Python program to calculate the sum over a container.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#83.Write a Python program to test whether all numbers of a list is greater than a certain number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#84.Write a Python program to count the number occurrence of a specific character in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#85.Write a Python program to check if a file path is a file or a directory.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#86.Write a Python program to get the ASCII value of a character.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#87.Write a Python program to get the size of a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#88.Given variables x=30 and y=20, write a Python program to print t "30+20=50".
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#89.Write a Python program to perform an action if a condition is true.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#90.Write a Python program to create a copy of its own source code.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#91.Write a Python program to swap two variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#92.Write a Python program to define a string containing special characters in various forms.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#93.Write a Python program to get the identity of an object.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#94.Write a Python program to convert a byte string to a list of integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#95.Write a Python program to check if a string is numeric.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#96.Write a Python program to print the current call stack.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#97.Write a Python program to list the special variables used within the language.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#98.Write a Python program to get the system time.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#99.Write a Python program to clear the screen or terminal.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#100.Write a Python program to get the name of the host on which the routine is running.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#101.Write a Python program to access and print a URL's content to the console.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#102.Write a Python program to get system command output.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#103.Write a Python program to extract the filename from a given path.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#104.Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#105.Write a Python program to get the users environment.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#106.Write a Python program to divide a path on the extension separator.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#107.Write a Python program to retrieve file properties.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#108.Write a Python program to find path refers to a file or directory when you encounter a path name.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#109.Write a Python program to check if a number is positive, negative or zero.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#110.Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#111.Write a Python program to make file lists from current directory using a wildcard.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#112.Write a Python program to remove the first item from a specified list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#113.Write a Python program to input a number, if it is not a number generate an error message.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#114.Write a Python program to filter the positive numbers from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#115.Write a Python program to compute the product of a list of integers (without using for loop).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#116.Write a Python program to print Unicode characters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#117.Write a Python program to prove that two string variables of same value point same memory location.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#118.Write a Python program to create a bytearray from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#119.Write a Python program to display a floating number in specified numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#120.Write a Python program to format a specified string to limit the number of characters to 6.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#121.Write a Python program to determine if variable is defined or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#122.Write a Python program to empty a variable without destroying it.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#123.Write a Python program to determine the largest and smallest integers, longs, floats.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#124.Write a Python program to check if multiple variables have the same value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#125.Write a Python program to sum of all counts in a collections?
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#126.Write a Python program to get the actual module object for a given object.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#127.Write a Python program to check if an integer fits in 64 bits.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#128.Write a Python program to check if lowercase letters exist in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#129.Write a Python program to add leading zeroes to a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#130.Write a Python program to use double quotes to display strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#131.Write a Python program to split a variable length string into variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#132.Write a Python program to list home directory without absolute path.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#133.Write a Python program to calculate the time runs (difference between start and current time) of a program.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#134.Write a Python program to input two integers in a single line.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#135.Write a Python program to print a variable without spaces between values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#136.Write a Python program to find files and skip directories of a given directory.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#137.Write a Python program to extract single key-value pair of a dictionary in variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#138.Write a Python program to convert true to 1 and false to 0.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#139.Write a Python program to valid a IP address.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#140.Write a Python program to convert an integer to binary keep leading zeros.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#141.Write a python program to convert decimal to hexadecimal.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#142.Write a Python program to find the operating system name, platform and platform release date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#143.Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#144.Write a Python program to check if variable is of integer or string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#145.Write a Python program to test if a variable is a list or tuple or a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#146.Write a Python program to find the location of Python module sources.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#147.Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#148.Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#149.Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html



#150.Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-basic-exercise-1.html


'''

'''Python Basic (Part -II


#1.Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#2.Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#3.Write a Python program to remove and print every third number from a list of numbers until the list becomes empty
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#4.Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#5.Write a Python program to create the combinations of 3 digit combo.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#6.Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#7.Write a Python program to count the number of each character of a given text of a text file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#8.Write a Python program to get the top stories from Google news.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#9.Write a Python program to get a list of locally installed Python modules.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#10.Write a Python program to display some information about the OS where the script is running.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#11.Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#12.Write a Python program to create all possible permutations from a given collection of distinct numbers
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#13.Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#14.Write a Python program to add two positive integers without using the '+' operator.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#15.Write a Python program to check the priority of the four operators (+, -, *, /).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#16.Write a Python program to get the third side of right angled triangle from two given sides.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#17.Write a Python program to get all strobogrammatic numbers that are of length n.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#18.Write a Python program to find the median among three given numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#19.Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#20.Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#21.Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against an given amount.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#22.Write a Python program to create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#23.Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#24.Write a Python program to find the number of divisors of a given integer is even or odd.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#25.Write a Python program to find the digits which are absent in a given mobile number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#26.Write a Python program to compute the summation of the absolute difference of all distinct pairs in an given array (non-decreasing order).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#27.Write a Python program to find the type of the progression (arithmetic progression/geometric progression) and the next successive member of a given three successive members of a sequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#28.Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#29.Write a Python program to find common divisors between two numbers in a given pair.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#30.Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#31.Write a Python program to count the number of carry operations for each of a set of addition problems.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#32.Write a python program to find heights of the top three building in descending order from eight given buildings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#33.Write a Python program to compute the digit number of sum of two given integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#34.Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#35.Write a Python program which solve the equation:
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#36.Write a Python program to compute the amount of the debt in n months. The borrowing amount is $100,000 and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#37.Write a Python program which reads an integer n and find the number of combinations of a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#38.Write a Python program to print the number of prime numbers which are less than or equal to an given integer.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#39.Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed by three given points on the plane surface.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#40.Write a Python program to check if a point (x,y) is in a triangle or not. There is a triangle formed by three points.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#41.Write a Python program to compute and print sum of two given integers (more than or equal to zero). If given integers or the sum have more than 80 digits, print "overflow".
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#42.Write a Python program that accepts six numbers as input and sorts them in descending order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#43.Write a Python program to test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#44.Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers a1, a2, a3, ... an. A subsequence of one element is also a continuous subsequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#45.There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#46.Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#47.Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#48.Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals to another given number (s). Do not use the same digits in a combination.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#49.Write a Python program which reads the two adjoined sides and the diagonal of a parallelogram and check whether the parallelogram is a rectangle or a rhombus.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#50.Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#51.Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#52.Write a Python program to compute the sum of first n given prime numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#53.Write a Python program that accept a even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#54.if you draw a straight line on a plane, the plane is divided into two regions. For example, if you pull two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#55.There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys). Write a Python program to test AB and CD are orthogonal or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#56.Write a Python program to sum of all numerical values (positive integers) embedded in a sentence
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#57.There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#58.When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#59.A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#60.Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all cutting out words from sentences
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#61.Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#62.Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s in the range of 0 to 1000.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html



#63.Write a Python program which adds up columns and rows of given table as shown in the specified figure.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.html


'''

''' Python Programming Puzzles

'''

'''Python Conditional Statements and loops 


#1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#2.Write a Python program to convert temperatures to and from celsius, fahrenheit.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#3.Write a Python program to guess a number between 1 to 9.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#4.Write a Python program to construct the following pattern, using a nested for loop
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#5.Write a Python program that accepts a word from the user and reverse it.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#6.Write a Python program to count the number of even and odd numbers from a series of numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#7.Write a Python program that prints each item and its corresponding type from the following list
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#8.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#9. Write a Python program to get the Fibonacci series between 0 to 50. 
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#10.Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#11.Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#12.Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#13.Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#14.Write a Python program that accepts a string and calculate the number of digits and letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#15.Write a Python program to check the validity of password input by users.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#16.Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#17.Write a Python program to print alphabet pattern 'A'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#18.Write a Python program to print alphabet pattern 'D'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#19.Write a Python program to print alphabet pattern 'E'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#20.Write a Python program to print alphabet pattern 'G'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#21.Write a Python program to print alphabet pattern 'L'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#22.Write a Python program to print alphabet pattern 'M'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#23.Write a Python program to print alphabet pattern 'O'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#24.Write a Python program to print alphabet pattern 'P'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#25.Write a Python program to print alphabet pattern 'R'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#26.Write a Python program to print the following patterns.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#27.Write a Python program to print alphabet pattern 'T'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#28.Write a Python program to print alphabet pattern 'U'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#29.Write a Python program to print alphabet pattern 'X'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#30.Write a Python program to print alphabet pattern 'Z'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#31.Write a Python program to calculate a dog's age in dog's years.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#32.Write a Python program to check whether an alphabet is a vowel or consonant.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#33.Write a Python program to convert month name to a number of days.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#34.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#35.Write a Python program to check a string represent an integer or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#36.Write a Python program to check a triangle is equilateral, isosceles or scalene.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#37.Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#38.Write a Python program to display astrological sign for given date of birth.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#39.Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#40.Write a Python program to find the median of three values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#41.Write a Python program to get next day of a given date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#42.Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#43.Write a Python program to create the multiplication table (from 1 to 10) of a number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html



#44.Write a Python program to construct the following pattern, using a nested loop number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-conditional-exercise-1.html


'''

''' Python: Recursion

'''


''' Python Data Type: String


#1.Write a Python program to calculate the length of a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#2.Write a Python program to count the number of characters (character frequency) in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#3.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#4.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#5.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#7.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#8.Write a Python function that takes a list of words and returns the length of the longest one.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#9.Write a Python program to remove the nth index character from a nonempty string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#10.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#11.Write a Python program to remove the characters which have odd index values of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#12.Write a Python program to count the occurrences of each word in a given sentence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#13.Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#14.Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#15.Write a Python function to create the HTML string with tags around the word(s).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#16.Write a Python function to insert a string in the middle of a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#17.Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#18.Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#19.Write a Python program to get the last part of a string before a specified character.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#20.Write a Python function to reverses a string if it's length is a multiple of 4.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#21.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#22.rite a Python program to sort a string lexicographically.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#23.Write a Python program to remove a newline in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#24.Write a Python program to check whether a string starts with specified characters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#25.Write a Python program to create a Caesar encryption.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#26.Write a Python program to display formatted text (width=50) as output.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#27.Write a Python program to remove existing indentation from all of the lines in a given text.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#28.Write a Python program to add a prefix text to all of the lines in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#29.Write a Python program to set the indentation of the first line.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#30.Write a Python program to print the following floating numbers upto 2 decimal places.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#31.Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#32.Write a Python program to print the following floating numbers with no decimal places.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#33.Write a Python program to print the following integers with zeros on the left of specified width.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#34.Write a Python program to print the following integers with '*' on the right of specified width.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#35.Write a Python program to display a number with a comma separator.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#36.Write a Python program to format a number with a percentage.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#37.Write a Python program to display a number in left, right and center aligned of width 10.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#38.Write a Python program to count occurrences of a substring in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#39.Write a Python program to reverse a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#40.Write a Python program to reverse words in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#41.Write a Python program to strip a set of characters from a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#42.Write a Python program to count repeated characters in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#43.Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#44.Write a Python program to print the index of the character in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#45.Write a Python program to check if a string contains all letters of the alphabet.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#46.Write a Python program to convert a string in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#47.Write a Python program to lowercase first n characters in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#48.Write a Python program to swap comma and dot in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#49.Write a Python program to count and display the vowels of a given text.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#50.Write a Python program to split a string on the last occurrence of the delimiter.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#51.Write a Python program to find the first non-repeating character in given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#52.Write a Python program to print all permutations with given repetition number of characters of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#53.Write a Python program to find the first repeated character in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#54.Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#55.rite a Python program to find the first repeated word in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#56.Write a Python program to find the second most repeated word in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#57.rite a Python program to remove spaces from a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#58.Write a Python program to move spaces to the front of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#59.Write a Python program to find the maximum occurring character in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#60.Write a Python program to capitalize first and last letters of each word of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#61.Write a Python program to remove duplicate characters of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#62.Write a Python program to compute sum of digits of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#63.Write a Python program to remove leading zeros from an IP address.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#64.Write a Python program to find maximum length of consecutive 0's in a given binary string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#65.Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#66.Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#67.Write a Python program to remove all consecutive duplicates of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#68.Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#69.Write a Python program to find the longest common sub-string from two given strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#70.Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#71.Write a Python program to move all spaces to the front of a given string in single traversal.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#72.Write a Python program to remove all consecutive duplicates from a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#73.Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#74.Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#75.Write a Python program to find smallest window that contains all characters of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#76.Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#77.Write a Python program to count number of non-empty substrings of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#78.Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#79.Write a Python program to find smallest and largest word in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html



#80.Write a Python program to count number of substrings with same first and last characters of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/string/python-data-type-string-exercise-1.html


'''

''' Python Data Type: List


#1.Write a Python program to sum all the items in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#2.Write a Python program to multiplies all the items in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#3.Write a Python program to get the largest number from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#4.Write a Python program to get the smallest number from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#6.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#7.Write a Python program to remove duplicates from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#8.Write a Python program to check a list is empty or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#9.Write a Python program to clone or copy a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#10.Write a Python program to find the list of words that are longer than n from a given list of words.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#11.Write a Python function that takes two lists and returns True if they have at least one common member.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#13.Write a Python program to generate a 3*4*6 3D array whose each element is *.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#14.Write a Python program to print the numbers of a specified list after removing even numbers from it.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#15.Write a Python program to shuffle and print a specified list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#16.Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#17.Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#18.Write a Python program to generate all permutations of a list in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#19.Write a Python program to get the difference between the two lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#20.Write a Python program access the index of a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#21.Write a Python program to convert a list of characters into a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#22.Write a Python program to find the index of an item in a specified list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#23.Write a Python program to flatten a shallow list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#24.Write a Python program to append a list to the second list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#25.Write a Python program to select an item randomly from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#26.Write a python program to check whether two lists are circularly identical.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#27.Write a Python program to find the second smallest number in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#28.Write a Python program to find the second largest number in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#29.Write a Python program to get unique values from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#30.Write a Python program to get the frequency of the elements in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#31.Write a Python program to count the number of elements in a list within a specified range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#32.Write a Python program to check whether a list contains a sublist.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#33.Write a Python program to generate all sublists of a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#34.Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#35.Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#36.Write a Python program to get variable unique identification number or string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#37.Write a Python program to find common items from two lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#38.Write a Python program to change the position of every n-th value with the (n+1)th in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#39.Write a Python program to convert a list of multiple integers into a single integer.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#40.Write a Python program to split a list based on first character of word.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#41.Write a Python program to create multiple lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#42.Write a Python program to find missing and additional values in two lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#43.Write a Python program to split a list into different variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#44.Write a Python program to generate groups of five consecutive numbers in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#45.Write a Python program to convert a pair of values into a sorted unique array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#46.Write a Python program to select the odd items of a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#47.Write a Python program to insert an element before each element of a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#48.Write a Python program to print a nested lists (each list on a new line) using the print() function.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#49.Write a Python program to convert list to list of dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#50.Write a Python program to sort a list of nested dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#51.Write a Python program to split a list every Nth element.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#52.Write a Python program to compute the similarity between two lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#53.Write a Python program to create a list with infinite elements.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#54.Write a Python program to concatenate elements of a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#55.Write a Python program to remove key values pairs from a list of dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#56.Write a Python program to convert a string to a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#57.Write a Python program to check if all items of a list is equal to a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#58.Write a Python program to replace the last element in a list with another list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#59.Write a Python program to check if the n-th element exists in a given list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#60.Write a Python program to find a tuple, the smallest second index value from a list of tuples.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#61.Write a Python program to create a list of empty dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#62.Write a Python program to print a list of space-separated elements.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#63.Write a Python program to insert a given string at the beginning of all items in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#64.Write a Python program to iterate over two lists simultaneously.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#65.Write a Python program to access dictionary keys element by index.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#66.Write a Python program to find the list in a list of lists whose sum of elements is the highest.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#67.Write a Python program to find all the values in a list are greater than a specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#68.Write a Python program to extend a list without append.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#69.Write a Python program to remove duplicates from a list of lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#70.Write a Python program to get the depth of a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html



#71.Write a Python program to check if all dictionaries in a list are empty or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.html


'''



''' Python Data Type: List Advanced 

'''


''' Python Data Type: Dictionary 

'''


''' Python Data Types: Dictionary 


#1.Write a Python script to sort (ascending and descending) a dictionary by value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#2.Write a Python script to add a key to a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#3.Write a Python script to concatenate following dictionaries to create a new one.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#4.Write a Python script to check if a given key already exists in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#5.Write a Python program to iterate over dictionaries using for loops.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#7.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#8.Write a Python script to merge two Python dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#9.Write a Python program to iterate over dictionaries using for loops.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#10.Write a Python program to sum all the items in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#11.Write a Python program to multiply all the items in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#12.Write a Python program to remove a key from a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#13.Write a Python program to map two lists into a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#14.Write a Python program to sort a dictionary by key.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#15.Write a Python program to get the maximum and minimum value in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#16.Write a Python program to get a dictionary from an object's fields.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#17.Write a Python program to remove duplicates from Dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#18.Write a Python program to check a dictionary is empty or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#19.Write a Python program to combine two dictionary adding values for common keys.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#20.Write a Python program to print all unique values in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#21.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#22.Write a Python program to find the highest 3 values in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#23.Write a Python program to combine values in python list of dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#24.Write a Python program to create a dictionary from a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#25.Write a Python program to print a dictionary in table format.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#26.Write a Python program to count the values associated with key in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#27.Write a Python program to convert a list into a nested dictionary of keys.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#28.Write a Python program to sort a list alphabetically in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#29.Write a Python program to remove spaces from dictionary keys.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#30.Write a Python program to get the top three items in a shop.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#31.Write a Python program to get the key, value and item in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#32.Write a Python program to print a dictionary line by line.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#33.Write a Python program to check multiple keys exists in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#34.Write a Python program to count number of items in a dictionary value that is a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#35.Write a Python program to sort Counter by value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#36.Write a Python program to create a dictionary from two lists without losing duplicate values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#37.Write a Python program to replace dictionary values with their sum.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html



#38.Write a Python program to match key values in two dictionaries.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.html


'''


''' Python Data Types: Tuple 


#1.Write a Python program to create a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#2.Write a Python program to create a tuple with different data types.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#3.Write a Python program to create a tuple with numbers and print one item.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#4.Write a Python program to unpack a tuple in several variables.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#5.Write a Python program to add an item in a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#6.Write a Python program to convert a tuple to a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#7.Write a Python program to get the 4th element and 4th element from last of a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#8.Write a Python program to create the colon of a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#9.Write a Python program to find the repeated items of a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#10.Write a Python program to check whether an element exists within a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#11.Write a Python program to convert a list to a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#12.Write a Python program to remove an item from a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#13.Write a Python program to slice a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#14.Write a Python program to find the index of an item of a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#15.Write a Python program to find the length of a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#16.Write a Python program to convert a tuple to a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#17.Write a Python program to unzip a list of tuples into individual lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#18.Write a Python program to reverse a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#19.Write a Python program to convert a list of tuples into a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#20.Write a Python program to print a tuple with string formatting.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#21.Write a Python program to replace last value of tuples in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#22.Write a Python program to remove an empty tuple(s) from a list of tuples.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#23.Write a Python program to sort a tuple by its float element.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#24.Write a Python program to count the elements in a list until an element is a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html



#24.Write a Python program to count the elements in a list until an element is a tuple.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tuple/python-tuple-exercise-1.html


'''


''' Python Data Types: Sets 


#1.Write a Python program to create a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#2.Write a Python program to iteration over sets.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#3.Write a Python program to add member(s) in a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#4.Write a Python program to remove item(s) from set
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#5.Write a Python program to remove an item from a set if it is present in the set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#6.Write a Python program to create an intersection of sets.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#7.Write a Python program to create a union of sets.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#8.Write a Python program to create set difference.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#9.Write a Python program to create a symmetric difference.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#10.Write a Python program to issubset and issuperset.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#11.Write a Python program to create a shallow copy of sets.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#12.Write a Python program to clear a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#13.Write a Python program to use of frozensets.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#14.Write a Python program to find maximum and the minimum value in a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#15.Write a Python program to find the length of a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html



#15.Write a Python program to find the length of a set.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/sets/python-sets-exercise-1.html


'''


''' Python Data Type: Collections    

'''


''' Python Data Type: Array 


#1.Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#2.Write a Python program to append a new item to the end of the array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#3.Write a Python program to reverse the order of the items in the array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#4.Write a Python program to get the length in bytes of one array item in the internal representation.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#5.Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#6.Write a Python program to get the number of occurrences of a specified element in an array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#7.Write a Python program to append items from inerrable to the end of the array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#8.Write a Python program to convert an array to an array of machine values and return the bytes representation.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#9.Write a Python program to append items from a specified list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#10.Write a Python program to insert a new item before the second element in an existing array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#11.Write a Python program to remove a specified item using the index from an array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#12.Write a Python program to remove the first occurrence of a specified element from an array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html



#13.Write a Python program to convert an array to an ordinary list with the same items.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/array/python-array-exercise-1.html


'''


''' Python Data Type: Enum    

'''


''' Python Class 

#1.Write a Python class to convert an integer to a roman numeral. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#2.Write a Python class to convert a roman numeral to an integer. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#4.Write a Python class to get all possible unique subsets from a set of distinct integers. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#6.Write a Python class to find the three elements that sum to zero from a set of n real numbers. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#7.Write a Python class to implement pow(x, n). -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#8.Write a Python class to reverse a string word by word. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#9.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#10.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#11.Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html



#12.Write a Python program to get the class name of an instance in Python. -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.html


'''


''' Python Unit Test    

'''


''' Python Exception Handling

'''


''' Python Object-Oriented Programming

'''


''' Python Decorator

'''


''' Python Functional : Functions 


#1.Write a Python function to find the Max of three numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#2.Write a Python function to sum all the numbers in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#3.Write a Python function to multiply all the numbers in a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#4.Write a Python program to reverse a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#6.Write a Python function to check whether a number is in a given range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#7.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#8.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#9.Write a Python function that takes a number as a parameter and check the number is prime or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#10.Write a Python program to print the even numbers from a given list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#11.Write a Python function to check whether a number is perfect or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#12.Write a Python function that checks whether a passed string is palindrome or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#13.Write a Python function that prints out the first n rows of Pascal's triangle.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#14.Write a Python function to check whether a string is a pangram or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#15.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#16.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#17.Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#18.Write a Python program to execute a string containing Python code.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#19.Write a Python program to access a function inside a function.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html



#20.Write a Python program to detect the number of local variables declared in a function.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/python-functions-exercise-1.html


'''


''' Python Functional : Lambda 

'''


''' Python Functional : Map

'''

''' Python Functional : Itertools

'''

''' Python Functional : Filter Functions

'''

''' Python Datetime 


#1.Write a Python script to display the various Date Time formats -
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#2.Write a Python program to determine whether a given year is a leap year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#3.Write a Python program to convert a string to datetime.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#4.Write a Python program to get the current time in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#5.Write a Python program to subtract five days from current date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#6.Write a Python program to convert unix timestamp string to readable date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#7.Write a Python program to print yesterday, today, tomorrow.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#8.Write a Python program to convert the date to datetime (midnight of the date) in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#9.Write a Python program to print next 5 days starting from today.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#10.Write a Python program to add 5 seconds with the current time.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#11.Write a Python program to convert Year/Month/Day to Day of Year in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#12.Write a Python program to get current time in milliseconds in Python
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#13.Write a Python program to get week number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#14.Write a Python program to find the date of the first Monday of a given week.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#15.Write a Python program to select all the Sundays of a specified year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#16.Write a Python program to add year(s) with a given date and display the new date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#17.Write a Python program to drop microseconds from datetime.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#18.Write a Python program to get days between two dates.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#19.Write a Python program to get the date of the last Tuesday.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#20.Write a Python program to test the third Tuesday of a month.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#21.Write a Python program to get the last day of a specified year and month.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#22.Write a Python program to get the number of days of a given month and year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#23.Write a Python program to add a month with a specified date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#24.Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#25.Write a Python program to print a string five times, delay three seconds.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#26.Write a Python program calculates the date six months from the current date using the datetime module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#27.Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates will be 20.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#28.Write a Python program to get the dates 30 days before and after from the current date.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#29.Write a Python program to get the GMT and local current time.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#30.Write a Python program to convert a date to the timestamp.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#31.Write a Python program to convert a string date to the timestamp.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#32.Write a Python program to calculate a number of days between two dates.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#33.Write a Python program to calculate no of days between two datetimes.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#34.Write a Python program to display the date and time in a human-friendly string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#35.Write a Python program to convert a date to Unix timestamp.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#36.Write a Python program to calculate two date difference in seconds.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#37.Write a Python program to convert two date difference, in days, hours, minutes, seconds.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#38.Write a Python program to get last modified information of a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#39.Write a Python program to calculate an age in year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#40.Write a Python program to get the current date time information.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#41.Write a python program to generate a date and time as a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#42.Write a Python program to display formatted text output of a month and start weeks on Sunday.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#43.Write a Python program to print a 3-column calendar for an entire year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#44.Write a Python program to display a calendar for a locale.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#45.Write a Python program to get the current week.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#46.Write a Python program to create an HTML calendar with data for a specific year and month.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#47.Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#48.Write a Python program to display a simple, formatted calendar of a given year and month.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#49.Write a Python program to convert a string into datetime
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#50.Write a Python program to get a list of dates between two dates.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#51.Write a Python program to generate RFC 3339 timestamp.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html



#52.Write a Python program to get the first and last second.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.html


'''

''' Python Datetime Pendulum Module

'''


''' Python File Input Output 


#1.Write a Python program to read an entire text file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#2.Write a Python program to read first n lines of a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#3.Write a Python program to append text to a file and display the text.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#4.Write a Python program to read last n lines of a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#5.Write a Python program to read a file line by line and store it into a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#6.Write a Python program to read a file line by line store it into a variable.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#7.Write a Python program to read a file line by line store it into an array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#8.Write a python program to find the longest words.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#9.Write a Python program to count the number of lines in a text file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#10.Write a Python program to count the frequency of words in a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#11.Write a Python program to get the file size of a plain file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#12.Write a Python program to write a list to a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#13.Write a Python program to copy the contents of a file to another file .
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#14.Write a Python program to combine each line from first file with the corresponding line in second file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#15.Write a Python program to read a random line from a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#16.Write a Python program to assess if a file is closed or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html



#17.Write a Python program to remove newline characters from a file.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/file/python-io-exercise-1.html


'''

''' Python File CSV Read, Write

'''

''' Python Regular Expression 


#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#2.Write a Python program that matches a string that has an a followed by zero or more b's.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#3.Write a Python program that matches a string that has an a followed by one or more b's.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#4.Write a Python program that matches a string that has an a followed by zero or one 'b'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#5.Write a Python program that matches a string that has an a followed by three 'b'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#6.Write a Python program that matches a string that has an a followed by two to three 'b'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#7.Write a Python program to find sequences of lowercase letters joined with a underscore.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#8.Write a Python program to find sequences of one upper case letter followed by lower case letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#9.Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#10.Write a Python program that matches a word at the beginning of a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#11.Write a Python program that matches a word at end of string, with optional punctuation.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#12.Write a Python program that matches a word containing 'z'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#13.Write a Python program that matches a word containing 'z', not start or end of the word.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#14.Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#15.Write a Python program where a string will start with a specific number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#16.Write a Python program to remove leading zeros from an IP address.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#17.Write a Python program to check for a number at the end of a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#18.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#19.Write a Python program to search some literals strings in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#20.Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#21.Write a Python program to find the substrings within a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#22.Write a Python program to find the occurrence and position of the substrings within a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#23.Write a Python program to replace whitespaces with an underscore and vice versa.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#24.Write a Python program to extract year, month and date from a an url.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#25.Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#26.Write a Python program to match if two words from a list of words starting with letter 'P'.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#27.Write a Python program to separate and print the numbers of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#28.Write a Python program to find all words starting with 'a' or 'e' in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#29.Write a Python program to separate and print the numbers and their position of a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#30.Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#31.Write a Python program to replace all occurrences of space, comma, or dot with a colon.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#32.Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#33.Write a Python program to find all five characters long word in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#34.Write a Python program to find all three, four, five characters long words in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#35.Write a Python program to find all words which are at least 4 characters long in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#36.Write a python program to convert camel case string to snake case string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#37.Write a python program to convert snake case string to camel case string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#38.Write a Python program to extract values between quotation marks of a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#39.Write a Python program to remove multiple spaces in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#40.Write a Python program to remove all whitespaces from a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#41.Write a Python program to remove everything except alphanumeric characters from a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#42.Write a Python program to find urls in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#43.Write a Python program to split a string at uppercase letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#44.Write a Python program to do a case-insensitive string replacement.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#45.Write a Python program to remove the ANSI escape sequences from a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#46.Write a Python program to find all adverbs and their positions in a given sentence.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#47.Write a Python program to split a string with multiple delimiters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#48.Write a Python program to check a decimal with a precision of 2.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#49.Write a Python program to remove words from a string of length between 1 and a given number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#50.Write a Python program to remove the parenthesis area in a string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#51.Write a Python program to insert spaces between words starting with capital letters.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#52.Write a Python program that reads a given expression and evaluates it.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#53.Write a Python program to remove lowercase substrings from a given string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html


'''


''' Python: Data Structures 


#1.Write a Python program to create an Enum object and display a member name and value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#2.Write a Python program to iterate over an enum class and display individual member and their value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#3.Write a Python program to display all the member name of an enum class ordered by their values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#4.Write a Python program to get all values from an enum class.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#5.Write a Python program to count the most common words in a dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#6.Write a Python program to find the class wise roll number from a tuple-of-tuples.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#7.Write a Python program to count the number of students of individual class.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#8.Write a Python program to get the unique enumeration values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#9.Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#10.Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#11.Write a Python program to compare two unordered lists (not sets).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#12.Write a Python program to create an array contains six integers. Also print all the members of the array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#13.Write a Python program to get the array size of types unsigned integer and float.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#14.Write a Python program to get an array buffer information.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#15.Write a Python program to get the length of an array.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#16.Write a Python program to convert an array to an ordinary list with the same items.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#17.Write a Python program to convert an array to an array of machine values and return the bytes representation.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#18.Write a Python program to read a string and interpreting the string as an array of machine values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#19.Write a Python program to push three items into the heap and print the items from the heap.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#20.Write a Python program to push three items into a heap and return the smallest item from the heap. Also Pop and return the smallest item from the heap.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#21.Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#22.Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#23.Write a Python program to get the two largest and three smallest items from a dataset.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#24.Write a Python program to locate the left insertion point for a specified value in sorted order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#25.Write a Python program to locate the right insertion point for a specified value in sorted order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#26.Write a Python program to insert items into a list in sorted order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#27.a Python program to create a queue and display all the members and size of the queue.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#28.Write a Python program to find whether a queue is empty or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#29.Write a Python program to create a FIFO queue.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html



#30.Write a Python program to create a LIFO queue.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-1.html


'''


'''Python: Data Strucutures: Search and Sorting

'''


'''Python: Data Strucutures: Linked List

'''


'''Python: Data Strucutures: Binary Search Tree

'''

'''Python: Data Strucutures: Heap queue algorithm

'''

'''Python: Data Strucutures: Bisect

'''

'''Python: Advanced Data Types : Boolean Data type

'''

'''Python: Advanced Data Types : None Data type

'''

'''Python: Advanced Data Types : Bytes and Bytes Data type

'''

'''Python: Advanced Data Types : Memory Views 

'''

'''Python: Advanced Data Types : Frozenset Views

'''

'''Python: Advanced Data Types : NamedTuple

'''

'''Python: Advanced Data Types :OrderedDict

'''

'''Python: Advanced Data Types : Counter

'''

'''Python: Advanced Data Types : Ellipsis

'''

'''Python: Concurency and Threading: Threading

'''


'''Python: Concurency and Threading: Asynchronous

'''

'''Python: Modules: Modules

'''


'''Python: Modules: Operating System Services

'''


'''Python: Modules: Math

'''



'''Python: Modules: Math


#1.Write a Python program to convert degree to radian.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#2.Write a Python program to convert radian to degree.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#3.Write a Python program to calculate the area of a trapezoid.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#4.Write a Python program to calculate the area of a parallelogram.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#5.Write a Python program to calculate surface volume and area of a cylinder.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#6.Write a Python program to calculate surface volume and area of a sphere.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#7.Write a Python program to calculate arc length of an angle.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#8.Write a Python program to calculate the area of the sector.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#9.Write a Python program to calculate the discriminant value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#10.Write a Python program to find the smallest multiple of the first n numbers. Also, display the factors.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#11.Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.(default value of number=2).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#12.Write a Python program to calculate the sum of all digits of the base to the specified power.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#13.Write a Python program to find out, if the given number is abundant.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#14.Write a Python program to sum all amicable numbers from 1 to specified numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#15.Write a Python program to returns sum of all divisors of a number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#16.Write a Python program to print all permutations of a given string (including duplicates).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#17.Write a Python program to print the first n Lucky Numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#18.Write a Python program to computing square roots using the Babylonian method.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#19.Write a Python program to multiply two integers without using the * operator in python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#20.Write a Python program to calculate magic square.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#21.Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#22.Write a python program to find the next smallest palindrome of a specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#23.Write a python program to find the next previous palindrome of a specified number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#24.Write a Python program to generate all permutations of a list in Python.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#25.Write a Python program for nth Catalan Number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#26.Write a Python program to print number with commas as thousands separators.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#27.Write a Python program to calculate the distance between two points using latitude and longitude.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#28.Write a Python program to calculate the area of regular polygon.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#29.Write a Python program to calculate wind chill index.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#30.Write a Python program to find the roots of a quadratic function.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#31.Write a Python program to convert a decimal number to binary number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#32.Write a Python program to print a complex number and its real and imaginary parts.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#33.Write a Python program to add, subtract, multiply and division of two complex numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#34.Write a Python program to get the length and the angle of a complex number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#35.Write a Python program to convert to/from rectangular coordinates to Polar coordinates.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#36.Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#37.Write a Python program to find the sum of the following decimal numbers and display the numbers in sorted order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#38.Write a Python program to get the square root and exponential of a given decimal number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#39.Write a Python program to retrieve the current global context (public properties) for all decimal.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#40.Write a Python program to round a specified decimal by setting precision (between 1 and 4).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#41.Write a Python program to round a specified number upwards towards infinity and down towards negative infinity of precision 4.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#42.Write a Python program to get the local and default precision.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#43.Write a Python program to display the fraction instances of the string representation of a number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#44.Write a Python program to create the fraction instances of float numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#45.Write a Python program to create the fraction instances of decimal numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#46.Write a Python program to add, subtract, multiply and divide two fractions.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#47.Write a Python program to convert a floating point number (PI) to an approximate rational value on the various denominator.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#48.Write a Python program to generate random float numbers in a specific numerical range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#49.Write a Python program to generate random integers in a specific numerical range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#50.Write a Python program to generate random even integers in a specific numerical range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#51.Write a Python program to get a single random element from a specified string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#52.Write a Python program to shuffle the following elements randomly.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#53.Write a Python program to flip a coin 1000 times and count heads and tails.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#54.Write a Python program to print a random sample of words from the system dictionary.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#55.Write a Python program to randomly select an item from a list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#56.Write a Python program to calculate the absolute value of a floating point number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#57.Write a Python program to calculate the standard deviation of the following data.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#58.Write a Python program to print the floating point from mantissa, exponent pair.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#59.Write a Python program to split fractional and integer parts of a floating point number.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#60.Write a Python program to parse math formulas and put parentheses around multiplication and division.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#61.Write a Python program to describe linear regression.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#62.Write a Python program to calculate a grid of hexagon coordinates of the given radius given lower-left and upper-right coordinates. The function will return a list of lists containing 6 tuples of x, y point coordinates. These can be used to construct valid regular hexagonal polygons.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#63.Write a Python program to create a simple math quiz.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#64.Write a Python program to calculate the volume of a tetrahedron.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#65.Write a Python program to compute the value of e(2.718281827...) using infinite series.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#66.Write a Python program to create an ASCII waveform.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#67.Write a Python program to create a dot string.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#68.Write a Python program to create a Pythagorean theorem calculator.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#69.Write a Python function to round up a number to specified digits.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#70.Write a Python program for casino simulation.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#71.Write a Python program to reverse a range.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#72.Write a Python program to create a range for floating numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#73.Write a Python program to generate (given an integer n) a square matrix filled with elements from 1 to n2 in spiral order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#74.Write a Python program to select a random date in the current year.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#75.Write a Python program to calculate clusters using Hierarchical Clustering method.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#76.Write a Python program to implement Euclidean Algorithm to compute the greatest common divisor (gcd).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#77.Write a Python program to convert RGB color to HSV color.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#78.Write a Python program to find perfect squares between two given numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#79.Write a Python program to compute Euclidean distance.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#80.Write a Python program to convert an integer to a 2 byte Hex value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#81.Write a Python program to generate a series of unique random numbers.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html



#82.Write a Python program to convert a float to ratio.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/re/python-re-exercise-1.html


'''
''' Python tkinter:basic 


#1.Write a Python GUI program to import Tkinter package and create a window and set its title.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-1.html



#2.Write a Python GUI program to import Tkinter package and create a window. Set its title and add a label to the window.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-1.html



#3.Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-1.html



#4.Write a Python GUI program to create a window and set the default window size using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-1.html



#5.Write a Python GUI program to create a window and disable to resize the window using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-1.html


'''



'''Python: Modules: Request

'''


'''Python: Modules: SQLite Database

'''


'''Python: Modules: SQLAlchemy

'''


'''Python: Modules: PPrint

'''


'''Python: Miscellaneous: Cyber Security

'''


'''Python: Miscellaneous: Generators Yield

'''


'''Python: Tkinter: Basic

'''

'''Python: Tkinter: Layout

'''

'''Python: Tkinter: Managment

'''

'''Python: Tkinter: Widgets

'''

'''Python: Tkinter: Dialogue and File Handling

'''

'''Python: Tkinter: Canavas and Graphics

'''

'''Python: Tkinter: Events and Event Handling

'''

'''Python: Tkinter: Custom Widgets and Themes

'''

'''Python: Tkinter: File operation and Integration

'''


'''Python PyQt: Basic

'''


'''Python PyQt: Widgets

'''


'''Python PyQt: Connecting Signals to Slots

'''


'''Python PyQt: Event Handling

'''


'''Python NumPy: 

'''
 

'''Python urllib3:

'''


'''Python GeoPy 

'''


'''Python BeautifulSoup 

'''


'''Python Arrow 

'''


'''Python Pandas: 

'''

'''Python Pandas: Data Series

'''

'''Python Pandas: DataFrame

'''

'''Python Pandas: Indexing

'''

'''Python Pandas: Pandas String and Regular Expression

'''

'''Python Pandas: Joining and merging DataFrame

'''

'''Python Pandas: Time Series

'''

'''Python Pandas: Filter

'''

'''Python Pandas: Grouping and Aggregating: Split-Apply-Combine

'''

'''Python Pandas: Handling Missing Values

'''

'''Python Pandas: Styling

'''

'''Python Pandas: Excel

'''

'''Python Pandas: Pivot Table

'''

'''Python Pandas: Datetime

'''

'''Python Pandas: Plotting

'''

'''Python Pandas: SQL Query

'''

'''Python IMDb Movies Data

'''

'''Python Machine learning: 

'''

'''Python TensorFlow :Basics 

'''

'''Python TensorFlow : building and training a simple model:

'''

'''Python Web ScrapingWeb Scraping : 

'''

'''Python TensorFlow : 

'''


''' Python tkinter: widgets 


#1.Write a Python GUI program to add a button in your application using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#2.Write a Python GUI program to add a canvas in your application using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#3.Write a Python GUI program to create two buttons exit and hello using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#4.Write a Python GUI program to create a Combobox with three options using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#5.Write a Python GUI program to create a Checkbutton widget using tkinter module
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#6.Write a Python GUI program to create a Spinbox widget using tkinter module
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#7.Write a Python GUI program to create a Text widget using tkinter module. Insert a string at the beginning then insert a string into the current text. Delete the first and last character of the text
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#8.Write a Python GUI program to create three single line text-box to accept a value from the user using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#9.Write a Python GUI program to create three radio buttons widgets using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#10.Write a Python GUI program to create a ScrolledText widgets using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#11.rite a Python GUI program to create a Progress bar widgets using tkinter module
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html



#12.Write a Python GUI program to create a Listbox bar widgets using tkinter module.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/tkinter/python-tkinter-widgets-exercise-1.html


'''


''' Python Data Structures and Algorithms : Search and Sorting 


#1.Write a Python program for binary search.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#2.Write a Python program for sequential search.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#3.Write a Python program for binary search for an ordered list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#4.Write a Python program to sort a list of elements using the bubble sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#5.Write a Python program to sort a list of elements using the selection sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#6.Write a Python program to sort a list of elements using the insertion sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#7.Write a Python program to sort a list of elements using shell sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#8.Write a Python program to sort a list of elements using the merge sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#9.Write a Python program to sort a list of elements using the quick sort algorithm.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#10.Write a Python program for counting sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#11.Write a Python code to create a program for Bitonic Sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#12.Write a Python program to sort a list of elements using Bogosort sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#13.Write a Python program to sort a list of elements using Gnome sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#14.Write a Python program to sort a list of elements using Cocktail shaker sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#15.Write a Python program to sort a list of elements using Comb sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#16.Write a Python program to sort a list of elements using Cycle sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#17.Write a Python program to sort a list of elements using Heap sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#18.Write a Python program to sort a list of elements using Pancake sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#19.Write a Python program to sort a list of elements using Radix sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#20.Write a Python program to sort a list of elements using Selection sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#21.Write a Python program to sort a list of elements using Time sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#22.Write a Python program to sort a list of elements using Topological sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html



#23.Write a Python program to sort a list of elements using Tree sort.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.html


'''

''' Python: Linked List 


#1.Write a Python program to create a singly linked list, append some items and iterate through the list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#2.Write a Python program to find the size of a singly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#3.Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#4.Write a Python program to access a specific item in a singly linked list using index value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#5.Write a Python program to set a new value of an item in a singly linked list using index value.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#6.Write a Python program to delete the first item from a singly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html

    

#7.Write a Python program to delete the last item from a singly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#8.Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#9.Write a Python program to create a doubly linked list and print nodes from current position to first node.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#10.Write a Python program to count the number of items of a given doubly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#11.Write a Python program to print a given doubly linked list in reverse order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#12.Write a Python program to insert an item in front of a given doubly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#13.Write a Python program to search a specific item in a given doubly linked list and return true if the item is found otherwise return false.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#14.Write a Python program to delete a specific item from a given doubly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html



#14.Write a Python program to delete a specific item from a given doubly linked list.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list-exercise-1.html


'''

''' Python: Binary Search Tree (BST


#1.Write a Python program to create a Balanced Binary Search Tree (BST) using an array (given) elements where array elements are sorted in ascending order.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



#2.Write a Python program to find the closest value of a given target value in a given non-empty Binary Search Tree (BST) of unique values.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



#3.Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



#4.Write a Python program to delete a node with the given key in a given Binary search tree (BST).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



#5.Write a Python program to convert a given array elements to a height balanced Binary Search Tree (BST).
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



#6.Write a Python program to find the kth, smallest element in a given a binary search tree.
#file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.html



'''


''' Data Structures and Algorithms: Recursion 


# 1.Write a Python program to calculate the sum of a list of numbers.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 2.Write a Python program to converting an Integer to a string in any base.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 3.Write a Python program of recursion list sum.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 4. Write a Python program to get the factorial of a non-negative integer. 
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 5.Write a Python program to solve the Fibonacci sequence using recursion.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 6.Write a Python program to get the sum of a non-negative integer.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 7.Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 8.Write a Python program to calculate the harmonic sum of n-1.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 9.Write a Python program to calculate the geometric sum of n-1.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 10.Write a Python program to calculate the value of 'a' to the power 'b'.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html



# 11.Write a Python program to find the greatest common divisor (gcd) of two integers.
# file:///D:/cNG/W3Resource%20Offline%20Dec%202019_2/W3Resource%20Offline%20Dec%202019/www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.html


'''




