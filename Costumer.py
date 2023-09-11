class Costumer:
    def __init__(self, costumer_name: str, groceries_list: list, total_price: float) -> None:
        self._costumer_name = costumer_name
        self._groceries_list = []
        self._total_price = 0

    @property
    def costumer_name(self):
        return self._costumer_name
    
    @property
    def groceries_list(self):
        return self._groceries_list
    
    @property
    def total_price(self):
        return self._total_price
    

    def add_product(self, product_name: str, product_units: int) -> list:
        """
        a function that gets a product's info and adds it to the list of dictionaries
        """
        if self.groceries_list == []:
            self.groceries_list.append({"name": product_name,  "units": int(product_units)})
            return self.groceries_list
        for dict in self.groceries_list:
            if product_name in dict.values():
                dict["units"] += int(product_units)
            else:
                new_dict = {"name": product_name,  "units": int(product_units)}
                self.groceries_list.append(new_dict)
            return self.groceries_list