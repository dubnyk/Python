import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 1337))

print('Waiting for incoming data')

while True:
    received, addr = sock.recvfrom(1024)
    received_message = received.decode("utf-8")
    print("[RECEIVED]: " + received_message.strip())
    sock.sendto(str.encode("You said: " + received_message), addr)

socket.close()
