from costumer_class import Costumer
import socket, os, random, json
COSTUMER_PATH = "costumers/"
HOST = '127.0.0.1'
PORT = 2221
MEMORY = 1024

class Bank:
    def __init__(self) -> None:
        self._costumers_list = self.get_costumers_list()
    
    @property
    def costumers_list(self):
        return self._costumers_list
    

    def get_costumers_list(self) -> list:
        """
        A function that creates a costumer's list from files in costumers folder
        """
        for costumer_file in os.scandir(COSTUMER_PATH):
            new_costumer = Costumer(costumer_file.path)
            self.costumers_list.append(new_costumer)
        return self.costumers_list
    

    def start_listen(self):
        """
        A function that listens to costumers and preforms their wishes
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        while True:
            conn, costumer_addr = server_socket.accept()
            print(f"server is connect by the address: {costumer_addr}")
            conn.sendall(bytes("Please enter 1: To create account\n2: To deposit or withdrawal money\n\
3: To transfer money".encode('utf-8')))
            costumer_data = conn.recv(MEMORY)
            if costumer_data == "1":
                conn.sendall(bytes("Please enter your name and your current balance (name current-balance)\n".encode('utf-8')))
                costumer_info = conn.recv(MEMORY)
                self.create_account(costumer_info)
                print("action was successful")
            elif costumer_data =="2":
                conn.sendall(bytes("Would you like to deposit or withdraw money?".encode('utf-8')))
                costumer_choice = conn.recv(MEMORY)
                conn.sendall(bytes("Enter your name, your account number, and the amount of money you want to deposit or withdraw:\n".encode('utf-8')))
                costumer_name, account_number, costumer_money = conn.recv(MEMORY).decode('utf-8').split(" ")
                print(self.deposit_or_withdrawal(costumer_name, account_number, costumer_money, costumer_choice))
            elif costumer_data == "3":
                conn.sendall(bytes("Please enter your information (name account number transaction money):\n".encode('utf-8')))
                costumer_name, account_number, transaction_money = conn.recv(MEMORY).decode('utf-8').split(" ")
                conn.sendall(bytes("Please enter the info for the person you want to transfer the money to (name account number ):\n".encode('utf-8')))
                receiver_name, receiver_account = conn.recv(MEMORY).decode('utf-8').split(" ")
                print(self.transfer_money(costumer_name, account_number, receiver_name, receiver_account, transaction_money))
            if costumer_data == b"stop":
                break
        server_socket.close()


    def create_account(self, costumer_info: str) -> None:
        """
        A function that gets from costumer their info and creates a new file with it
        and adds it to the costumers' list as a costumer object
        """
        costumer_name, costumer_balance = costumer_info.split(" ")
        costumer_account_num = self.new_account_number()
        with open(f"{COSTUMER_PATH}{costumer_account_num}", 'w') as new_costumer_file:
            json.dumps({"name": costumer_name, "current balance": costumer_balance, 
                                    "account number": costumer_account_num}, new_costumer_file)
        new_costumer = Costumer(f"{COSTUMER_PATH}{costumer_account_num}")
        self.costumer_list.append(new_costumer)


    def new_account_number(self) -> int:
        """
        A function that sets a random unique account number and returns it
        """
        while True:
            account_number = random.randint(10000000, 100000000000)
            for costumer in self.costumer_list:
                if account_number == costumer.account_number:
                    continue
            return account_number
            

    def deposit_or_withdrawal(self, costumer_name: str, account_number: int, costumer_money: float,
                               costumer_action: str) -> str:
            """
            A function that deposits or withdraws money from account if it's valid
            """
            with open(f"{COSTUMER_PATH}{account_number}", 'w') as costumer_file:
                costumer_data = json.load(costumer_file)
                if costumer_name == costumer_data["costumer name"]:
                    if costumer_action.lower == "deposit":
                        costumer_data["current balance"] += costumer_money
                    elif costumer_action.lower == "withdraw":
                        if costumer_data["current balance"] >= costumer_money:
                            costumer_data["current balance"] -= costumer_money
                        else:
                            return "Not enough money in account for that action"
                    else:
                        return "Invalid input"
                    json.dumps({"name": costumer_name, "current balance": costumer_data["current balance"], 
                    "account number": account_number}, costumer_file)
                    for costumer in self.costumer_list:
                        if costumer.account_number == account_number:
                            costumer.current_balance = costumer_data["current balance"]
                            return "Action was successful"
                return "Given name doesn't match costumer's name on account"


    def transfer_money(self, costumer_name: str, costumer_account: int,
                        receiver_name: str, receiver_account: int, transaction_money: float):
        """
        A function that gets costumer's info and transfers money from their account to another person
        """
        with open(f"{COSTUMER_PATH}{costumer_account}", 'r') as costumer_file:
            costumer_data = json.load(costumer_file)
            if costumer_name == costumer_data["costumer name"] and costumer_account == costumer_data["account number"]:
                if costumer_data["current_balance"] < transaction_money:
                    return "Not enough money for this transaction"
        with open(f"{COSTUMER_PATH}{receiver_account}", 'w') as receiver_file:
            receiver_data = json.load(receiver_file)
            if receiver_name == receiver_data["costumer name"] and receiver_account == receiver_account["account number"]:
                receiver_data["current balance"] += transaction_money
                for receiver in self.costumer_list:
                    if receiver.account_number == receiver_account:
                        receiver.current_balance = receiver_data["current balance"]
                        return "Action was successful"
        return "Invalid input"    

def main():
    test_bank = Bank()
    test_bank.start_listen()


if __name__ == "__main__":
    main()
