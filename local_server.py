import socket
import threading

# Server configuration
host = '0.0.0.0'
port = 12346
color_map = {'r': 'red', 'g': 'green', 'b': 'blue'}

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    with client_socket:
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    print(f"Connection with {client_address} closed.")
                    break

                response_lines = [color_map[char] for char in message.lower() if char in color_map]

                if response_lines:
                    for line in response_lines:
                        print(line)  # Print each color

                    response = "\n".join(response_lines)
                    client_socket.send(response.encode('utf-8'))
                else:
                    client_socket.send(b"")  # Send empty response if no valid chars

            except Exception as e:
                print(f"Error handling client {client_address}: {e}")
                break
            

def start_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(5)
            print(f"Server listening on {host}:{port}")

            while True:
                print("Waiting for a connection...")
                client_socket, client_address = server_socket.accept()
                thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                thread.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_server()
