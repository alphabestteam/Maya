from Costumer import Costumer
class Register:
    def __init__(self) -> None:
        self._profit_sum = 0
        self._total_sales = []

    @property
    def profit_sum(self):
        return self._profit_sum
    
    @property
    def total_sales(self):
        return self._total_sales
    

    def checkout_costumer(self, costumer_obj: Costumer) -> None:
        """
        a function that adds the costumer's payment to the profit of the cash register and the 
        costumer's name and payment to total_sales list
        """
        self.profit_sum += costumer_obj.total_price
        self.total_sales.append({"name": costumer_obj.costumer_name, "total price": costumer_obj.total_price})

    def print_summary(self) -> str:
        """
        a function that prints the profit of the cash register and the total sales list for the day
        """
        return f"Today's cash register's profit is: {self.profit_sum}\n\
            Today's total sales list is: {self.total_sales}"