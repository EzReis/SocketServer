import socket

#connexion parameters
port = 8040

#create a new socket 
s = socket.socket()
print("socket binded!")

s.bind(('', port)) #withot any string in ip field, this socket will be in listening mode

s.listen(5) #the server will accept up to five connections

while True:
    c, addr = s.accept()
    print("We are connected with: %s".format(addr))
    c.send("Thank you for connecting!".encode())
    c.close()

    break


    