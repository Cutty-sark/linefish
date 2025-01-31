import socket  # Import the socket module for networking

# Define the server address and port
HOST = "127.0.0.1"  # This means the server will only accept connections from this machine (localhost)
PORT = 65433        # Port to listen on (must match the client)

# Create a TCP socket using IPv4 addressing
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the specified host and port
    s.listen()  # Start listening for incoming connections
    print(f"Server listening on {HOST}:{PORT}...")

    # Wait for a client to connect (blocking call)
    conn, addr = s.accept()  # When a client connects, accept() returns a new socket (conn) and the client address (addr)
    print(f"Connected by {addr}") # Print the client's address
    #print(s.accept())
    # Use 'with' to ensure the connection socket is properly closed when done
    with conn:
        print("Connection established. Waiting for data...")
        while True:  # Keep the server running to handle messages
            data = conn.recv(1024)  # Receive up to 1024 bytes of data from the client
            if not data:  # If no data is received, the client has disconnected
                print("Client disconnected.")
                break  # Exit the loop and close the connection

            print(f"Received: {data}")  # Print the message received from the client
            conn.sendall(data)  # Echo the message back to the client