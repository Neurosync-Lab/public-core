# UDP Mesh Broadcast Listener
import socket

PORT = 42169
BROADCAST_IP = "255.255.255.255"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('', PORT))

print(f"Listening on UDP {PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"[{addr[0]}]: {data.decode()}")
