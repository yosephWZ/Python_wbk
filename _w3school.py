# @#$!@#$@!#$Progress### << ///Feb_2024..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$
# !!!!! don't stay at one part for more than 1 weekds...!!!!
# !!!!! proceed as you go through by commenting .. for furhter refirinement..
# //..//...//..//...//..//..//..//...//
# //..//..Code explanation.//..use...//.ChatGPT.//..//..//...//
# //..//...//..//..codeChalenge..//..//..//..//..sololearn..//


exit()

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




variables
    # my_num=1234
    # a=str(my_num//1000%10) #print(1%10)
    # b=str(my_num//100%10) #print(12%10)
    # c=str(my_num//10%10) #print(123%10)
    # d=str(my_num//1%10) #print(1234%10)
    # print(d+c+b+a)
    # exit()


variables
    # val=3
    # print(val is None)


variables
    # x = 10
    # y = 20
    # expression = 'x + y'  # This is a string representing a Python expression

    # result = eval(expression)  # Evaluating the expression using eval()

    # print(result)  # Output will be 30 (since x + y = 10 + 20)

'''



'''_______ Python Data Types         
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

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection


# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

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


# For numbers, the + character works as a mathematical operator:
exit()

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


# Python Numbers

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

# Random Number __Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))




# print(7//2) # floor quoteent
# print(13%2) # modular operator remainder
# print("Welcome to the Code Playground")            #https://peps.python.org/pep-0008/

# print("this is one");print("this is again")
# exit()


#print("#working with Numberical data")
#6.17. Operator precedence  #https://docs.python.org/3/reference/expressions.html
# print(6/2*3**2)
# print(6/2*3)
# print(5+6/2*3)
# print(7-5+6/2*3)
exit()


# a=range(6)
# r=a[3+1]*4%3    #operator precedance..?? Multiply after modulo
# print(r)
exit()

# print(pow(2,2,3))#(same as (2 * 2 * 2) % 5):
# print("Workign with Text data")
exit()

# from fractions import Fraction
# frac=Fraction(2,5)
# print(frac*10)
exit()

# a=1
# B=a+1
# print(B,end="")
# print(B,a,sep="0")
# print(int(1+2-3*4/5%6))
exit()

# import random
# x=random.randint(0,120)%55
# print(x)
exit()

# print(int(abs(5j+1)))# complex number
# print("".join(['h','i']))
exit()

# x=1024
# print(isinstance(x,str))
exit()

h="234"
i=2
# print("{}{}".format(*['h','i']))
exit()

exit()
# a=2
# b=3;
# c="{a}{b}{ab}";
# d=c.format(a=4,b=5,ab=a*b);
# print(d)

exit()

# print("shdfdf"[3])
exit()

# print("helower"+"pyton user")
exit()

# str="3434 this is a string"

# print(str.partition('is'))  # creates a partition.. add to tuples..
exit()

# print(True+ False)
exit()
# s="hello"
# print(*s)
exit()

# s='abc'   
# i=iter(s)
# print(next(i))   #https://www.geeksforgeeks.org/python-next-method/
# print(next(i))
# print(next(i))
exit()

# print("Mixing things up")
# print(9 + 4 - 7)
# print(9//4) #divide 9 how much to 4....that is...becomes...2
# print(9%2)  #modular..///remander.. left for 9 to 2.. that is becomes...1
# print(1%2)
exit()

# # #data types... 
# print(type("0"))
# print(type(2.04))
# print(type(2))
# print(float(4))       #float
# print(str(6)+str(5))  #string
# print(int(5.0))       #integer 
# print(chr(71))        # chr() builtin function
# print("hey man"+ "i am good") #concatination
exit()

# import math
# a=pow(6,7)
# b=math.pow(6,7)
# print(a)
# print(b)
exit()

# print("Balance", 5000,sep=":")
# print(4%5) #is 4 .. any thing less than ... would be itself
exit()

# a=list(range(6))
# print(a[4])

exit()


# x=(1,2,3)
# print(*x)
# print(*x,sep="1")
# print(*x,sep="1",end="3")

exit()

# print("Iron", "Man", sep ="-")


exit()
#print("Labeling, Storing and Handling Data with Variables")
# x = 42       #integer
# y = "Hello"  #string
# z = 3.14     #float
exit()

# print(type(1J))   # complex number

 exit()
# from math import sqrt as sty
# print(sqrt(4))
# print(sty(4))

# name="palul"
# print("his {0} is ".format(name))

exit()


# name = "palul"
# print("his {0} is".format(name))

# name = "palul"
# print(f"his {name} is")

exit()


exit()
# x="2"
# print(int(x)) #convert to string
# print(float(x)) # convert to float
# print(int(9.04)) # convert to int

data types 

    # print((1j**2).real)
    # exit()

    # a=chr(65)
    # b=ord("a") 
    # print(a==chr(b))

    # exit()


data types

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
Specify a Variable Type

# Casting in python is therefore done using constructor functions:
int() - constructs 
float() - constructs
str() - constructs 


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
exit()
Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
exit()
Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''




''' _______Python Strings

Python Strings
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

exit()
print("Hello")
print('Hello')
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

exit()
a = "Hello"
print(a)
Multiline Strings
You can assign a multiline string to a variable by using three quotes:

exit()
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
Or three single quotes:

exit()


print(a)
Note: in the result, the line breaks are inserted at the same position as in the code.

Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

exit()
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.

exit()
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
Learn more about For Loops in our Python For Loops chapter.

String Length
To get the length of a string, use the len() function.

exit()
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.

exit()
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
Use it in an if statement:

exit()
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
Learn more about If statements in our Python If...Else chapter.

Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

exit()
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
Use it in an if statement:

exit()
print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



Python - Slicing Strings
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

exit()
Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
Note: The first character has index 0.

Slice From the Start
By leaving out the start index, the range will start at the first character:

exit()
Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])
Slice To the End
By leaving out the end index, the range will go to the end:

exit()
Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
Negative Indexing
Use negative indexes to start the slice from the end of the string:
exit()
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])




Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

Upper Case
exit()
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
Lower Case
exit()
The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

exit()
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
Replace String
exit()
The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
Split String
The split() method returns a list where the text between the specified separator becomes the list items.

exit()
The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
Learn more about Lists in our Python Lists chapter.

String Methods
Learn more about String Methods with our String Methods Reference



Python - String Concatenation
String Concatenation
To concatenate, or combine, two strings you can use the + operator.

exit()
Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)
exit()
To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)



Python - Format - Strings
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

exit()
age = 36
txt = "My name is John, I am " + age
print(txt)
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

exit()
Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

exit()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

exit()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
Learn more about String Formatting in our String Formatting chapter.



Python - Escape Characters
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An exit() of an illegal character is a double quote inside a string that is surrounded by double quotes:

exit()
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."
To fix this problem, use the escape character \":

exit()
The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
Escape Characters
Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value


Python - String Methods
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

exit()

print("gameofdice"[::2])

string

# print("joining by converting each string to ord of \"hello world\"")
# s = "hello world"
# print(''.join(str(ord(c)) for c in s))

# exit()


string
    # print(len(str(8/2**2**2)))
    # exit()
    # x=0b0010
    # print(x)
    # exit()

string
    # str1="5"
    # str2="6"
    # print(str1<str2)
    # exit()


string
    # s='think'
    # s=''.join(sorted(list(s)[:4]))
    # print(s)
    # exit()

    # a='solo'
    # print(a.zfill(6))
    # exit()


# print("joining by converting each string to ord of \"hello world\"")
# s = "hello world"
# print(''.join(str(ord(c)) for c in s))

# exit()

# str1="5"
# str2="6"
# print(str1<str2)
# exit()



# s='think'
# s=''.join(sorted(list(s)[:4]))
# print(s)
# exit()
# a='solo'
# print(a.zfill(6))
# exit()



    # strt = "Hello world!"
    # print(strt[6])

'''
   
   


'''_______ Python Boolean            

Python Booleans
Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

exit()
print(10 > 9)
print(10 == 9)
print(10 < 9)
When you run a condition in an if statement, Python returns True or False:

exit()
Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,

exit()
Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
exit()
Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

exit()
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

exit()
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

exit()
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
Functions can Return a Boolean
You can create functions that returns a Boolean Value:

exit()
Print the answer of a function:

def myFunction() :
  return True

print(myFunction())
You can execute code based on the Boolean answer of a function:

exit()
Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

exit()
Check if an object is an integer or not:

x = 200
print(isinstance(x, int))


comparision

    # print("alphabetical order of their component letters")
    # print("ord('a')",ord('a'))
    # print("ord('b')",ord('b'))
    # print("'a' > 'b'",'a' > 'b')

    # print("\"Bob\" > \"Dave\"","Bob" > "Dave")

    # exit()

    # x = (7 > 5)
    # print("int(7 > 5)",int(x))
    # print("int not(7 > 5)",int(not x))
    # exit()



boolean comparision
        # print("# # Booleans  and comparision")
        # exit()

        # print("2==3",2 == 3)           #equal.......... not assign
        # print("2 > 3 and 2<2",2 > 3 and 2<2)    #and 
        # print("2 > 3 and 2==2",2 > 3 and 2==2)   #lessthan ..... greaterthan ......comparative
        # print("2 == 3 or 2>=2",2 == 3 or 2>=2)   #greater or equal
        # print("0== 0 or 2 != 3",0== 0 or 2 != 3)  #the not equal to operator
        # exit()

        # print("0  == 0 or True)",0  == 0 or True)#2 <>3)   #the not equal to operator
        exit()
        # print(3.0==3) 
        # print(0.0==0) 
        # print("#and")
        # print("1 == 1 and 2 == 2",1 == 1 and 2 == 2)
        # print("1 == 1 and 2 == 3",1 == 1 and 2 == 3)
        # print("1 != 1 and 2 == 2",1 != 1 and 2 == 2)
        # print("2 < 1 and 3 > 6",2 < 1 and 3 > 6)
        # exit()
        # print("#or")
        # print( "1 == 1 or 2 == 2",1 == 1 or 2 == 2)
        # print( "1 == 1 or 2 == 3 ",1 == 1 or 2 == 3 )
        # print( "1 != 1 or 2 == 2 ",1 != 1 or 2 == 2 )
        # print( "2 < 1  or 3 > 6 ",2 < 1  or 3 > 6 )
        # exit()
        # print(" Boolean Not")

        # print("not 1 == 1",not 1 == 1)

        # exit()
        # print(" Boolean Operator preccedance      NOT > XOR > AND > OR    derived from C")
        # print(not True and True)
        # print("2>3 and 4<2 or 3>3 and 2>3 or not(3>3)",2>3 and 4<2 or 3>3 and 2>3 or not(3>3))
        # exit()



Operator
    # a=8
    # b=6
    # c=a%b

    # # print(c)

    # d=int(a/c)




# # logical operator
# print('p' == 'p',[]is[])
# print('p' == 'p',[]is[])
# # print([]is[])



boolean
    # print(1 or 2)
    # print(1 or 0 and 2)
    # print(0 and 2)




# comparision

    # print("alphabetical order of their component letters")
    # print("ord('a')",ord('a'))
    # print("ord('b')",ord('b'))
    # print("'a' > 'b'",'a' > 'b')

    # print("\"Bob\" > \"Dave\"","Bob" > "Dave")

    # exit()

    # x = (7 > 5)
    # print("int(7 > 5)",int(x))
    # print("int not(7 > 5)",int(not x))
    # exit()



# boolean comparision
        # print("# # Booleans  and comparision")
        # exit()

        # print("2==3",2 == 3)           #equal.......... not assign
        # print("2 > 3 and 2<2",2 > 3 and 2<2)    #and 
        # print("2 > 3 and 2==2",2 > 3 and 2==2)   #lessthan ..... greaterthan ......comparative
        # print("2 == 3 or 2>=2",2 == 3 or 2>=2)   #greater or equal
        # print("0== 0 or 2 != 3",0== 0 or 2 != 3)  #the not equal to operator
        # exit()

        # print("0  == 0 or True)",0  == 0 or True)#2 <>3)   #the not equal to operator
        exit()
        # print(3.0==3) 
        # print(0.0==0) 
        # print("#and")
        # print("1 == 1 and 2 == 2",1 == 1 and 2 == 2)
        # print("1 == 1 and 2 == 3",1 == 1 and 2 == 3)
        # print("1 != 1 and 2 == 2",1 != 1 and 2 == 2)
        # print("2 < 1 and 3 > 6",2 < 1 and 3 > 6)
        # exit()
        # print("#or")
        # print( "1 == 1 or 2 == 2",1 == 1 or 2 == 2)
        # print( "1 == 1 or 2 == 3 ",1 == 1 or 2 == 3 )
        # print( "1 != 1 or 2 == 2 ",1 != 1 or 2 == 2 )
        # print( "2 < 1  or 3 > 6 ",2 < 1  or 3 > 6 )
        # exit()
        # print(" Boolean Not")

        # print("not 1 == 1",not 1 == 1)

        # exit()
        # print(" Boolean Operator preccedance      NOT > XOR > AND > OR    derived from C")
        # print(not True and True)
        # print("2>3 and 4<2 or 3>3 and 2>3 or not(3>3)",2>3 and 4<2 or 3>3 and 2>3 or not(3>3))
        # exit()


# # logical operator
    # print('p' == 'p',[]is[])
    # print('p' == 'p',[]is[])
    # # print([]is[])


# a='abcd'
# b='defg'
# c=''
# for i in a:
    # if i not in b:
        # c+=i
# print(c)

# a=0 or 1
# print(a)
# b=0 or 2
# print(b)
# exit()
# c=a or b
# print(a+b+c)

# print(1 or 2)
# print(1 or 0 and 2)
# print(0 and 2)

# x = 10
# y = 20
# expression = 'x + y'  # This is a string representing a Python expression

# result = eval(expression)  # Evaluating the expression using eval()

# print(result)  # Output will be 30 (since x + y = 10 + 20)
'''




'''_______ Python Opertors           

Python Operators
Python Operators
Operators are used to perform operations on variables and values.

In the exit() below, we use the + operator to add together two values:

exit()
print(10 + 5)
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	exit()	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	exit()	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	exit()	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	exit()	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	exit()	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y	
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	exit()	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# operators

#print("#In-Place Operator")
# x = 2
# print(x)

# x += 3
# print("x+=2",x)
# exit()

# x *= 3
# print("x*=2",x)
# exit()

# x **= 3
# print("x**=2",x)
# x %= 2
# print("x%=2",x)
# exit()

# exit()
# x = "spam"
# print("x = \"spam\"",x)
# exit()

# x += "eggs"
# print("x = \"egg\"",x)
# exit()

# x = "a"
# x *= 3
# print("x *= 3",x)


# exit()

# print(5**5%5+9*9)
# rint=5**5
# print(rint%5+9*9)

# if 2&0:
    # print("yes")
# else:
    # print("No")

# exit()


Oeprator
    # a=b=c=2
    # print(a==b==c)


    # exit()
    # #send to string operation
    # x="slooealrn"

    # y=x[:]
    # print(id(x)==id(y))

    # exit()


operator
    # a=0 or 1
    # print(a)
    # b=0 or 2
    # print(b)

    # c=a or b
    # print(a+b+c)



operator
    # print(7*(3+4-2)//5)
    # exit() 

    # print(abs(3+4j))
    # exit()
    


# a=b=c=2
# print(a==b==c)


# exit()
# #send to string operation


# a=8
# b=6
# c=a%b

# # print(c)

# d=int(a/c)


# print(len(str(8/2**2**2)))
# exit()
# x=0b0010
# print(x)
# exit()

# print((1j**2).real)
# exit()

# a=chr(65)
# b=ord("a") 
# print(a==chr(b))

# exit()


# print(7*(3+4-2)//5)
# exit() 

# print(abs(3+4j))
# exit()



# my_num=1234
# a=str(my_num//1000%10) #print(1%10)
# b=str(my_num//100%10) #print(12%10)
# c=str(my_num//10%10) #print(123%10)
# d=str(my_num//1%10) #print(1234%10)
# print(d+c+b+a)

'''




'''_______ Python Lists              

Python Lists
mylist = ["apple", "banana", "cherry"]
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

exit()
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:

exit()
Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
List Length
To determine how many items a list has, use the len() function:

exit()
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
List Items - Data Types
List items can be of any data type:

exit()
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
A list can contain different data types:

exit()
A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
type()
From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>
exit()
What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
The list() Constructor
It is also possible to use the list() constructor when creating a new list.

exit()
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


Python - Access List Items
Access Items
List items are indexed and you can access them by referring to the index number:

exit()
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
Note: The first item has index 0.

Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

exit()
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

exit()
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:

exit()
This exit() returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
By leaving out the end value, the range will go on to the end of the list:

exit()
This exit() returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:

exit()
This exit() returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

exit()
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  

Python - Change List Items
Change Item Value
To change the value of a specific item, refer to the index number:

exit()
Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

exit()
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

exit()
Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

exit()
Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

exit()
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
Note: As a result of the exit() above, the list will now contain 4 items.


Python - Add List Items
Append Items
To add an item to the end of the list, use the append() method:

exit()
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

exit()
Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
Note: As a result of the examples above, the lists will now contain 4 items.

Extend List
To append elements from another list to the current list, use the extend() method.

exit()
Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
The elements will be added to the end of the list.

Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

exit()
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


Python - Remove List Items
Remove Specified Item
The remove() method removes the specified item.

exit()
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
Remove Specified Index
The pop() method removes the specified index.

exit()
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
If you do not specify the index, the pop() method removes the last item.

exit()
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
The del keyword also removes the specified index:

exit()
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
The del keyword can also delete the list completely.

exit()
Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

exit()
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


Python - Loop Lists
Loop Through a List
You can loop through the list items by using a for loop:

exit()
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
Learn more about for loops in our Python For Loops Chapter.

Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

exit()
Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
The iterable created in the exit() above is [0, 1, 2].

Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

exit()
Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
Learn more about while loops in our Python While Loops Chapter.

Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

exit()
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
Learn more about list comprehension in the next chapter: List Comprehension.


Python - List Comprehension
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

exit():

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

exit()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
With list comprehension you can do all that with only one line of code:

exit()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

Condition
The condition is like a filter that only accepts the items that valuate to True.

exit()
Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:

exit()
With no if statement:

newlist = [x for x in fruits]
Iterable
The iterable can be any iterable object, like a list, tuple, set etc.

exit()
You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
Same exit(), but with a condition:

exit()
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

exit()
Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]
You can set the outcome to whatever you like:

exit()
Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

exit()
Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
The expression in the exit() above says:

"Return the item if it is not banana, if it is banana return orange".



Python - Sort Lists
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

exit()
Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
exit()
Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
Sort Descending
To sort descending, use the keyword argument reverse = True:

exit()
Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
exit()
Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

exit()
Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

exit()
Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

exit()
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

exit()
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

Python - Copy Lists
Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

exit()
Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
Another way to make a copy is to use the built-in method list().

exit()
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

exit()
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
Another way to join two lists is by appending all the items from list2 into list1, one by one:

exit()
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
Or you can use the extend() method, which purpose is to add elements from one list to another list:

exit()
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



Python - List Methods
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list



exit()
a=[8,0,4,6,1]
if (a is a[:]):#(a == a[:]):
    print(True)
else:
    print(False)
    
print(a[:])


list


    # x=[2,3,4]
    # y=x
    # print(y is x)
    # y=x[:]
    # print(y is x)

    # exit()



list
    # a=[[1,2],[2,3],[3,4]]
    # b=[x for x in a for x in x]
    # print(b)


    # arr=[1,(2,3),4]
    # n=len(arr)
    # if (2 in arr):
        # n=n+len(arr[1])
    # print(n)

list
    # a="Hello !"
    # newHello=[]
    # for hi in a:
       # for by in range(2):
        # newHello.append(hi)
        # print(newHello)
    # print(len(newHello))

    # exit()


list
    # x=[i for i in range(3,15,3)]
    # y=x
    # print(x)
    # y.append([i for i in range(2,14,3)])
    # print(y)
    # print(x)
    # print(len(x)/1)
    # exit()
    # x=[1,3,5]
    # print(x in x)
    # exit()
    # a=[1,2,4,5]
    # print(a[1:5])#=[1]
    # a[1:5]=[1]
    # print(a)
    # exit()
    # a=0
    # b=0
    # x=[a,b]
    # y=(1,2)
    # x=y
    # print(x,a,b)

    # exit()
    # lst=[].append(5)
    # print(lst)
    # exit()
    # a={1,3,5}
    # b={2,4,6}



# exit()
# x=[i for i in range(3,15,3)]
# y=x
# print(x)
# y.append([i for i in range(2,14,3)])
# print(y)
# print(x)
# print(len(x)/1)

# exit()
# x=[1,3,5]
# print(x in x)
# exit()
# a=[1,2,4,5]
# print(a[1:5])#=[1]
# a[1:5]=[1]
# print(a)
# exit()
# a=0
# b=0
# x=[a,b]
# y=(1,2)
# x=y
# print(x,a,b)

# exit()
# lst=[].append(5)
# print(lst)
# exit()


# x=[2,3,4]
# y=x
# print(y is x)
# y=x[:]
# print(y is x)

# exit()


# a=[[1,2],[2,3],[3,4]]
# b=[x for x in a for x in x]
# print(b)

# arr=[1,(2,3),4]
# n=len(arr)
# if (2 in arr):
    # n=n+len(arr[1])
# print(n)


# a="Hello !"
# newHello=[]
# for hi in a:
   # for by in range(2):
    # newHello.append(hi)
    # print(newHello)
# print(len(newHello))

# exit()


    # words = ["Hello", "world", "!"]
    # print(words[0])
    # print(words[1])
    # print(words[2])

    # ar=[2,1,3]#,"a",3]
    # ar.sort()
    # print(ar)

    # exit()
    # a=[1,2,3,4]
    # b=a.copy()
    # print(b)
    # b.append(a)
    # print(b)
    # a.append(b)
    # print(a)
    # print(len(a))
    # print(len(b))


    # m = [
        # [1, 2, 3],
        # [4, 5, 6]
        # ]
    # print(m)


    # # # iterate throguh a list and dump the list

    # x=[2,8]#,7,1,0,124,8897,55,3,67,99]
    # nums=0


# y=[x if x==1 else x*2 for x in ["1","2"]][0]

# print([x if x==1 else x*2 for x in ["1","2"]])


# a=[2,4,6,8]
# b=a
# print(b)


# b[0]=7
# a[3]=9

# print(a)

# b.append(5)


# print(a)

# exit()

# a,b=[0],[0]
# a,b=b,a





# L=list(range(10))

# print(L)
# print(L.pop())#remove the last
# print(L)
# print(max(L))


# word="bringback"
# print(word[::-2])


# iterate throguh a list and dump the list
# for nums in len(x):
    # nums+=1
    
    
    
    
# # iterate throguh a list and dump the list
# print(list(range(len(x))))

# games=['tennis','footballes','cricket']
# for item in games:
    # if 'ball' in item:
        # print(item)




# #diffrence b/n list and map>>???
# abc=list(range(5))
# sq=list(map(lambda x:x**2,range(5)))
# print(abc)
# print(sq)

# for i in range(len(x)):
    # print(x[i])
    # i+=i 

# # iterate throguh a list find cummmulative
# sum=0
# for num in x:
    # sum+=num
    
# print(sum)


# # to add all odd nubmer in list...

# b=[1,2,3,4,5]
# print(b[1:-2])
# print(b[1:-1])


# nums = [1,2,3,4]
# res=0

# for x in nums:
    # if x%2==nums:
        # continue
    # else:
        # print(x)    #res+=x #res = res+x
        # res+=x      #res = res+x
        
# print(res)



# i=list(range(1,4))
# # i=list(range(4))
# print(i)
# # s=list(map(lambda x:x**2,i)) 
# s=list(filter(lambda x:x**2,i))
# print(s)
# print(sum(s))

# my_list=["apples","tomatoes","banana","orange","melons"]
# my_list.sort(key=lambda x:x[-2])
# print(my_list[1])



#Python next() method
# list=[1,2,3,4]
# a=(i**2 for i in list)
# print(a)
# print(next(a),next(a))  #https://www.geeksforgeeks.org/python-next-method/



# fib=[0,1,1,2,3,5,8,13]
# # print(fib[::2])
# print(fib[2::2])




# # https://www.geeksforgeeks.org/python-range-function/       #Syntax of Python range() function

# # Syntax: range(start, stop, step)
# # In the given exit(), we are printing the number from 0 to 4.

# for i in range(5):
	# print(i, end=" ")
# exit()

## The remove method working 
# l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

# l.remove('Alice')
# print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']


# # In this exit(), we are printing the number from 0 to 5. We are using the range function in which we are passing the stopping of the loop... printing first 6  whole number
# for i in range(6):
	# print(i, end=" ")
# exit()


# for i in range(5, 20): # printing a naturar number from 5 to 20
	# print(i, end=" ")


# for i in range(0, 10, 2): # exit() of Python range (start, stop, step)
	# print(i, end=" ")
# exit()



# for i in range(0, 30, 4): #incremented by 4
	# print(i, end=" ")
# exit()


# for i in range(25, 2, -2): #incremented by -2
	# print(i, end=" ")
# exit()



# for i in range(3.3): #using a float number
	# print(i)

# # Concatenation of two range() functions using itertools chain() method

# from itertools import chain

# # Using chain method
# print("Concatenating the result")
# res = chain(range(5), range(10, 20, 2))

# for i in res:
	# print(i, end=" ")




# ele = range(10)[0]  # Accessing range() with an Index Value
# print("First element:", ele)

# ele = range(10)[-1]
# print("\nLast element:", ele)

# ele = range(10)[4]
# print("\nFifth element:", ele)

# range() function with List in Python

# fruits = ["apple", "banana", "cherry", "date"]

# for i in range(len(fruits)):
	# print(fruits[i])

# # Return Type in range() vs xrange()
# # initializing a with range()

# a = range(1, 10000)

# # initializing a with xrange()
# x = xrange(1, 10000)

# # testing the type of a
# print("The return type of range() is : ")
# print(type(a))

# # testing the type of x
# print("The return type of xrange() is : ")
# print(type(x))

# # Speed of xrange() and range() Function
# import sys

# # initializing a with range()
# a = range(1,10000)

# # initializing a with xrange()
# x = xrange(1,10000)

# # testing the size of a
# range() takes more memory
# print ("The size allotted using range() is : ")
# print (sys.getsizeof(a))

# # testing the size of x
# xrange() takes less memory
# print ("The size allotted using xrange() is : ")
# print (sys.getsizeof(x))


# # Operations Usage of xrange() and range() Function
# # initializing a with range()
# a = range(1,6)

# # initializing a with xrange()
# x = xrange(1,6)

# # testing usage of slice operation on range() prints without error
# print ("The list after slicing using range is : ")
# print (a[2:5])

# # testing usage of slice operation on xrange() raises error
# print ("The list after slicing using xrange is : ")
# print (x[2:5])

# # Python – Test if List contains elements in Range


# # Method #1 : 
    # # Using loop This is brute force method in which this task can be performed. In this, we just check using if condition if element falls in range, and break if we find even one occurrence out of range. 

# # Python3 code to demonstrate 
# # Test if List contains elements in Range
# # using loop

# # Initializing loop 
# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list 
# print("The original list is : " + str(test_list))

# # Initialization of range 
# i, j = 3, 10

# # Test if List contains elements in Range using loop
# res = True
# for ele in test_list:
	# if ele < i or ele >= j :
		# res = False
		# break

# # printing result 
# print ("Does list contain all elements in range : " + str(res))


# # Method #2 : 
    # # Using all() This is alternative and shorter way to perform this task. In this we use check operation as a parameter to all() and returns True when all elements in range. 


# # Python3 code to demonstrate 
# # Test if List contains elements in Range
# # using all()

# # Initializing loop 
# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list 
# print("The original list is : " + str(test_list))

# # Initialization of range 
# i, j = 3, 10

# # Test if List contains elements in Range
# # using all()
# res = all(ele >= i and ele < j for ele in test_list) 

# # printing result 
# print ("Does list contain all elements in range : " + str(res))


# # Method #3 : Using list comprehension and len()

# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using List Comprehension and len()
# # Initializing list


# test_list = [4, 5, 6, 7, 3, 9]

# # printing original list
# print("The original list is : " + str(test_list))

# # Initialization of range
# i, j = 3, 10

# # Test if List contains elements in Range
# # using List Comprehension and len()
# out_of_range = len([ele for ele in test_list if ele < i or ele >= j])==0

# # printing result
# print ("Does list contain all elements in range : " + str(out_of_range))


# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using any()

# # Initializing list and range boundaries
# test_list = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10

# # Checking if any element in the list is within the range
# res = any(i <= x < j for x in test_list)

# # Printing the result
# print("Does list contain any element in range: " + str(res))


# # Method 5: Using filter() function

# # Python3 code to demonstrate
# # Test if List contains elements in Range
# # using filter()

# # Initializing list and range boundaries
# test_list = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10

# # Function to check if x lies within the given range
# def in_range(x):
	# return i <= x < j

# # Filtering out the elements that lie within the range
# # filtered_list = list(filter(in_range, test_list))

# # Checking if the filtered list is not empty
# res = bool(filtered_list)

# # Printing the result
# print("Does list contain any element in range: " + str(res))


# Python – Test if elements of list are in Min/Max range from other list


# # Method #1 : Using loop + min() + max()
# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using loop + min() + max()

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# res = True
# for ele in range_list:

	# flag off list in case of any off range element
	# if ele max(test_list):
		# res = False
		# break

# # printing result
# print("Are all elements in min/max range? : " + str(res))



# # Method #2 : Using all() + min() + max()

# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using all() + min() + max()

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# # checking for all values in range using all()
# res = all(ele >= min(test_list) and ele <= max(test_list)
		# for ele in range_list)

# # printing result
# print("Are all elements in min/max range? : " + str(res))


# # Method #3: Using set intersection


# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using set intersection

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original lists
# print("The original list is : " + str(test_list))

# # initializing range_list
# range_list = [4, 7, 9, 6]

# # using set intersection to find common elements between test_list and range_list
# # common_elements = set(test_list).intersection(set(range_list))

# # checking if all common elements are within the range

# res = all(ele >= min(test_list) and ele <= max(test_list)
		# for ele in common_elements)

# # printing result
# print("Are all elements in min/max range? : " + str(res))

# # Method #4: Use list comprehension

# # Python3 code to demonstrate working of
# # Min/Max range test from other list
# # Using list comprehension

# # initializing list
# test_list = [5, 6, 3, 7, 8, 10, 9]

# # printing original list
# print("The original list is : " + str(test_list))

# # initializing range list
# range_list = [4, 7, 9, 6]

# # filtering range list to remove elements outside of min/max range
# # filtered_list = [x for x in range_list if min(test_list) <= x <= max(test_list)]

# # checking if filtered list is the same as range list
# res = filtered_list == range_list

# # printing result
# print("Are all elements in min/max range? : " + str(res))




# # Python | Generate random numbers within a given range and store in a list

# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 15):
	# y = random.randrange(9)
	# print(y)

# # Method 1: Generate random integers using random.randrange() method
# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 15):
	# y = random.randrange(9)
	# print(y)

# # Method 2: Generate random integers using random.uniform() method
# import random


# print("Random integers between 0 and 9: ")
# for i in range(4, 11):
	# y = random.uniform(4, 10)
	# print(y)


# # Method 3: Generate random integers using randbelow() method
# from secrets import randbelow

# for _ in range(3, 9):

	# print(randbelow(15))


# # Method 4: Generate random integers using the random.randint() method

# # Python code to generate
# # random numbers and
# # append them to a list










# def Rand(start, end, num):
	# res = []

	# for j in range(num):
		# res.append(random.randint(start, end))

	# return res


# Driver Code
# num = 10
# start = 20
# end = 40
# print(Rand(start, end, num))


# # Using random.sample() function:
# import random

# num = 10
# start = 20
# end = 40

# result = random.sample(range(start, end + 1), num)

# print(result)



# # Python | Contiguous Boolean Range


# # Method #1 : Using enumerate() + zip() + list comprehension By using combination of above three functions, this task can easily be accomplished. The enumerate function handles the role of iteration, zip function groups the like values and the logic part is handled by list comprehension. 
# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using enumerate() + zip() + list comprehension

# # initializing list 
# test_list = [True, True, False, False, True,
			# True, True, True, False, True]

# # printing the original list 
# print ("The original list is : " + str(test_list))

# # using enumerate() + zip() + list comprehension
# # for Contiguous Boolean Ranging
# # res = [x for x, (i , j) in enumerate(zip( [2]
		# # + test_list, test_list + [2])) if i != j]

# # printing result
# print ("The boolean range list is : " + str(res))



  # # Method #2 : Using sum() + accumulate() + groupby() The above three functions can also be clubbed together to achieve the particular task, as they use the iterators to achieve it. The sum function counts each value, groupby groups each one and all together are accumulated by the accumulate function. 

# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using sum() + accumulate() + groupby()
# # from itertools import accumulate, groupby

# # initializing list 
# test_list = [True, True, False, False, False,
			# True, True, True, False, False]

# # printing the original list 
# print ("The original list is : " + str(test_list))

# # using sum() + accumulate() + groupby()
# # for Contiguous Boolean Ranging
# # res = [0] + list(accumulate(sum(1 for i in j) 
			# # for i, j in groupby(test_list)))

# # printing result
# print ("The boolean range list is : " + str(res))


# # Method #3 : Using looping


# # Python3 code to demonstrate
# # Contiguous Boolean Ranging
# # using for loop and if statement

# # initializing list 
# test_list = [True, True, False, False, False,
			# True, True, True, False, False]

# # printing the original list 
# print("The original list is:", test_list)

# # using for loop and if statement
# # for Contiguous Boolean Ranging

# res = []
# for i, v in enumerate(test_list):
	# if i == 0 or v != test_list[i-1]:
		# res.append(i)
# res.append(len(test_list))
# # printing result
# print("The boolean range list is:", res)
# # This code is contributed by Edula Vinay Kumar Reddy
# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
# print(sqs[4:7])


# k=list(range(0,6,2)) #covnert to list range
# print(len(k))


# a=[1,2,3,4]
# b=a
# print(b)
# exit()

# import copy
# a = [[1],[2],[3]]
# b = copy.deepcopy(a) ## this will copy the list a to list b

# print(b)

# exit()
# a=[1,2,3,4]
# print(a[2:2])


# a='python'[::-1]
# print(a)
# a='python'[::-1].endswith('y')
# print(a)
# a='python'[::-1][::-1]
# print(a)
# a='python'[::-1][::-1].endswith('n')
# print(a)

# mylist=list(range(5))
# n=id(mylist)
# mylist[:]=[x for x in mylist if x%2]
# print(id(mylist)==n)



# a=[8,0,4,6,1]
# print(a == a[:])
# print(a is a[:])
# # print('a'is 'b')
# if(a is a[:]):
    # print(True)
# else:
    # print(False)
    



# num=5
# my_list=[0,1,5,4]

# print(my_list[:-1])
# print(my_list[:-2])
# exit()
# print(my_list if num > 7 else my_list[:-2])




# print(list(range(0,5)))
# print(list(range(5)))
# x="hello!"
# for i in range(0,len(x)-1):
    # print((x[i]))



# List=[]
# List.append(1)
# List.extend(2)
# print(List)


# exit()
# a=[1]
# a*=2
# print(a)
# a[0]=3
# print(sum(a))


# # list
# l1=[1,2,3,4] 
# l2=list(map(lambda x:x+2 if x>2 else x-2,l1))
# print(l2)

# k=[[1,2,3,4,5,6]]
# k.append(7)
# k.insert(1,8)
# print(k)
# print(len(k))

# exit()
# print(sum(list(range(0,4)))) #
# my_list=[i for i in range(8)]
# for i in my_list:
    # my_list.remove(i)
# print(sum(my_list))


# print(list(range(4,7,2)))
# exit()

# my_list=["car","plane","train","bike","rocket"]
# newlist=sorted(my_list)
# print(newlist)
# print(newlist[-1])
# newlist=sorted(my_list,key=lambda x:x[-2])
# print(newlist)

# exit()


# # list
# x='abcde'
# y=x[-1:]
# print(y)
# print(len(y))
# #list
# a=[1,2,3]
# b=[4,5]
# a.append(b)
# a.extend(b)

# print(a)

# #list 
# l=['a','b','c']
# print('d'.join(l))
# exit()


# exit()



# L=[[]]*3
# print(L)
# L[0]+=[[]]
# print(L)
# print(L[0]==L[1])
# print(L[0]is L[1])
# print(len(L[0])==bool(L[0]))


# nums={1,2,3,4,5,6}
# nums={0,1,2,3}&nums
# nums=filter(lambda x:x>1, nums)
# print(len(list(nums)))



# exit()

# #List
# a=[1,2,3,4,6,7,8]
# b=a[:4]
# b.append(5)

# print(b)

# exit()

# lar_num=0
# print(list(range(0,10,3)))
# exit()
# for i in range(0,10,3):
    # if lar_num>=6:
        # break
    # if i > lar_num:
        # lar_num=i%2
# print(lar_num)


exit()

# r=['red','orange','yellow','green','blue','indigor']
# p=[c[0] for c in r if len(c)<6]
# print('_'.join(p))


# arr=[0,1,2,3,4,5]
# ##r=[#,1,#,3,#,5]
# n=0
# for _ in arr:
    # print(_)  # refers from arr
    # # del arr[n] # method is only to delete okay
    # # print(arr[n])
    # n+=1
    # # print(n)
    # del arr[n]  # method is only to delete okay
    # print("loop")
    # # del arr[n] # method is only to delete okay

# a=[2,4,5]
# print(list(range(1,3)))

# for i in range(1,3):
    # print(i)
    # a[i]=a[i-1] #[1,1]..[2,2]
    # print(a[i],end='')
    # print(i)


# a=[2,1,2,4]
# a[1:].remove(2)
# print(sum(a))


# A=[1,2,3,4,5,6,7]
# G=iter(A)
# next(G)
# for num in G:
    # print(num)
    # next(G)
    # next(G)

# a=[1,2,3]
# b=a
# b.append(3)
# print(b[3]==a[-1])

# print({1,2,3}is{1,2,3})
# print({1,2,3}=={1,2,3})

# L=[[]]*3
# # print(L)
# print(L[0]==L[1])
# print(L[0] is L[1])
# print(len(L[0])==bool(L[0]))

# # arr=[2,1,"a",3]
# arr=["b","a"]
# arrL=[2,1,2,3]
# arrL.sort()
# arr.sort()
# print(arrL) #with letter and nubmer mixed up..it gifes error
# print(arr)



# my_list=[1,5,1,0,1,9,9,5]
# new_list=my_list[-1:-4:-1]#[-1::-1] #for start.. then undrestand
# print(new_list)

# print(list[::-1]) #one way of doing reversing
# print(list(reversed(list(range(5)))))
# print([i for i in list(range(5))])

# print(bool([])+1)


# s=list(reversed(list("hewer")))
# print(s)



# s=reversed("sdfd")
# print(s) # address of object s..


# print(''.join(list(reversed(list("sdfsd")))))


# x="abc"
# x=list(x)
# x.insert(1,"d")
# x=''.join(x)
# x=x[2:0:-1]
# print(x)



# a=[1,2,3]
# del(a[0])
# # print(del(a[0]))
# print(a)
# print(len(a[1:]))


# a=[1,2,3,5,8,13]
# print(a[2:2])
# exit()

# arr=[1,0,1,0]
# a=all(arr)
# s=sum(arr)
# if a or s:
    # print(a or s)
# else:
    # pass
# exit()


# squares=[0,1,4,8,16]
# quaras=squares
# squares[3]=0
# print(quaras)
# exit()

# nums=[11,22,33,44,55]
# res=list(filter(lambda x:not(x%2==0),nums))
# print(res)
# exit()



# a=["c","b","a"]
# a=a[::-1]
# print(a[1])
# exit()


# exit()

# arr=[0,1,1,0]
# for val in arr:
    # if val==0:
        # arr[val]=1
# print(arr)
# exit()


# num1=[1,3,4,5]
# num2=num1
# num2[0]=5
# print(num1[0])
# exit()

# exit()

# mylist=[1,2,3,4,5,6]
# print(mylist[2:5])
# mylist[2:5]=[]
# print(mylist)
# print(len(mylist))
# exit()


# print("sololearn"[:1])
# exit()



# a=[1,2,3]
# b=[4,5]
# a.append(b)
# a.extend(b)
# print(a)
# exit()


# a,b,*c=[x for x in range(0,12,3)]
# print(*c)
# exit()

# A=[8,0,-4,-6,1]
# for n in A:
    # if n<0:
        # A.append(abs(n))
    # x=n
# print(x)    
# exit()


# strList=['1','2','3','4','a']
# intList=[]
# for i in strList:
    # try:
        # intList.append(int(i))
    # except ValueError:
        # intList=['something not int']
    # finally:
        # inList=[]
# print(str(len(intList)))
# exit()



# arr=[4,3,2][1]
# print(arr)
# exit()



# a={0:1,1:2}
# _sum=0
# for b in a: _sum+=b-1    
# print(_sum + b) 
# exit()




# a={1:'a',2:'b'}
# b={2:'c',3:'d'}
# c={**a,**b}
# print(c[2])
# exit()


# exit()
# a=[i//2 for i in range(50) if i//2==20]
# print(len(a))
# exit()
# x=0
# for i in range(2,20,3): # [2, 5, 8, 11, 14, 17]
    # if i%2 ==0:
        # print(x)
        # x+=1
# print(x)

# exit()
# list1=[1,2]
# list2=list1
# list3=list1[:]  # python hates beign assigned to ..[] values for list
# a=list2 is list1
# b=list3 is list1
# # print(b)
# print(a,b)

# exit()
# arr=['b','c','d']   #converting list to dictionar bu assiend keys
# x={1:'a'}
# n=1
# for x[n] in arr:
    # print(x)
    # n+=1
# print(x)


# exit()
# n=0
# a=5
# b=3
# while a>0:
    # b+=1
    # a-=1
    # n+=1
# print(n) #5,4,3,2,1
# exit()
# def rec(x,y):
    # if(x==0):
        # return y;
    # if(x!=0):
        # return rec(x-1,y+1);    
# print(rec(3,4));

# exit()
# I=[]
# for i in range(17):
    # I.append(i*2) #print(I) find all even interger b/n 0-(17-1)*2
# m=[x|1 for x in I] #bitwise OR
# k=[x&1 for x in I] #bitwise AND
# p=[x^1 for x in I] #bitwise XOR
# n=[~x for x in I] #bitwise NOT
# print(sum(m))
# print(sum(k))
# print(sum(p))
# print(sum(n))

# exit()
# x=1
# while x<5:
    # x*=2
# print(x)

# exit()

# a=[]
# b=[a,a,a]
# print(b)
# for x in b:
    # n=len(x)
    # # print(n)
    # x.append(n)
    # print(x)
# print(b)
# print(b[0])
# exit()

exit()
A=[8,0,-4,-6,1]
for n in A:
    if n<0:
        # print(n)
        A.append(abs(n))
    print(n)
    x=n
print(x)



# a=(0)
# b=[0],[[0]],{0},[(0)]
# print(b)

# for i in b:
    # print(a in i)



# Lh=[1,2,3,4]
# print(Lh)
# Lh[0]=4
# print(Lh)

# spam={i:i%3+i for i in range(1,11)}
# print(spam)
# print(spam[2])
# print(spam[4])
# print(spam[spam[2]])


# print(type(1,))
# print(type((1,2)))



# paris=[(x,x**2)for x in range(1,5)]
# print(paris)
# print(paris[2][1])
# exit()

# # Quick examples of range to a list

# # Example 1: Range to list 
# # Using * unpacking Operator
# myrange = range(5, 10, 1)
# mylist = [*myrange]

# # Example 2: Range to List using list()
# mylist = list(range(10, 20))

# # Example 3: Using list() function
# mylist = range(10, 20, 1)

# # Example 4: Using list comprehension
# mylist = [x for x in range(10, 21)]

# # Example 5: Range to list 
# # Using for loop
# myrange = range(5, 15, 2)
# my_list = []
# for x in myrange:
    # my_list.append(x)

# # Example 6: Using extend() function
# myrange = range(5, 20, 3)
# my_list = []
# my_list.extend(myrange)

# # Example 7: Create an empty list
# my_list = []
# start, end = 5, 10  
# # Check if start value
# # smaller than end value
# if start < end:
    # my_list.extend(range(start, end))
    # my_list.append(end)  
    
    

# rang=range(20)
# mylist=[*rang]
# print(mylist)

# my="one","tw","thre"

# print(my[0])


# lst=[]
# for val in gen():
    # lst.append(int(a==val))
# print(sum(lst))


'''





'''_______ Python Tuples             

Python Tuples
mytuple = ("apple", "banana", "cherry")
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

exit()
Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:

exit()
Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
Tuple Length
To determine how many items a tuple has, use the len() function:

exit()
Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

exit()
One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
Tuple Items - Data Types
Tuple items can be of any data type:

exit()
String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
A tuple can contain different data types:

exit()
A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>
exit()
What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

exit()
Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


Python - Access Tuple Items
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

exit()
Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
Note: The first item has index 0.

Negative Indexing
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.

exit()
Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

exit()
Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:

exit()
This exit() returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
By leaving out the end value, the range will go on to the end of the list:

exit()
This exit() returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:

exit()
This exit() returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:

exit()
Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

Python - Update Tuples
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

exit()
Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
Add Items
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

exit()
Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

exit()
Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

exit()
Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
Or you can delete the tuple completely:

exit()
The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


Python - Unpack Tuples
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

exit()
Packing a tuple:

fruits = ("apple", "banana", "cherry")
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

exit()
Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

exit()
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

exit()
Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


Python - Loop Tuples
Loop Through a Tuple
You can loop through the tuple items by using a for loop.

exit()
Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
Learn more about for loops in our Python For Loops Chapter.

Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

exit()
Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.

exit()
Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
Learn more about while loops in our Python While Loops Chapter.


Python - Join Tuples
Join Two Tuples
To join two or more tuples you can use the + operator:

exit()
Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

exit()
Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


Python - Tuple Methods
Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found


# print(b,a)
# print(a)
# print(b)
# print(a is b)
# if (a is b):
    # print(True)
# else:
    # print(False)


# exit()


# t1=(1,2,3)
# t2=('a','b','c')
# print(tuple(zip(t1,t2)))#[1][0])
# print(tuple(zip(t1,t2))[1][0])



# tuple .. list
# ans=(1,2,3,4)[1]
# print(ans)

# becha tupples are immitible lets see them in more lively projects 
# # okay that is the onlyw ay to udnertstand them..


# gh=(1,2,3,4)
# print(gh)
# # gh(0)=12  # since tuples are immutabligty .. here 
# print(gh[0])
# gh=(12,2,3,4)
# print(gh)




# a=("la")
# b=("g")
# c=a+"o"+b
# print(c[::-1])
# exit()

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

Python Sets
myset = {"apple", "banana", "cherry"}
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

exit()
Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.

exit()
Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
Get the Length of a Set
To determine how many items a set has, use the len() function.

exit()
Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
Set Items - Data Types
Set items can be of any data type:

exit()
String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
A set can contain different data types:

exit()
A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>
exit()
What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))
The set() Constructor
It is also possible to use the set() constructor to make a set.

exit()
Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove items and add new items.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


Python - Access Set Items
Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

exit()
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
exit()
Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
Change Items
Once a set is created, you cannot change its items, but you can add new items.

Python - Add Set Items
Add Items
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.

exit()
Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
Add Sets
To add items from another set into the current set, use the update() method.

exit()
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

exit()
Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


Python - Remove Set Items
Remove Item
To remove an item in a set, use the remove(), or the discard() method.

exit()
Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
Note: If the item to remove does not exist, remove() will raise an error.

exit()
Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

exit()
Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

exit()
The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
exit()
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


Python - Loop Sets
Loop Items
You can loop through the set items by using a for loop:

exit()
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  


Python - Join Sets
Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

exit()
The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
exit()
The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
Note: Both union() and update() will exclude any duplicate items.

Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.

exit()
Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
The intersection() method will return a new set, that only contains the items that are present in both sets.

exit()
Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

exit()
Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

exit()
Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


Python - Set Methods
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others



# nums=set([1,1,2,3,3,4])
# print(len(nums))



# set={1,3,5,6,8,8,3,2}
# print(len(set))   # repetation is not allowed.. 
# print(len(set)+int("3"))



# exit()
# a=[1,5,13,4,19,14]
# b=[5,12,48,6,14,1]
# c=len(set(a)&set(b))
# print(c)

# exit()

'''



'''_______ Python Dictionary         


Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

exit()
Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

exit()
Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

exit()
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
Dictionary Length
To determine how many items a dictionary has, use the len() function:

exit()
Print the number of items in the dictionary:

print(len(thisdict))
Dictionary Items - Data Types
The values in dictionary items can be of any data type:

exit()
String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
exit()
Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


Python - Access Dictionary Items
Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

exit()
Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
There is also a method called get() that will give you the same result:

exit()
Get the value of the "model" key:

x = thisdict.get("model")
Get Keys
The keys() method will return a list of all the keys in the dictionary.

exit()
Get a list of the keys:

x = thisdict.keys()
The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

exit()
Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
Get Values
The values() method will return a list of all the values in the dictionary.

exit()
Get a list of the values:

x = thisdict.values()
The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

exit()
Make a change in the original dictionary, and see that the values list gets updated as well:

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
Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
Get Items
The items() method will return each item in a dictionary, as tuples in a list.

exit()
Get a list of the key:value pairs

x = thisdict.items()
The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

exit()
Make a change in the original dictionary, and see that the items list gets updated as well:

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
Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

exit()
Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


Python - Change Dictionary Items
Change Values
You can change the value of a specific item by referring to its key name:

exit()
Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

exit()
Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


Python - Add Dictionary Items
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

exit()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.

exit()
Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


Python - Remove Dictionary Items
Removing Items
There are several methods to remove items from a dictionary:

exit()
The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
exit()
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
exit()
The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
exit()
The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
exit()
The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


Python - Loop Dictionaries
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

exit()
Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)
exit()
Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
exit()
You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
exit()
You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)
exit()
Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)


Python - Copy Dictionaries
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

exit()
Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
Another way to make a copy is to use the built-in function dict().

exit()
Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


Python - Nested Dictionaries
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

exit()
Create a dictionary that contain three dictionaries:

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
Or, if you want to add three dictionaries into a new dictionary:

exit()
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

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


Python Dictionary Methods
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary




dictonary
    # person={"Name":"Sarah","Age":"18"}
    # person["Name"]="Sia"
    # person["Age"]="18+"
    # if "18+" not in person:
        # print("a")
    # else:
        # print("b")


    # exit()





# a={1,3,5}
# b={2,4,6}
# for i in range(7):
    # if i not in a and i not in b:
        # print(False)
        # break
    # else:
        # print(True)

# exit()


# person={"Name":"Sarah","Age":"18"}
# person["Name"]="Sia"
# person["Age"]="18+"
# if "18+" not in person:
    # print("a")
# else:
    # print("b")

# exit()


# # print(type({})==type({1})) # why is this?
# print(type([])==type([1]))  #??
# print(type(())==type((1,2)))    #??

# exit()



# # to convert list to dictoinary..
# contacts = [
    # ('James', 42),
    # ('Amy', 24),
    # ('John', 31),
    # ('Amanda', 63),
    # ('Bob', 18)
# ]

# t1=(1,2,3)
# t2=('a','b','c')
# print(tuple(zip(t1,t2))[1][0])



# contacts=dict(contacts)    #let it be taught/ treated...as dictonary.. ignoring .get(amanda)
# name=input()
# if name in contacts:
    # print(name, 'is', contacts[name])
# else:
    # print('not found')

# my_dict={"bill":"Gates","steve":"jobs"}
# L=[]
# # print(my_dict.items()) # .items().. dictionary.. 
# # my_dict.append("rich_gy") # . you can' t apend in dictionary

# for i,j in my_dict.items():
    # L.append(i)
    # print(L)
    # L.append(j)
    # print(L)
# # print(len(L))




# # method -1 append to list ...coloraly to deicitonary
# my_dict = {'key1': 'value1', 'key2': 'value2'}
# # Adding a new key-value pair
# my_dict['key3'] = 'value3'
# print(my_dict)

# # method -2 append to list ...coloraly to deicitonary
# my_dict = {'key1': 'value1', 'key2': 'value2'}
# # Adding/Updating multiple key-value pairs
# my_dict.update({'key3': 'value3', 'key4': 'value4'})

# print(my_dict)

# # method -3 append to list ...coloraly to deicitonary
# my_dict = {'key1': 'value1', 'key2': 'value2'}
# # Adding/Updating multiple key-value pairs
# my_dict.update({'key3': 'value3', 'key4': 'value4'})
# print(my_dict)




# a={1:[1,2,3]}
# b=a.copy()
# a[1].append(4)
# print(a)
# print(a==b)




# exit()
# dic={1:'X',3:'Y',2:'z'}
# for item in dic:
    # print(dic[item])
    # # print(item)

# exit()


# my_dict={"Bill":"Gates","Steve":"Jobs"}
# L=[]
# for i,j in my_dict.items():
    # L.append(i)
    # L.append(j)
# print(len(L))
# print(L)

#exit()
'''



'''_______ Python If..Else           

Python If ... Else
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

exit()
If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
In this exit() we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

exit()
If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

exit()
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
In this exit() a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

Else
The else keyword catches anything which isn't caught by the preceding conditions.

exit()
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
In this exit() a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

You can also have an else without the elif:

exit()
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

exit()
One line if statement:

if a > b: print("a is greater than b")
Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

exit()
One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
This technique is known as Ternary Operators, or Conditional Expressions.

You can also have multiple else statements on the same line:

exit()
One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
And
The and keyword is a logical operator, and is used to combine conditional statements:

exit()
Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
Or
The or keyword is a logical operator, and is used to combine conditional statements:

exit()
Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
Nested If
You can have if statements inside if statements, this is called nested if statements.

exit()
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

exit()
a = 33
b = 200

if b > a:
  pass


exit()

D=3
d=2 if D>0 else 7
print(D)# d=2 if D>0 else 7

exit()
# if statments

    # whq=12      #wht/(ht**2)
    # whq=wht/(ht**2)

    # if whq < 18.5:
        # print("under wight")     #..// find this caracter.. it is not compatable to sololearns.. 
    # elif whq > 18.5 and whq<25 :
        # print("Normal")
    # elif whq > 25 and whq<30:
        # print("over weight")
    # elif whq>30:
        # print("obesity")


# exit()


# print("if #condition:")
# print("   #statements    ")

# x = 42
# if x > 5:
    # print("x is greater than 5")


# exit()

# print(" else statment")
# exit()

# x = 4
# if x == 5:
    # print("Yes")
# else:
    # print("No")



# exit()   

# if d==25//b:
    # print(str(d)+str(c))
    
# else:
    # print("dc")

# print("# Boolean Logic")
# exit()   

# print("if #condition:")
# print("   #statements    ")

# x = 42
# if x > 5:
    # print("x is greater than 5")


# exit()

# print(" else statment")
# exit()

# x = 4
# if x == 5:
    # print("Yes")
# else:
    # print("No")



# exit()   

# if d==25//b:
    # print(str(d)+str(c))
    
# else:
    # print("dc")
'''



'''_______ Python While Loops        

Python While Loops
Python Loops
Python has two primitive loop commands:

while loops
for loops
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

exit()
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
Note: remember to increment i, or else the loop will continue forever.

The while loop requires relevant variables to be ready, in this exit() we need to define an indexing variable, i, which we set to 1.

The break Statement
With the break statement we can stop the loop even if the while condition is true:

exit()
Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

exit()
Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

exit()
Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  
 # print("# while loops")

    # loop
    # count=0
    # while(count<5):
        # print(count)
        # if(count>1):
            # count+=1
            # break
        # else:
            # count+=1

    # x=1
    # while (x<=5):
        # x+=x #x=x+x
       
    exit()

    # i = 1
    # while i <=5:
       # print(i)
       # i = i + 1

    # exit()

    # print("cummulative finder")
    # sum = 0
    # x = 10
    # while x > 0:
      # sum += x
      # x -= 1

    # print(sum)

    # exit()

  

while loops
    # exit()
    # x = 1
    # while x < 10:
      # if x%2 == 0:
        # print(str(x) + " is even")
      # else:
        # print(str(x) + " is odd")

      # x += 1

    # exit()

    # print(" # break continue")
    # exit()

    # print("break statment")
    # i = 0
    # while True:
      # print(i)
      # i = i + 1
      
      # if i >= 5:
        # print("Breaking")
        # break

    # print("Finished")
    # exit()
    # print("continue statment")

    # i = 0
    # while i<5:
      # i += 1
      # if i==3:
        # print("Skipping 3")
        # continue
      # print(i)

    # exit()



while loops
    # print(" Now this could be considered perfect:  # ticket issue ")
    # print(" While loop exit problem.... help .. for calculator .. a sorth.. tinkitner")

    # i = 1
    # ticket_cost = 100 
    # total = 0 


    # print("input 5  numbers")
    # while i<=5: 
        # age = int(input()) 
        # if age < 3: 
            # i += 1
            # continue 
        # # break 
        # else: 
            # total += ticket_cost 
            # #print("$" + str(total)) 
            # i += 1
    # print(total) 





while loops
    # i=1
    # while i<=10:
        # print(i+1)
        # i*=2

while loops
    # i=1
    # while i<=10:
        # if i==4:
            # break
        # i+=i
    # print(i)

    # exit()


while loops
    # i=1
    # while i<=10:
        # print(''.join(map(str,list(range(i+1)))))
        # i*=2

    # exit()


# count=0
# while(count<5):
    # print(count)
    # if(count>1):
        # count+=1
        # break
    # else:
        # count+=1
        


# x=1
# while (x<=5):
    # x+=x #x=x+x
    
# print(x)

# i = 1
# while i <=5:
   # print(i)
   # i = i + 1

# print("Finished!")

# exit()

# print("cummulative finder")
# sum = 0
# x = 10
# while x > 0:
  # sum += x
  # x -= 1

# print(sum)


# exit()


# x = 1
# while x < 10:
  # if x%2 == 0:
    # print(str(x) + " is even")
  # else:
    # print(str(x) + " is odd")

  # x += 1

  # exit()

# print(" # break continue")
# exit()

# print("break statment")
# i = 0
# while True:
  # print(i)
  # i = i + 1
  
  # if i >= 5:
    # print("Breaking")
    # break

# print("Finished")
# exit()
# print("continue statment")

# i = 0
# while i<5:
  # i += 1
  # if i==3:
    # print("Skipping 3")
    # continue
  # print(i)

# exit()


# i = 1
# ticket_cost = 100 
# total = 0 


# print("input 5  numbers")
# while i<=5: 
    # age = int(input()) 
    # if age < 3: 
        # i += 1
        # continue 
    # # break 
    # else: 
        # total += ticket_cost 
        # #print("$" + str(total)) 
        # i += 1
# print(total) 




# i=1
# while i<=10:
    # print(i+1)
    # i*=2


# i=1
# while i<=10:
    # print(''.join(map(str,list(range(i+1)))))
    # i*=2

# exit()

# i=1
# while i<=10:
    # if i==4:
        # break
    # i+=i
# print(i)

# exit()



# i=1
# while i<=5:
    # print(i)
    # i+=1


'''




'''_______ Python For Loops          

Python For Loops
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

exit()
Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
The for loop does not require an indexing variable to set beforehand.

Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:

exit()
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
The break Statement
With the break statement we can stop the loop before it has looped through all the items:

exit()
Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
exit()
Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:

exit()
Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

exit()
Using the range() function:

for x in range(6):
  print(x)
Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

exit()
Using the start parameter:

for x in range(2, 6):
  print(x)
The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

exit()
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

exit()
Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
Note: The else block will NOT be executed if the loop is stopped by a break statement.

exit()
Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

exit()
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

exit()
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


for loops
    # for i in range(5):
        # i=i+i
        
    # print(i)

    # # other possilble way
    # exit()
    # i=0
    # for x in range(8):
        # if x%2==0:
            # # print(x)
            # i+=x
         # # i+=1   

    # print(i)

    # num = int(input())
    # # def printValues():
    # l = list()
    # for i in range(0,21):
        # l.append(i**2)

    # for i in l[:num]:
        # print(i)

    # # print(l[-num:])


    # exit()
    # # import itertools as it
    # # for i in it.count(1):
        # # if(100-i==0):
            # # break
        # # print(i)



for loops
    # for i in range(10):
        # # print(i)
        # if i%2==0:
            # continue
            # print(i)
        # else:
            # pass
            # print(i)

    # exit()




for loops
    # a='abcd'
    # b='defg'
    # c=''
    # for i in a:
        # if i not in b:
            # c+=i
    # print(c)



for loops

    # for i in range(2):
        # print(i)
    # for i in range(4,6):
        # print(i)


    # exit()



for loops
    # for i in range(7):
        # if i not in a and i not in b:
            # print(False)
            # break
        # else:
            # print(True)

    # exit()

for loops
# x="hello!"
# for i in range(0,len(x)-1):
    # print(x[i])

# exit()


# for i in range(5):
    # i=i+i
    
# print(i)

# # other possilble way
# exit()
# i=0
# for x in range(8):
    # if x%2==0:
        # # print(x)
        # i+=x
     # # i+=1   

# print(i)

# num = int(input())
# # def printValues():
# l = list()
# for i in range(0,21):
    # l.append(i**2)

# for i in l[:num]:
    # print(i)

# # print(l[-num:])



# exit()
# # import itertools as it
# # for i in it.count(1):
    # # if(100-i==0):
        # # break
    # # print(i)


# for i in range(10):
# # print(i)
# if i%2==0:
    # continue
    # print(i)
# else:
    # pass
    # print(i)



# exit()

# for i in range(2):
    # print(i)
# for i in range(4,6):
    # print(i)

# exit()



# x="hello!"
# for i in range(0,len(x)-1):
    # print(x[i])

# exit()
# for i in range (10):
    # if i>10:
        # print("nope")
    # else:
        # print("done" + str(i))
'''



'''_______ Python Functions          

Python Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

exit()
def my_function():
  print("Hello from a function")
Calling a Function
To call a function, use the function name followed by parenthesis:

exit()
def my_function():
  print("Hello from a function")

my_function()
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following exit() has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

exit()
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
Arguments are often shortened to args in Python documentations.

Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

exit()
This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
If you try to call the function with 1 or 3 arguments, you will get an error:
exit()
This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

exit()
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
Arbitrary Arguments are often shortened to *args in Python documentations.

Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

exit()
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

exit()
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

Default Parameter Value
The following exit() shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

exit()
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

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
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

exit()
def myfunction():
  pass
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this exit(), tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

exit()
Recursion exit()

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
# def calc(x):
    # #your code goes here
    # return (x*4,x**2)

# side = int(input())
# p, a = calc(side)

# print("Perimeter: " + str(p))
# print("Area: " + str(a))



# def func(n):
    # y='+'.join(str(x)for x in range(n))
# # print('+'.join(str(x)for x in range(7)))
    # return (eval(y))
# print(func(7))



# def func1():
    # pass
# def func2(n):
    # if n%2==0:
        # return None
# print(func1())
# print(func2(3))#6 #3


# def sum(a,b):   
    # if a==0 or b==0:
        # return 0    #exit
    # return 1+sum(a-1,b-1) #3,1..1>>2,0..0
    # # 1+1+1...
# print(sum(23,2))



# #from challenges..Function..??
# a=()
# def func(n):
    # k=()
    # k=k+n
    # return k
    # return k
# for i in range(0,5,2):
    # a+=func((i,i+1))
# print(len(a))


# def count(n=0):
    # while True:
        # yield(yield n)
        # n+=1
# a=count()
# next(a)
# print(a.send(5),end="")
# print(a.send('a'))

# def gen():
    # global a
    # for num in [2,4,8]:
        # a+=1
        # yield (num*0.5)
# a=0.0

# # print(gen())


# lst=[]
# for val in gen():
    # lst.append(int(a==val))
# print(sum(lst))



# def fun(n):
    # if(n>100):
        # return n-5
    # return fun(fun(n+11))

# print(fun(2))
# # print(fun(105))



# Use Pop In Python to Remove an Item and Return It

# a=list(range(0,100))
# def function(x):
    # a.pop(x-1):
    # return(a)
# for i in range(0,100):
    # n=101-i
    # function(n)
# print(len(a))



# cars = ['Mercedes Benz', 'BMW', 'Jeep', 'Mahindra', 'Maserati']

# print(cars)

# # Using pop() and storing the return value

# ret_val = cars.pop(2)

# print('The return value is:', ret_val)

# # Updated List

# print('The updated list is:', cars)



# def f(x,a=[]):
    # for i in range(x):
        # a.append(i*i)
    # print(a)

# f(2)





# # def testFunc(x,y=[]):
    # # y.append(x)
    # # return y
# # a= testFunc(1)
# # b= testFunc(2,[])
# # c= testFunc(3)
# # print(c)


# a=([{}])
# # print(a[0])
# # print(len({}))
# # print(len(a))

# def fun(arr):
    # if len(arr)>0:
        # return 1 +fun(arr[0])
    # return  1
    
# print(fun(a))


# def swap(x,y):
    # x=x+y;  #14
    # y=x-y;  #14-9   5
    # x=x-y;  #14-5   9
    # return(x,y);
    
# print(swap(5,9))




# def f(s1,s2,s3):
    # return (int(s1)+int(s2))*str(s3)
    
# print(f("1","3",3))


# # def printValues():
	# # l = list()
	# # for i in range(1,21):
		# # l.append(i**2)
	# # print(l[:5])
	# # print(l[-5:])

# # printValues()

 
# # functions
# def evens(max):
    # v=0
    # while v<=max:
        # # return v
        # yield v
        # v+=2
# evens(2)



# def my_code():
    # return 0
    # print(4)
    
# print(my_code())

# y=[]
# def loop(x):
    # for i in x:
        # try:
            # y.append(int(i))
        # except:
            # pass
        # return y 
# print(loop([1.0,"1.0",y,abs(5j+1)]))


# def fs(ls,fil):
    # f=lambda x:not any(p in x for p in fil)
    # return list(filter(f,lst))
# f=['$','%']
# lst=['$dollar','@at','%modulu']
# print(fs(lst,f))

# # a=([{}])
# # a=([])
# # print(len(a))
# # # print(a[0])
# # exit()
# # def fun (arr):
    # # if len(arr)>0:
        # # return 1+fun(arr[0])
    # # return 1
# # print(fun(a))


# # def fun():
    # # for x in range(10,0,-1):
        # # yield(x)
# # x=fun()

# # for a in range(6):
    # # next(x)

# # print(next(x))

# # def func_a(a,b,c):
    # # a+=b
    # # b=a*c
    # # print(b)
# # a=10
# # b=15
# # c=5.0
# # func_a(a,b,c) #






# # def f(r):
    # # j=range(r)
    # # e=eval("*".join([str(i+1)for i in j]))
    # # return e

# # print(f(5))


# # def search(a,b,*c):
    # # length=len(c)
    # # if length is not None:
        # # print("The variable C holds {} items".format(length))
# # search(1,2,3,4,5,6,7,8,9,10)


# # k=0
# # var="abcb"
# # for i in var:
    # # print(i,k)
    # # k+=1
    
# # def counts(var):
    # # for i in var:
        # # if var.count(i)>1:
            # # return i
            # # break

# # print(counts(var))


# exit()

# # exit()
# # def f(q,mylist=[]):
    # # mylist=mylist+q
    # # return mylist
# # a=[1]
# # print(f(a))
# # a=[2]
# # print(f(a))
# # exit()


# # def a(x):
    # # return(x*7//5*10%4)
# # nums=[2,4,8,3,1]
# # print(a(nums[3]))
# # exit()



# # exit()
# # def cm():
    # # return [lambda x:i*x for i in range(3)]

# # for m in cm():
    # # print(m(2),end='')

# # exit()
# # def f(x):
    # # return g(x)+3%2
# # def g(x):
    # # return x**2+2
# # print(f(g(1)))   



# # exit()

# # def fun(a):
    # # x=range(a)
    # # y=eval('*'.join([str(i+1) for i in x])) #1*,2*3*4*5*6
    # # return y
# # x=range(6)
# # y=[str(i+1) for i in x]
# # y='*'.join([str(i+1) for i in x])
# # print(y)
# # print(fun(6))

# # exit()


# # def sub(x,y):
    # # return(x-y)
# # def mult(x,y):
    # # return x*y
# # def pr(f1,f2,d):
    # # print(f1(f2(d+1,d),d))
# # pr(mult,sub,4)

# # exit()
# # def f(x):
    # # return(2*x+1)
# # def g(x):
    # # return (x-1)
# # print(g(f(2))-f(g(2)))

# # exit()
# # def f(q,mylist=[]):
    # # mylist=mylist+q
    # # return mylist
# # a=[1]
# # print(f(a))
# # a=[2]
# # print(f(a))

# exit()

# # def guess(list1):
    # # list2=list1
    # # list2.append(4)
    # # list1=[5,6,7]
# # list1=[1,2,3]
# # guess(list1)
# # print(sum(list1))
# # exit()


# def dec(x):
    # def f(a,b):
        # print("Solo",end="")
        # if b==0:
            # print("Learn",end="")
            # return
        # return dec(a,b)
    # return f
# @dec
# def dec(a,b):
    # return a/b
# dec(3,0)
'''




'''_______ Python Lambda             

Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:

exit()
Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))
Lambda functions can take any number of arguments:

exit()
Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))
exit()
Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
Use that function definition to make a function that always doubles the number you send in:

exit()
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
Or, use the same function definition to make a function that always triples the number you send in:

exit()
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
Or, use the same function definition to make both functions, in the same program:

exit()
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



# func=lambda x:x%2==0
# abc=list(filter(func,range(8)))
# print(sum(abc))



# func=lambda x:x%2==0
# abc=list(filter(func,range(8)))
# print(sum(abc))
# exit()



'''



'''_______ Python Arrays             

Python Arrays
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

Arrays are used to store multiple values in one single variable:

exit()
Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
What is an Array?
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for exit()), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.

Access the Elements of an Array
You refer to an array element by referring to the index number.

exit()
Get the value of the first array item:

x = cars[0]
exit()
Modify the value of the first array item:

cars[0] = "Toyota"
The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

exit()
Return the number of elements in the cars array:

x = len(cars)
Note: The length of an array is always one more than the highest array index.

Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

exit()
Print each item in the cars array:

for x in cars:
  print(x)
Adding Array Elements
You can use the append() method to add an element to an array.

exit()
Add one more element to the cars array:

cars.append("Honda")
Removing Array Elements
You can use the pop() method to remove an element from the array.

exit()
Delete the second element of the cars array:

cars.pop(1)
You can also use the remove() method to remove an element from the array.

exit()
Delete the element that has the value "Volvo":

cars.remove("Volvo")
Note: The list's remove() method only removes the first occurrence of the specified value.

Array Methods
Python has a set of built-in methods that you can use on lists/arrays.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
'''



'''_______ Python Classes/Objects    

Python Classes and Objects
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:

exit()
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
Create Object
Now we can use the class named MyClass to create objects:

exit()
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

exit()
Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

exit()
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

exit()
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
Modify Object Properties
You can modify properties on objects like this:

exit()
Set the age of p1 to 40:

p1.age = 40
Delete Object Properties
You can delete properties on objects by using the del keyword:

exit()
Delete the age property from the p1 object:

del p1.age
Delete Objects
You can delete objects by using the del keyword:

exit()
Delete the p1 object:

del p1
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

exit()
class Person:
  pass

# print("___class")

# class myclass():
    # n=0
    # def __init__(self):
        # myclass.n+=1
    # def __del__(self):
        # myclass.n-=1
# a=myclass()
# print(a.n)
# b=myclass()
# print(b.n)
# a=myclass()
# print(b.n)


# class spam:
    # __egg=7
    # def print_egg(self):
        # print(self.__egg)
# s=spam()
# print(s.__egg)



# #os.close(f) # close the descritor f

# class myclass:
    # def __iter__(self):
        # self.x=1
        # return obj
    # def __next__(self):
        # y=self.x
        # self.x+=1
        # return y
# obj=myclass()
# it=iter(obj)
# print(next(it))
# print(next(it))
    



# #send to class object orinted prorgramming.. 
# class Class:
    # n=3
    # def __init__(self,n):
        # self.n=n%2
# a=Class(5)

# print(a.n)
# class tower():
    # def __init__(self,x=100):
        # self.hp=x
# A=tower()
# B=tower(90)
# C=tower()
# print(A.hp+B.hp-C.hp)





# def tripler(org_func):
    # def my_function(orig_val):
        # return(org_func(orig_val)*3)
    # return(my_function)

# @tripler
# def doubler(user_input):
    # return(user_input*2)
# print(doubler(5))


# class A:
    # def __init___(self,value):
        # self.a=value
# class B(A):
    # def __init__(self,value=2):
        # super().__init__()
# ab=B(8)
# print(ab)
# # print(ab.a)


# class vec:
    # def __init__(self,x,y):
        # self.x=x
        # self.y=y
    # def __add__(self,other):
        # return vec(self.x+ other.x,self.y+other.y)
# v1=vec(3,4)
# v2=vec(1,2)
# r=v1+v2
# print(r.x)
# print(r.y)
# print(r.x*r.y)

exit()


# class foo:
    # def bar(self):
        # pass

# print(foo.bar.__name__)

# exit()

# from functools import reduce
# mul = lambda n1, n2: n1 * n2
# class cls:
    # def __enter__(self):
        # # Return a function that calculates factorial
        # def f(n):
            # return reduce(mul, range(2, n + 1), 1)
        # return f  # Return the factorial function

    # def __exit__(self, *args):
        # pass

# with cls() as a:
    # print(a(5))  # Call the returned function a(5) to calculate factorial

# exit()

# class A:
    # @staticmethod
    # def sample(self):
        # print("static method")
    # @classmethod
    # def sample(self):
        # print("class method")
# A.sample()
# exit()


# class J(str):
    # def __init__(self, j):
        # self.j=j
    # def __add__(self,other):
        # self.j+other.j
# x=J(5)
# y=J(7)
# print(x+y)
# exit()

# exit()
# add=lambda x,y: x+y
# class Add:
    # def __init__(self,n):
        # self.n=n
    # def __add__(self,other):
        # if type('')in (type(self.n),type(other)):
            # return add(str(self.n),str(other))
        # return add(self.n,other)

# print(Add(7)+'4')

# exit()


# class Go:
    # def __call__(self,x):
        # return x
# print(Go()(5))
# exit()
# try:
    # print(Go()(5))
# except:
    # print(0)
# exit()





# class A:
    # def __init__(self):
        # self.a=0
    # def change(self,n):
        # a=n
# obj=A()
# obj.change(2)
# print(obj.a)
'''



'''_______ Python Inheritance        


Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

exit()
Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

exit()
Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass
Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

Now the Student class has the same properties and methods as the Person class.

exit()
Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

exit()
Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

exit()
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

exit()
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

Add Properties
exit()
Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
In the exit() below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

exit()
Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
Add Methods
exit()
Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.


'''


'''_______ Python Itertors           

Python Iterators
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

exit()
Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
Even strings are iterable objects, and can return an iterator:

exit()
Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
Looping Through an Iterator
We can also use a for loop to iterate through an iterable object:

exit()
Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
exit()
Iterate the characters of a string:

mystr = "banana"

for x in mystr:
  print(x)
The for loop actually creates an iterator object and executes the next() method for each loop.

Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

exit()
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

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
StopIteration
The exit() above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

exit()
Stop after 20 iterations:

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
'''


'''_______ Python Scope              

Python Scope
A variable is only available from inside the region it is created. This is called scope.

Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

exit()
A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()
Function Inside Function
As explained in the exit() above, the variable x is not available outside the function, but it is available for any function inside the function:

exit()
The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

exit()
A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

exit()
The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

exit()
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)
Also, use the global keyword if you want to make a change to a global variable inside a function.

exit()
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
'''


'''_______ Python Modules            

Python Modules
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:

exit()
Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)
Use a Module
Now we can use the module we just created, by using the import statement:

exit()
Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")
Note: When using a function from a module, use the syntax: module_name.function_name.

Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

exit()
Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
exit()
Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

exit()
Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

exit()
Import and use the platform module:

import platform

x = platform.system()
print(x)
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

exit()
List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
Note: The dir() function can be used on all modules, also the ones you create yourself.

Import From Module
You can choose to import only parts from a module, by using the from keyword.

exit()
The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
exit()
Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
Note: When importing using the from keyword, do not use the module name when referring to elements in the module. exit(): person1["age"], not mymodule.person1["age"]
'''


'''_______ Python Dates              

Python Datetime
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

exit()
Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)
Date Output
When we execute the code from the exit() above the result will be:

2024-01-28 08:47:18.251607
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

exit()
Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

exit()
Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

exit()
Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
A reference of all the legal format codes:

Directive	Description	exit()	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
# import time
# print(time.sleep(1))    ## used for threading
# exit()
'''



'''_______ Python Math               

Python Math
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

exit()
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
The abs() function returns the absolute (positive) value of the specified number:

exit()
x = abs(-7.25)

print(x)
The pow(x, y) function returns the value of x to the power of y (xy).

exit()
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

import math
When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for exit(), returns the square root of a number:

exit()
import math

x = math.sqrt(64)

print(x)
The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

exit()
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
The math.pi constant, returns the value of PI (3.14...):

exit()
import math

x = math.pi

print(x)
Complete Math Module Reference
In our Math Module Reference you will find a complete reference of all methods and constants that belongs to the Math module.
'''


'''_______ Python JSON               

Python JSON
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.

exit()
Import the json module:

import json
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.

The result will be a Python dictionary.

exit()
Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

exit()
Convert from Python to JSON:

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
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
exit()
Convert Python objects into JSON strings, and print the values:

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
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
exit()
Convert a Python object containing all the legal data types:

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
Format the Result
The exit() above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:

exit()
Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

exit()
Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))
Order the Result
The json.dumps() method has parameters to order the keys in the result:

exit()
Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)
'''


'''_______ Python RegEx              

Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re
RegEx in Python
When you have imported the re module, you can start using regular expressions:

exit()
Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	exit()	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 	 
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	exit()	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
 
The findall() Function
The findall() function returns a list containing all matches.

exit()
Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:

exit()
Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
 
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

exit()
Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
If no matches are found, the value None is returned:

exit()
Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
 
The split() Function
The split() function returns a list where the string has been split at each match:

exit()
Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
You can control the number of occurrences by specifying the maxsplit parameter:

exit()
Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
 
The sub() Function
The sub() function replaces the matches with the text of your choice:

exit()
Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
You can control the number of replacements by specifying the count parameter:

exit()
Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
 
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

exit()
Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
exit()
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
exit()
Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
exit()
Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
Note: If there is no match, the value None will be returned, instead of the Match Object.

# import re
# w="coder"
# if re.match(w,"code"):
    # print("a")
# else:
    # print("b")
    
    


# def square_numbers(n):
    # for i in range(n):
        # yield i ** 2

# # Using the generator to iterate over the sequence of squared numbers
# my_generator = square_numbers(5)

# for num in my_generator:
    # print(num)



# import itertools as it
# for i in it.count(1):
    # if (100-i==0):
        # break
    # print(i)


# A=[1,2,3,4,5,6,7]
# G=iter(A)
# next(G)
# for num in G:
    # print(num)
    # next(G)
    # next(G)
# exit()


# import re
# pattern = r"[\d]+"
# x=re.search(pattern,"good luck in 2017!")
# y=x.group()
# print(int(y)%100+3)
# exit()

# import random
# print(random.randint(1,20))
# exit()


# import time
# print(time.sleep(1))    ## used for threading
# exit()


'''


'''_______ Python PIP                

Python PIP
What is PIP?
PIP is a package manager for Python packages, or modules if you like.

Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:

exit()
Check PIP version:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version
Install PIP
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

Download a Package
Downloading a package is very easy.

Open the command line interface and tell PIP to download the package you want.

Navigate your command line to the location of Python's script directory, and type the following:

exit()
Download a package named "camelcase":

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
Now you have downloaded and installed your first package!

Using a Package
Once the package is installed, it is ready to use.

Import the "camelcase" package into your project.

exit()
Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
Find Packages
Find more packages at https://pypi.org/.

Remove a Package
Use the uninstall command to remove a package:

exit()
Uninstall the package named "camelcase":

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:

Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase\*
Proceed (y/n)?
Press y and the package will be removed.

List Packages
Use the list command to list all the packages installed on your system:

exit()
List installed packages:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
Result:

Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1
'''



'''_______ Python Try..Except        

Python Try Except
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

exit()
The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

exit()
This statement will raise an error, because x is not defined:

print(x)
Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

exit()
Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
Else
You can use the else keyword to define a block of code to be executed if no errors were raised:

exit()
In this exit(), the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.

exit()
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
This can be useful to close objects and clean up resources:

exit()
Try to open and write to a file that is not writable:

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
The program can continue, without leaving the file object open.

Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

exit()
Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

exit()
Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# print("__exception")

# from math import sqrt as math
# try:
    # print(math(4))
# except TypeError:
    # print("TypeError occured")
# except:
    # print("An error occured")


# #error handling..exception
# try:
    # str="Python"
    # int=42
    # print(int//str)
# except TypeError:
    # int=12
# finally:
    # print(int+8)


# # try:
    # # if("hello world"/0==1):
        # # print(0)
    # # except ZeroDivisionError:
        # # print(1)
    # # except SyntaxError:
        # # print(2)
    # # except TypeError:
        # # print(3)
    # # finally:    
        # # print(9)

# exit()
# a=[4,5,6,7]
# try:
    # print(a[True])
# except:
    # print(0)

'''



'''_______ Python User Input         

Python User Input
User Input
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.

The following exit() asks for the username, and when you entered the username, it gets printed on the screen:

Python 3.6
username = input("Enter username:")
print("Username is: " + username)
Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)
Python stops executing when it comes to the input() function, and continues when the user has given some input.




#print("# taking user Input")
# hey=input()
# print(hey,"<<< this is string don't forget that")
exit()

# #working with input
# print("input weight:")
# wht=float(input())

# print("input height:")
# ht=float(input())

# print("name:")
# name =input()
# print("age:")
# age=input()
# print(name+ "is"+ age)

'''


'''_______ Python String Formatting  

Python String Formatting
To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

exit()
Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
You can add parameters inside the curly brackets to specify how to convert the value:

exit()
Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"
Check out all formatting types in our String format() Reference.

Multiple Values
If you want to use more values, just add more values to the format() method:

print(txt.format(price, itemno, count))
And add more placeholders:

exit()
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

exit()
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
Also, if you want to refer to the same value more than once, use the index number:

exit()
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

exit()
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
'''


'''_______ Python File Handling      

Python File Open
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.
'''


'''_______ Python Read files         

Python File Open
Open a File on the Server
Assume we have the following file, located in the same folder as Python:

demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

exit()
f = open("demofile.txt", "r")
print(f.read())
If the file is located in a different location, you will have to specify the file path, like this:

exit()
Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:

exit()
Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))
Read Lines
You can return one line by using the readline() method:

exit()
Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())
By calling readline() two times, you can read the two first lines:

exit()
Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
By looping through the lines of the file, you can read the whole file, line by line:

exit()
Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)
Close Files
It is a good practice to always close the file when you are done with it.

exit()
Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()
Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
'''


'''_______ Python Write/Create files 

Python File Write
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

exit()
Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
exit()
Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
Note: the "w" method will overwrite the entire file.

Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

exit()
Create a file called "myfile.txt":

f = open("myfile.txt", "x")
Result: a new empty file is created!

exit()
Create a new file if it does not exist:

f = open("myfile.txt", "w")
'''



'''_______ Python Delete files       

Python Delete File
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:

exit()
Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

exit()
Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
Delete Folder
To delete an entire folder, use the os.rmdir() method:

exit()
Remove the folder "myfolder":

import os
os.rmdir("myfolder")
Note: You can only remove empty folders.

'''



''' _______ Python Numpy





# import numpy as np
 # # b=np.array([[2,5],[3,7]])
# ak=np.array([[11,[2,2],[2,2],34],[34,34,3]])
# ak=ak.transpose();

# print(ak)

# ar1=np.array([[2,5],[3,7]])
# ar1=ar1.transpose();
# print(ar1)



# arr1=np.array([[1,2,3],[4,5,6]])

# print(arr1)


# exit()


# import numpy as np
# a=np.array([1,2,3,5,8])
# b=np.array([0,3,4,2,1])
# c=a+b
# print(c)
# c=c*a
# print(c)



# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]])
# arr1=arr1.transpose();
# print(arr1[1][0]);
# exit()



# import numpy as np
# a = np.array([[1,2,3],[0,1,4]])
# print(a.size)



# import numpy as np
# a = np.arange(0, 8, 2)
# b = np.arange(1, 8, 3)
# print(a[2] == b[1])
# exit()
'''


