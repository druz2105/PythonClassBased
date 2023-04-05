from customers import Customers, Member, VIPMember
from products import Product


class Order:
    def __init__(self, customer: Customers, product: Product, quantity: int, total: float = 0, discount_rate: float = 0):
        self.Customer = customer
        self.Product = product
        self.Quantity = quantity
        self.Total = total
        self.Discounted_Rate = discount_rate * 100

    def _get_Customer(self):
        return self.Customer

    def _get_Product(self):
        return self.Product

    def _get_Quantity(self):
        return self.Quantity

    def _get_Total(self):
        return self.Total

    def _get_Discounted_Rate(self):
        return self.Discounted_Rate

    def set_discount_rate_member(self, discount_rate: float):
        member = Member(customer=self.Customer, discount_rate=discount_rate)

    def set_discount_rate_vip_member(self, min_rate: float):
        vip_member = VIPMember(self.Customer, min_discount=min_rate)

    def set_product_stock(self, stock):
        self.Product.set_Stock(stock)

    def display_info(self):
        print(self._get_Customer())
        print(self._get_Product())
        print(self._get_Quantity())
        print(self._get_Total())
        print(self._get_Discounted_Price())
