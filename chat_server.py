import socket

# Start a socket object using IPv4 properties and TCP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to our local computer on IP 0.0.0.0, port 1337
sock.bind(("0.0.0.0", 1337))
# Start listening with a backlog size of 10
sock.listen(10)

conn = False

while True:
    if conn is False:
        print('Waiting for connection')
        conn, client = sock.accept()
        print('Connection from', client)
    else:
        received = conn.recv(1024)
        print(received)
    #else:
        #received = conn.recv(1024)
        #received_message = received.decode("utf-8")
        #print("[RECEIVED]: " + received_message)
        #conn.send(str.encode("You said: " + received_message))
sock.close()
