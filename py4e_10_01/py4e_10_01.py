"""
Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line.
Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary.
Then sort the list in reverse order and print out the person
who has the most commits.
"""
#dictionary to store email addresses as key and their count as value
dic = dict()
#list to sort the dictionary
ranking = list()

#open file
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

#create a dictionary storing email addresses as key and their count as value
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        if words[1] not in dic:
            dic[words[1]] = 1
        else:
            dic[words[1]] = dic[words[1]]+1

#create a list of tupples. Each tupple is the value and key of each element of
#the dictionary
for k,v in dic.items():
    ranking.append((v,k))

#sort the list in descending order
ranking = sorted (ranking, reverse = True)
#print the first element of the list (the one with the highest value)
print (ranking[0])
