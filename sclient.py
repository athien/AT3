# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 3: PART C2 - Server and Client socket Manager
# This is the Python program used to manage connections. This program facilitates the client side connection.

# Import the socket library
import socket

# Create a socket object
s = socket.socket()

# Define the port number (1234)
port = 1234

# Connect to the client to the server on the local computer
s.connect(("127.0.0.1", port))

# Receive the data from the server
print(s.recv(1024))

# Close the connection
s.close()
