class Costumer:
    def __init__(self, costumer_name: str, groceries_list: list, total_price: float) -> None:
        self._costumer_name = costumer_name
        self._groceries_list = groceries_list
        self._total_price = total_price

    @property
    def costumer_name(self):
        return self._costumer_name
    
    @property
    def groceries_list(self):
        return self._groceries_list
    
    @property
    def total_price(self):
        return self._total_price
    