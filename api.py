import socket
HOST = '127.0.0.1'
PORT = 2226
class ApiClass:
    def socket_deco(func):
        def wrapper(*args):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            client_choice = client_message = ""
            function_output = list(func(*args))
            for index in range(len(function_output)):
                if index == 0:
                    client_choice = function_output[index]
                else:
                    client_message += str(function_output[index]) + " "
            client_socket.sendall(bytes(client_choice.encode()))
            client_socket.recv(1024)
            client_socket.sendall(bytes(client_message, encoding = 'utf-8'))
        return wrapper
    
    @socket_deco
    def create_account(self, costumer_name: str, current_balance: float) -> tuple:
        return '1', costumer_name, current_balance

    @socket_deco
    def deposit_or_withdraw(self, costumer_name: str, account_number: int, costumer_money: float, costumer_choice: str) -> tuple:
        return '2', costumer_name, account_number, costumer_money, costumer_choice

    @socket_deco
    def money_transaction(self, costumer_name: str, account_number: int, receiver_name: str, receiver_account: int, transaction_money: float) -> tuple:
        return '3', costumer_name, account_number, receiver_name, receiver_account, transaction_money

def main():
    api = ApiClass()
    api.create_account("MayaAAdiid", 9.221)
    api.create_account("sjsj", 383)
    api.deposit_or_withdraw("MayaAAdiid", 471012857441, 5, "withdraw")
    api.money_transaction("MayaAAdiid", 471012857441, "sjsj", 213948693640, 1000)



if __name__ == "__main__":
    main()