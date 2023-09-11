from Product import Product
class Costumer:
    def __init__(self, costumer_name: str) -> None:
        self._costumer_name = costumer_name
        self._groceries_list = []

    @property
    def costumer_name(self):
        return self._costumer_name
    
    @property
    def groceries_list(self):
        return self._groceries_list
    

    def total_price(self) -> float:
        """
        a function that returns the total price of a product for the costumer
        """
        for dict in self.groceries_list:
            total_price = dict["units"] * dict["product"].product_price
        return total_price


    def add_product(self, product_obj: Product, product_units: int) -> None:
        """
        a function that gets a product's info and adds it to the list of dictionaries
        """
        if self.groceries_list == []:
            self.groceries_list.append({"product": product_obj, "units": int(product_units)})
            return None
        for dict in self.groceries_list:
            if product_obj.product_name == dict["product"].product_name:#SEE IF WORKS
                dict["units"] += int(product_units)
                return None
        new_dict = {"product": product_obj, "units": int(product_units)}
        self.groceries_list.append(new_dict)
        print(self.groceries_list)
        

    def remove_product(self, product_name: str, delete_units: int) -> bool:
        """
        a function that gets product's info and deletes what needed to be deleted if it makes sense
        """
        for dict in self.groceries_list:
            if product_name == dict["product"].product_name:
                if dict["units"] > delete_units:
                    dict["units"] -= delete_units
                    print(self.groceries_list)
                    return True
                elif dict["units"] == delete_units:
                    self.groceries_list.remove(dict)
                    print(self.groceries_list)
                    return True
                else:
                    return False
        return False