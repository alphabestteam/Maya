from Product import Product
class Costumer:
    def __init__(self, costumer_name: str) -> None:
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
    

    def add_product(self, product_obj: Product) -> list:
        """
        a function that gets a product's info and adds it to the list of dictionaries
        """
        if self.groceries_list == []:
            self.groceries_list.append({"name": product_obj.product_name,  "units": int(product_obj.product_units)})
            self._total_price += product_obj.total_product_price
            return self.groceries_list
        for dict in self.groceries_list:
            if product_obj.product_name in dict.values():
                dict["units"] += int(product_obj.product_units)
            else:
                new_dict = {"name": product_obj.product_name,  "units": int(product_obj.product_units)}
                self.groceries_list.append(new_dict)
            self._total_price += product_obj.total_product_price #SEE IF CORRECT
            return self.groceries_list
        
        
    def remove_product(self, product_obj: Product, delete_units: int) -> int:
        """
        a function that gets product's info and deletes what needed to be deleted if it makes sense
        """
        reduction = 0
        for dict in self.groceries_list:
            if product_obj.product_name not in dict:
                raise ValueError('invalid name')
            elif dict[product_obj.product_name]["units"] > delete_units:
                dict[product_obj.product_name]["units"] -= delete_units
                reduction = dict[product_obj.product_name]["price"] * delete_units
                return reduction
            elif dict[product_obj.product_name]["units"] == delete_units:
                reduction = dict[product_obj.product_name]["price"] * delete_units
                self.groceries_list.remove(dict)
                return reduction
            else:
                raise ValueError('invalid input')
        return reduction