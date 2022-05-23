"""
In this assignment you will write a Python program that expands on
http://www.pythonlearn.com/code/urllinks.py (http://www.pythonlearn.com/code/urllinks.py).
The program will use urllib to read the HTML, extract the href= values from
the anchor tags, scan for a tag  that is in a particular position relative to
the first name in the list, follow that link and repeat the process
a number of times and report the last name you find.

Sample problem: Start at
http://python-data.dr-chuck.net/known_by_Fikret.html (http://python-data.drchuck.net/known_by_Fikret.html)
Find the link at position 3 (the first name is 1).
Follow that link. Repeat this process 4 times. The answer is the last name
that you retrieve.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

count = 0

#starts to analyze from this URL
url= "http://python-data.dr-chuck.net/known_by_Fikret.html"
#repeat the process 4 times
while count < 4:
    #list to append the URLs. Resets at every cycle
    lst = list()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    #retrieve the URLs
    tags = soup ("a")
    #keep only the address parts
    for tag in tags:
        lst.append(tag.get("href", None))
    #the next URL to analyze is the one in at position 3
    url = lst[2]
    count += 1

#split the last URL in order to get the name
name = re.split('_|\.|/',url)
print(name[-2])
