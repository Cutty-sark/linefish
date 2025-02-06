import socket
import psutil
import time

# Get all active network connections -- not going to work as getsocket() not module of socket. Using netstat and psutil easy but socket is portable
connections = [s for s in socket.getsockets() if s]

# Define the table headers
headers = ["Conn.", "Time", "Proc. name", "PID", "Proto.", "State", "Send Q", "Recv. Q", "Proc. loc."]

# Iterate through each connection and get the corresponding process information
for connection in connections:
    # Get the process ID (PID) of the process that owns the connection
    pid = connection.fileno()
    process = psutil.Process(pid)

    # Using psutil here to grab  process name, location, PID, state, protocol, and receive/send queues
    process_name = process.name()
    process_location = process.exe()
    process_state = process.status()
    process_protocol = connection.family()
    process_recv_queue = connection.recv(1024)
    process_send_queue = connection.send(1024)

    # Grab current time - will be useful if cron or persistence coding
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # table dump
    print("{:<7} {:<12} {:<14} {:<6} {:<8} {:<8} {:<10} {:<10} {:<14}".format(*[current_time] + [process_name, str(pid), str(process_protocol), process_state, str(process_recv_queue), str(process_send_queue), process_location] + [None] * (len(headers) - len(headers) - 1)))

    # Close the connection
    connection.close()
