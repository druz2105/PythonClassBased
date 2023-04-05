from products import Product
from customers import Customers


class Records:
    def __init__(self):
        self.list_customers_data = []
        self.list_products_data = []

    def read_customers(self):
        try:
            customers_file = open("customers.txt", "r")
            customers = customers_file.readlines()
            for line in customers:
                line = line.strip()
                data = line.split(", ")
                unique_id = data[0][0:1]
                if unique_id not in ("C", "M", "V"):
                    continue
                user_data_dict = {
                    "uni_id": data[0],
                    "name": data[1],
                    "discount_rate": float(data[2]),
                    "value": float(data[3]),
                    "member": False,
                    "vip_member": False,
                }
                if unique_id == "M":
                    user_data_dict["member"] = True
                elif unique_id == "V":
                    user_data_dict["vip_member"] = True
                self.list_customers_data.append(user_data_dict)
            return True
        except FileNotFoundError:
            return False

    def read_products(self):
        try:
            products_file = open("products.txt", "r")
            products = products_file.readlines()
            for line in products:
                line = line.strip()
                data = line.split(", ")
                product_data_dict = {
                    "prod_id": data[0],
                    "name": data[1],
                    "price": float(data[2]),
                    "stock": int(data[3])
                }
                self.list_products_data.append(product_data_dict)
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

    def find_customer_name(self, search: str):
        for data in self.list_customers_data:
            if search.lower() == data.get("name").lower():
                return data
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
        customers_file = open("customers.txt", "r")
        return customers_file.read()

    @staticmethod
    def list_products():
        products_file = open("products.txt", "r")
        return products_file.read()

    def write_customer(self, data: str):
        customers_file = open("customers.txt", "a")
        customers_file.write("\n")
        customers_file.write(data)
        self.read_customers()

    @staticmethod
    def update_customers(customer: Customers):
        customers_file = open("customers.txt", "r")
        customers_data = customers_file.readlines()
        for i in range(len(customers_data)):
            line = customers_data[i].strip()
            data = line.split(", ")
            if data[0] == customer.Id:
                if customers_data[i] == customers_data[-1]:
                    customers_data[i] = customer.read_Customers()
                else:
                    customers_data[i] = f"{customer.read_Customers()}\n"

        write_file = open("customers.txt", "w")
        write_file.writelines(customers_data)
        write_file.close()

    @staticmethod
    def update_products(product_id: Product):
        products_file = open("products.txt", "r")
        products_data = products_file.readlines()
        for i in range(len(products_data)):
            line = products_data[i].strip()
            data = line.split(", ")
            if data[0] == product_id.ID:
                if products_data[i] == products_data[-1]:
                    products_data[i] = product_id.read_Products()
                else:
                    products_data[i] = f"{product_id.read_Products()}\n"

        write_file = open("products.txt", "w")
        write_file.writelines(products_data)
        write_file.close()
