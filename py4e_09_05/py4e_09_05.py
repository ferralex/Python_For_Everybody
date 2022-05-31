"""
This program records the domain name (instead of the address) where the message
was sent from instead of who the mail came from (i.e., the whole email address).
 At the end of the program, print out the contents of your dictionary.
"""
#file name input by user
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

counts = dict()

for line in fhand:
    #split at the space
    words = line.split()

    if len(words) <2 or words[0] != "From":
        continue
    else:
        #split at '@''
        domains = words[1].split('@')
        #use the second string from the list 'domain' as key of the dictionary
        counts[domains[1]] = counts.get(domains[1],0)+1

print (counts)
