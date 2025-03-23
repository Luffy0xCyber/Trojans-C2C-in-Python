# Python Trojan (C2 Client-Server)

**Disclaimer**: For ethical hacking and educational use only.

## Description
I've decided to create a simple Python Trojan as a learning exercise. 
It's a basic Command & Control (C2) system with a client-server architecture.
I will improve it over time.
---
A lightweight Command & Control system in Python featuring:
- Remote shell execution
- Directory navigation with persistent working directory
- Output logging with encoding-safe handling

## Structure
- `client.py`: Connects to the server and executes commands
- `server.py`: Sends commands and logs responses
- `session_log.txt`: Stores session outputs

## Usage
1. Run `server.py`
2. Run `client.py`
3. Execute commands like `whoami`, `cd`, `dir`, `ipconfig`...

## TODO (coming soon)
- Add file transfer
- Encrypt client-server communication
- Auto system info on connection
- Multi-client support