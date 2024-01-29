import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("0.0.0.0", 1337))

print('Connected!')

while True:
    message = input("[SEND]: ")
    sock.send(str.encode(message))
    received = sock.recv(1024)
    print(received.decode("utf-8"))

socket.close()
