"""
Download a copy of the file from www.py4e.com/code3/romeo.txt

Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list.
If the word is not in the list, add it to the list.
"""
line_words = list()
unique_words = list()

fhand = open ("romeo.txt")
for line in fhand:
    line = line.rstrip()
    #for each line, split the line in a list of words (creates a list of lists)
    words = line.split()
    line_words.append(words)

#For each word, check if the word is already present
for list in line_words:
    for word in list:
        if word not in unique_words:
            unique_words.append(word)

#sort and print the resulting words in alphabetical order
unique_sorted = sorted(unique_words)
print (unique_sorted)
