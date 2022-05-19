"""
Write a program to prompt for a file name, and then read through the file and look for lines of the form:

*X-DSPAM-Confidence:0.8475*

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
"""

file_name = input("Enter the file name: ")

#try to open the file defined by the user
try:
    fhand = open(file_name)
except:
    print("Can't open ", file_name)
    quit()

#look for specific lines starting with "X-DSPAM-Confidence:"
good_lines = 0
spam_confidence_total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        #extract the floating-point and sum them
        spam_confidence_position = line.find(":")
        spam_confidence = float(line[spam_confidence_position+1:])
        spam_confidence_total = spam_confidence_total + spam_confidence
        #count them
        good_lines += 1

#calculate the average span confidence
spam_confidence_avg = spam_confidence_total / good_lines
print(spam_confidence_avg)
