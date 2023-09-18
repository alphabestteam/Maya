import socket
HOST = '127.0.0.1'
PORT = 2221
MEMORY = 1024

def client_actions():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))
    while True:
        data = my_socket.recv(MEMORY).decode("utf-8")
        print("Received from server: " + str(data))
        client_message = input("enter message: ")
        my_socket.sendall(bytes(client_message, "utf-8"))

if __name__ == "__main__":
    client_actions()
