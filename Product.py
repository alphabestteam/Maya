import random
class Product:
    def __init__(self, product_name: str) -> None:
        self._product_name = product_name
        self._product_price = round(random.uniform(1, 50), 2)
    
    @property
    def product_name(self) -> str:
        return self._product_name
    
    @property
    def product_price(self) -> float:
        return self._product_price
