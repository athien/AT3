# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 3: PART C1 - Server and Client socket Manager
# This is the Python program used to manage connections. This program facilitates the server side connection.

# Import the socket library
import socket

# Create a socket object
s = socket.socket()
print("Socket created, successfully!")

# Define port 1234 to be reserved on the server computer
port = 1234

# Bind the port
s.bind(('', port))
print("The socket has been bound to %s" %(port))

# Use the listen() function to standby for a connection
s.listen(3)
print("The socket is ready to listen")

# Establish a connection with client
while True:
    c, addr = s.accept()
    print("The connection has been established successfully with", addr)

    # Print a message of the day
    output = "Thank you for connecting to the server"
    c.sendall(output.encode('utf-8'))

    # Close the connection with the client
    c.close()
