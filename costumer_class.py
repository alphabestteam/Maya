import json
class Costumer:
    def __init__(self, costumer_path) -> None:
        with open(f"{costumer_path}", "r") as costumer_file:
            costumer_info = json.load(costumer_file)
            self._costumer_name = costumer_info["name"]
            self._account_number = costumer_info["account number"]
            self._current_balance = costumer_info["current balance"]

    @property
    def costumer_name(self) -> str:
        return self._costumer_name
      
    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def current_balance(self) -> float:
        return self._current_balance  

    @current_balance.setter
    def current_balance(self, new_balance) -> None:
        self.current_balance = new_balance