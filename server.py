import socket
def server():
    HOST = '127.0.0.1'
    PORT = 2221

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"The server is listening on port: {PORT} on host: {HOST}")
    while True:
        conn, client_addr = server_socket.accept()
        print(f"server is connect by the address: {client_addr}")
        client_data = conn.recv(1024)
        if client_data:
            print(f"data from client:\n{client_data}")
            conn.sendall(client_data.upper())
        if client_data == b"stop":
            break
    server_socket.close()


if __name__ == '__main__':
    server()