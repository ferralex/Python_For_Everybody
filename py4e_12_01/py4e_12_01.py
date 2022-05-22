"""
Change the socket program socket1.py to prompt the user for the URL
so it can read any web page. You can use split('/') to break the URL into
its component parts so you can extract the host name for the socket
connect call.
Add error checking using try and except to handle the condition
where the user enters an improperly formatted or non-existent URL.
"""


import socket
try:
    myurl = input("Enter a web URL: ")
    host = myurl.split("/")
    #make the connection
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host[2], 80))
    #create the request string
    cmd = 'GET ' + myurl + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    #print until we receive data
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print ("ERROR")
