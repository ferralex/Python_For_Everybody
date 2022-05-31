"""
Add code to Exercise 3 to figure out who has the most messages in the file.

After all the data has been read and the dictionary has been created,
look through the dictionary using a maximum loop (see Section [maximumloop])
to find who has the most messages and print how many messages the person has.
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

print(max(counts, key=counts.get), counts[max(counts, key=counts.get)])
