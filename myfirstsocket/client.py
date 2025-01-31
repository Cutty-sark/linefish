import socket  # Import the socket module

HOST = "127.0.0.1"  # The server's address (localhost, same machine)
PORT = 65433        # Must match the server's port

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server connection attempt...")
    try:
        s.connect((HOST, PORT))  # Connect to the server at the given address and port
        print("Successfully connected")
    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running first.")
    message = b"Hello, server!"  # Data to send, b tells socket that this is a byte string - would fuck up if not for some reason
    print(f"Sending: {message}")
    s.sendall(message)  # Send data
    data = s.recv(1024)  # Receive up to 1024 bytes of data from the server

    print(f"Received: {data!r}")  # Print the received data