class Product:
    def __init__(self, product_name: str, product_price: float, product_units: int) -> None:
        self._product_name = product_name
        self._product_price = product_price
        self._product_units = product_units
        self._total_product_price = self.product_price * self.product_units
    
    @property
    def product_name(self):
        return self._product_name
    
    @property
    def product_price(self):
        return self._product_price
    
    @property
    def product_units(self):
        return self._product_units
    
    @property
    def total_product_price(self):
        return self._total_product_price
    