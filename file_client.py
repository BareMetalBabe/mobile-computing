import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(('localhost', 15000))

# Receive file name
file_name = client.recv(1024).decode()

# Receive file data
data = client.recv(1024)

# Save file
f = open("Received_" + file_name, "wb")
f.write(data)

f.close()
client.close()

print("File received successfully!")