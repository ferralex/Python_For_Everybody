
"""
Write a program that categorizes each mail message by which day of the week
the commit was done.
To do this look for lines that start with "From", then look for the third word
and keep a running count of each of the days of the week.
At the end of the program print out the contents of your dictionary
(order does not matter).
"""
#file name input by user
file_name = input("Enter the file name: ")
#try to open the file defined by the user
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

count = dict()
for line in fhand:
        words = line.split()
        #consider only lists with "From" at [0] and length >=3
        if len(words) >= 3 and words[0] == "From":
            if words[2] not in count:
                #use the 3rd string from the list "words" as the dictionary key
                count[words[2]] = 1
            else:
                count[words[2]] = count[words[2]]+1
print (count)
