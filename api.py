import socket
HOST = '127.0.0.1'
PORT = 2221
class ApiClass:
    def socket_deco(func):
        def wrapper(*args, **kwargs):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            client_choice = func(*args, **kwargs)[0]
            client_socket.sendall(bytes(client_choice, 'utf-8'))
            client_socket.recv(1024)
            client_message = func(*args, **kwargs)
            client_socket.sendall(bytes(client_message, 'utf-8'))
            client_socket.recv(1024)
        return wrapper
    
    @socket_deco
    def create_account(costumer_name, account_number, current_balance):
        yield '1'
        return costumer_name, account_number, current_balance

    @socket_deco
    def deposit_or_withdraw(costumer_name, account_number, costumer_money, costumer_choice):
        yield '2'
        return costumer_name, account_number, costumer_money, costumer_choice

    @socket_deco
    def money_transaction(costumer_name, account_number, receiver_name, receiver_account, transaction_money):
        yield '3'
        return costumer_name, account_number, receiver_name, receiver_account, transaction_money
