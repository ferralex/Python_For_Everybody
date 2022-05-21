"""
Write a program to look for lines of the form

`New Revision: 39772`

and extract the number from each of the lines using a regular expression and
the findall() method.
Compute the average of the numbers and print out the average.
"""

#file name input by user
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

revisions = list()

import re
for line in fhand:
    #search for a line starting with "New Revisions " and extracts the numbers
    #after it
    y = re.findall('^New Revision:\s([0-9]+)',line)
    #exclude empty lists
    if len(y) > 0:
        num = int(y[0])
        revisions.append(num)

print("Average: ",sum(revisions)/len(revisions))
