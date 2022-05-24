"""
In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL
using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other
is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_11961.xml (Sum ends with 89)
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    myurl = input("Enter a web URL: ")
    input = urllib.request.urlopen(myurl).read()
    print ("Retrieved ", len(input), " characters")

    #comments count
    stuff = ET.fromstring(input)
    #find comment tags under comments and put in a list
    lst = stuff.findall("comments/comment")
    print ("Count: ", len(lst))

    #compute the sum of the numbers in the file
    sum = int()
    for item in lst:
        #find the text between the tags count
        num = int(item.find ('count').text)
        sum += num
    print ("Sum: ",sum)

except:
    print ("ERROR")
