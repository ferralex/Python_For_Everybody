"""
Exercise 3: Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address,
and print the dictionary.
"""
#file name input by user
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

counts = dict ()
for line in fhand:
    words  = line.split()
    #consider only lists with "From" at 0 and up to 2 elements
    if len(words) < 2 or words[0] != "From" :
        continue
    else:
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] = counts[words[1]]+1
print (counts)
