"""
This program counts the distribution of the hour of the day for each
of the messages.
You can pull the hour from the "From" line by finding the time string
and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts,
 one per line, sorted by hour
"""
#dictionary to store the e-mails time as key and their count as value
dic = dict()

#open file
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

#create a dictionary storing e-mails time as key and their count as value
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        #split at ':'
        hour = words[5].split(':')
        #use the first string from the list 'hour' as key of the dictionary
        dic[hour[0]] = dic.get(hour[0],0)+1

#sort by hour
for k,v in sorted (dic.items()):
    print (k,v)
