"""
Use urllib to replicate the previous exercise of (1) retrieving the document
 from a URL, (2) displaying up to 3000 characters, and (3) counting
 the overall number of characters in the document.
 Don't worry about the headers for this exercise,
 simply show the first 3000 characters of the document contents.
"""


import urllib.request, urllib.parse, urllib.error
import ssl

#in case of SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    myurl = input("Enter a web URL: ")
    #read the file and get a string in UTF-8
    fhand = urllib.request.urlopen(myurl, context = ctx).read()
    #decode the file in UNICODE
    mystring = fhand.decode()
    #print the firs 3000 characters
    print (mystring[:3001])
    print (len(mystring))
except:
    print ("ERROR")
