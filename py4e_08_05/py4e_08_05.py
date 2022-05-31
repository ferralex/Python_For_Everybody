"""
Write a program to read through the mail box data and when you find line that
starts with "From", you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the
From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines
and print out a count at the end.
"""



file_name = input("Enter the file name: ")

#try to open the file defined by the user
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

#read through to return the email addresses
emails = 0
for line in fhand:
    line = line.rstrip()
    #search for lines starting with "From"
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        #split the line into words
        email_from = line.split()
        #print and count the email addresses
        print(email_from[1])
        emails += 1
#print the number of email addresses
print(f"There were {emails} lines in the file with From as the first word")
