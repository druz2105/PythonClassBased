class Product:

    def __init__(self, prod_id: str, name: str, price: float, stock: int):
        self.ID = prod_id
        self.product_id = int(prod_id[1:])
        self.Name = name
        self.Price = price
        self.Stock = stock

    def _get_Id(self):
        return self.ID

    def _get_Name(self):
        return self.Name

    def _get_Price(self):
        return self.Price

    def _get_Stock(self):
        return self.Stock

    def set_Price(self, price):
        self.Price = price

    def set_Stock(self, stock):
        self.Stock = stock

    def get_dict(self):
        data = {
            "prod_id": self.ID,
            "name": self.Name,
            "price": self.Price,
            "stock": self.Stock
        }
        return data

    def display_info(self):
        print(f"ID: {self._get_Id()}")
        print(f"Name: {self._get_Name()}")
        print(f"Price: {self._get_Price()}")
        print(f"Stock: {self._get_Stock()}")
