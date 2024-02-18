



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
   
   


