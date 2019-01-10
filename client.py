import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

client.send("I am CLIENT\n")

from_server = client.recv(4096)

client.close()

print from_server
