from costumer_class import Costumer
import socket, os, random, json
COSTUMER_PATH = "costumers/"
HOST = '127.0.0.1'
PORT = 2226
MEMORY = 1024

class Bank:
    def __init__(self) -> None:
        self.costumers_list = []
        if os.path.exists(COSTUMER_PATH):
            for costumer_file in os.listdir(COSTUMER_PATH):
                if os.path.isfile(os.path.join(COSTUMER_PATH, costumer_file)) and costumer_file != ".DS_Store":
                    new_costumer = Costumer(f"{COSTUMER_PATH}{costumer_file}")
                    self.costumers_list.append(new_costumer)

    def start_listen(self):
        """
        A function that listens to costumers and preforms their wishes
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("waiting for connection")
        while True:
            conn, costumer_addr = server_socket.accept()
            print(f"server is connect by the address: {costumer_addr}")
            conn.sendall(bytes("Please enter 1: To create account\n2: To deposit or withdrawal money\n\
3: To transfer money".encode('utf-8')))
            costumer_data = conn.recv(MEMORY).decode()
            if costumer_data == "1":
                conn.sendall(bytes("Please enter your name and your current balance (name current-balance)\n".encode('utf-8')))
                costumer_info = conn.recv(MEMORY).decode()
                self.create_account(costumer_info)
                print("action was successful")
            elif costumer_data =="2":
                conn.sendall(bytes("Enter your name, your account number, the amount of money, and wether you want to deposit or withdraw :\n".encode('utf-8')))
                costumer_choice = conn.recv(MEMORY).decode()
                print(self.deposit_or_withdrawal(costumer_choice))
            elif costumer_data == "3":
                conn.sendall(bytes("Please enter your information (name account number transaction money):\n".encode('utf-8')))
                costumer_choice = conn.recv(MEMORY).decode()
                print(self.transfer_money(costumer_choice))
            elif costumer_data == b"stop":
                break
        server_socket.close()


    def create_account(self, costumer_info: str) -> None:
        """
        A function that gets from costumer their info and creates a new file with it
        and adds it to the costumers' list as a costumer object
        """
        costumer_name, costumer_balance, _ = costumer_info.split(" ")
        costumer_account_num = self.new_account_number()
        with open(f"{COSTUMER_PATH}{costumer_account_num}", 'w') as new_costumer_file:
            json.dump({"name": costumer_name, "current balance": costumer_balance, "account number": costumer_account_num}, new_costumer_file, indent=4)
        new_costumer = Costumer(f"{COSTUMER_PATH}{costumer_account_num}")
        self.costumers_list.append(new_costumer)
        for index in range(len(self.costumers_list)):
            print(self.costumers_list[index].costumer_name)


    def new_account_number(self) -> int:
        """
        A function that sets a random unique account number and returns it
        """
        while True:
            account_number = random.randint(10000000, 999999999999)
            for costumer in self.costumers_list:
                if account_number == costumer.account_number:
                    continue
            return account_number
            

    def deposit_or_withdrawal(self, costumer_choice: str) -> str:
            """
            A function that deposits or withdraws money from account if it's valid
            """
            costumer_name, account_number, costumer_money, costumer_action, _ = costumer_choice.split(" ")
            with open(f"{COSTUMER_PATH}{account_number}", 'r') as costumer_file:
                costumer_data = json.load(costumer_file)
            with open(f"{COSTUMER_PATH}{account_number}", 'w') as costumer_file:
                if not costumer_name == costumer_data["name"]:
                    return "Given name doesn't match costumer's name on account"
                else:
                    if costumer_action.lower() == "deposit":
                        costumer_data["current balance"] = float(costumer_data["current balance"]) + float(costumer_money)
                    elif costumer_action.lower() == "withdraw":
                        if float(costumer_data["current balance"]) >= float(costumer_money):
                            costumer_data["current balance"] = float(costumer_data["current balance"]) - float(costumer_money)
                        else:
                            return "Not enough money in account for that action"
                    else:
                        return "Invalid input"
                    json.dump({"name": costumer_name, "current balance": costumer_data["current balance"], 
                    "account number": account_number}, costumer_file, indent=4)
                    for costumer in self.costumers_list:
                        if int(costumer.account_number) == int(account_number):
                            costumer.current_balance = float(costumer_data["current balance"])
                            return "Action was successful"
                


    def transfer_money(self, costumer_choice: str) -> str:
        """
        A function that gets costumer's info and transfers money from their account to another person
        """
        costumer_name, costumer_account, receiver_name, receiver_account, transaction_money, _ = costumer_choice.split(" ")
        with open(f"{COSTUMER_PATH}{costumer_account}", 'r') as costumer_file:
            costumer_data = json.load(costumer_file)
            if not (costumer_name == costumer_data["name"] and int(costumer_account) == int(costumer_data["account number"])):
                return "Invalid input"  
            else:
                if float(costumer_data["current balance"]) < float(transaction_money):
                    return "Not enough money for this transaction"
                else:
                    with open(f"{COSTUMER_PATH}{receiver_account}", 'r') as receiver_file:
                        receiver_data = json.load(receiver_file)
                    with open(f"{COSTUMER_PATH}{receiver_account}", 'w') as receiver_file:
                        print(receiver_account, type(receiver_account))
                        if not(receiver_name == receiver_data["name"] and int(receiver_account) == int(receiver_data["account number"])):
                            return "Invalid input"  
                        else:
                            receiver_data["current balance"] = float(receiver_data["current balance"]) + float(transaction_money)
                            with open(f"{COSTUMER_PATH}{costumer_account}", 'w') as costumer_file: #updates the balance of the costumer that made the transaction
                                costumer_data["current balance"] = float(costumer_data["current balance"]) - float(transaction_money)
                                json.dump({"name": receiver_name, "current balance": receiver_data["current balance"], 
                    "account number": receiver_account}, receiver_file, indent=4)
                                json.dump({"name": costumer_name, "current balance": costumer_data["current balance"], 
                    "account number": costumer_account}, costumer_file, indent=4)
                            for costumer in self.costumers_list:
                                if int(costumer.account_number) == int(receiver_account):
                                    costumer.current_balance = receiver_data["current balance"]
                                if int(costumer.account_number) == int(costumer_account):
                                    costumer.current_balance = costumer_data["current balance"] 
    
                    return "Action was successful"
              

def main():
    test_bank = Bank()
    test_bank.start_listen()


if __name__ == "__main__":
    main()
