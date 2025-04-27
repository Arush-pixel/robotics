import socket

# Client socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Localhost for same computer
port = 12346        # Make sure this matches the server's port
client_socket.connect((host, port))
print(f"Connected to server {host}:{port}")

# Send string to server and receive feedback
try:
    while True:
        message = input("Enter a string (letters 'r', 'g', 'b' only): ")
        if not message:
            break  # Exit if input is empty

        client_socket.send(message.encode('utf-8'))
        reply = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {reply}")
        if not reply:
            break
finally:
    client_socket.close()
    print("Connection closed.")
