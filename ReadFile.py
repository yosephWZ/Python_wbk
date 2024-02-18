#### ???make it work please????


'''_______ Python Read files         

Python File Open

f = open("demofile.txt", "r")
print(f.read())

exit()

# Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
exit()


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

'''

