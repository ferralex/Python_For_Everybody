"""
Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown
3000 characters.
The program should retrieve the entire document and count the total number
of characters and display the count of the number of characters at the end
 of the document.
"""
import socket

count = int()

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

    #print until we receive data or until we receive 3000 characters
    while True:
        data = mysock.recv(512)
        #count the total number of characters
        for char in data:
            count += 1
        if len(data) < 1 or len(data) > 3000:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print ("ERROR")

print (count)
