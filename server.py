import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind address
server_address = ('localhost', 15000)
server.bind(server_address)

# Listen for client
server.listen(1)

print("Server is waiting for connection...")

# Accept client
connection, client_address = server.accept()

print("Client connected!")

# File name
file_name = "Text.txt"

# Send file name
connection.sendall(file_name.encode())

# Open file
f = open("Text.txt", "rb")

# Read file data
data = f.read()

# Send file data
connection.sendall(data)

# Close file
f.close()

# Close connection
connection.close()
server.close()

print("File sent successfully!")