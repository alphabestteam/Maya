import socket

def client():
    HOST = '127.0.0.1'
    PORT = 2221

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_message = input("Please enter a message that will be send to the server\n")
    client_socket.sendall(bytes(client_message, 'utf-8'))
    server_data = client_socket.recv(1024)
    print(f"received data from server: {server_data}")

if __name__ == '__main__':
    client()