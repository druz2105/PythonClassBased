import json

from customers import Customers
from products import Product


class Records:
    def __init__(self):
        self.list_customers_data = []
        self.list_products_data = []
        self.customer_index = {}

    def read_customers(self):
        try:
            customers_file = open("customers.json", "r")
            self.list_customers_data = json.load(customers_file)
            for (i, data) in enumerate(self.list_customers_data):
                uni_id = data["uni_id"]
                self.customer_index[uni_id] = i
            return True
        except FileNotFoundError:
            return False

    def read_products(self):
        try:
            products_file = open("products.json", "r")
            self.list_products_data = json.load(products_file)
            return True
        except FileNotFoundError:
            return False

    def find_customer(self, search: str):
        searched_data = []
        for data in self.list_customers_data:
            if search.lower() == data.get("uni_id").lower() or search.lower() == data.get("name").lower():
                searched_data.append(data)
        if len(searched_data) == 0:
            return None
        else:
            return searched_data

    def find_customer_name(self, search: str) -> Customers | None:
        for data in self.list_customers_data:
            if search.lower() == data.get("name").lower():
                return Customers(**data)
        return None

    def find_product(self, search: str):
        searched_data = []
        for data in self.list_products_data:
            if search.lower() == data.get("prod_id").lower() or search.lower() == data.get("name").lower():
                searched_data.append(data)
        if len(searched_data) == 0:
            return None
        else:
            return searched_data

    def find_product_id(self, search: str):
        for data in self.list_products_data:
            if search.lower() == data.get("prod_id").lower():
                return data
        return None

    def list_user_customers_id(self):
        ids = []
        for data in self.list_customers_data:
            ids.append(int(data.get("uni_id")[1::]))
        return ids

    @staticmethod
    def list_customers():
        customers_file = open("customers.json", "r")
        return customers_file.read()

    @staticmethod
    def list_products():
        products_file = open("products.json", "r")
        return products_file.read()

    def create_customer(self, customer: Customers):
        self.list_customers_data.append(customer.get_dict())
        customers_file = open("customers.json", "a")
        json.dump(self.list_customers_data, customers_file)

    def update_customers(self, customer: Customers):
        index = self.customer_index[customer.uni_id]
        customer_dict = customer.get_dict()
        self.list_customers_data[index] = customer_dict
        customers_file = open("customers.json", "w")
        json.dump(self.list_customers_data, customers_file)

    def update_products(self, product: Product):
        index = product.product_id - 1
        product_dict = product.get_dict()
        self.list_products_data[index] = product_dict
        product_file = open("./products.json", "w")
        json.dump(self.list_products_data, product_file)
