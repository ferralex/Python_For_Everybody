"""
Write a program that reads a file and prints the letters in decreasing order
of frequency.
Your program should convert all the input to lower case and
only count the letters a-z.
Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z.
Find text samples from several different languages and see how
letter frequency varies between languages.
"""
#file name input by user
file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

#create a dictionary with letters as key and count as value
counts = dict ()
for line in fhand:
    #lower every letter of the string
    line = line.lower()
    #remove spaces from the string
    line = line.replace(" ","")
    #check if every character is a letter and count the letters
    for letter in line:
        if letter.isalpha() == False:
            continue
        else:
            for l in letter:
                counts[l] = counts.get(l,0)+1

#print the letters in decreasing order of frequency
ranking = list()
#create a list of tuples
for k,v in counts.items():
    ranking.append((v,k))
#sort the list in descending order
ranking = sorted (ranking, reverse = True)
print (ranking)
