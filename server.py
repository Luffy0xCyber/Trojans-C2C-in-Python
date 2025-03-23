import socket

HOST = '127.0.0.1' # Localhost IP
PORT = 4444        # Port to listen on
# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the IP and port
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Waiting for connection on port {PORT}...")

client_socket, addr = server.accept()
print(f"[+] Connection established with {addr}")

# Open log file
with open("session_log.txt", "a", encoding="utf-8", errors="replace") as log_file:
    while True:
        command = input(">> ")
        if command.lower() == "exit":
            client_socket.send(b"exit")
            break

        client_socket.send(command.encode())
        response = client_socket.recv(4096).decode(errors="replace")

        # Print to console
        print(response)

        # Write to file
        log_file.write(f"Command: {command}\n")
        log_file.write(f"Response:\n{response}\n")
        log_file.write("=" * 40 + "\n")

client_socket.close()
server.close()
