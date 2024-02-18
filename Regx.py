

# ?? make it work please ??


''' _______ Python RegEx              



# Python RegEx


# RegEx Module


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
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

# #	Signals a special sequence (can also be used to escape special characters)	"\d"	
import re


txt = "That will be 59 dollars"

#Find all digit characters:

# x = re.findall("\d", txt)
# print(x)

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

# #A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

# x = re.findall("\AThe", txt)

# print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

exit()

# #b	Returns a match where the specified characters are at the beginning or at the end of a word
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

# x = re.findall(r"ain#b", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# r"ain#b"	
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

# x = re.findall(r"\Bain", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

# x = re.findall(r"ain#B", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\r", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# r"ain#B"	

exit()

# #d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

# x = re.findall("\d", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #D	Returns a match where the string DOES NOT contain digits	"\D"	
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

# x = re.findall("\D", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #s	Returns a match where the string contains a white space character	"\s"	
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

# x = re.findall("\S", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #S	Returns a match where the string DOES NOT contain a white space character	"\S"	
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

# x = re.findall("\w", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

# x = re.findall("\W", txt)

# print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

exit()

# #W	Returns a match where the string DOES NOT contain any word characters	"\W"	

exit()

# #Z	Returns a match if the specified characters are at the end of the string	"Spain#Z"	
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

# x = re.findall("Spain#Z", txt)

# print(x)

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
# x = re.search("\s", txt)

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
# x = re.split("\s", txt)
# print(x)
exit()






import re

txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
exit()
 
# The sub() Function



import re

txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
exit()


import re

txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)
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
# x = re.search(r"\bS#w+", txt)
# print(x.span())
exit()

# .string returns the string passed into the function
import re

txt = "The rain in Spain"
# x = re.search(r"\bS#w+", txt)
# print(x.string)
exit()

# .group() returns the part of the string where there was a match
import re

txt = "The rain in Spain"
# x = re.search(r"\bS#w+", txt)
# print(x.group())

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
pattern = r"[\d]+"
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


