import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Ready!')

while True:
    message = input("[SEND]: ")
    sock.sendto(str.encode(message), ("0.0.0.0", 1337))
    received = sock.recvfrom(1024)
    print(received[0].decode("utf-8"))

socket.close()
