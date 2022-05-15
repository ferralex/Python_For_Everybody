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
