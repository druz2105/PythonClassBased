from random import randint
from typing import Tuple, Union

from customers import Customers, Member, VIPMember
from orders import Order
from products import Product
from records import Records

records = Records()


class Main:

    def __init__(self):
        self.list_user_customers_id = None
        self.list_products = None
        self.list_customers = None

    def records_read(self):
        self.list_customers = records.read_customers()
        self.list_products = records.read_products()
        self.list_user_customers_id = records.list_user_customers_id()
        if not self.list_customers:
            print("Error in reading customers File")
            quit()

        elif not self.list_products:
            print("Error in reading products File")
            quit()

    def _get_random_id(self, member_type: str = "C"):
        random_num = randint(0, 100)
        if random_num in self.list_user_customers_id:
            return self._get_random_id(member_type)
        return f"{member_type.upper()}{random_num}"

    def create_member(self, name):
        member_price = 800
        vip_member_price = 1000

        membership_type = str(
            input("Chose membership type for VIP Membership choose (V) otherwise choose (M):"))
        uniq_id = self._get_random_id(membership_type)
        if membership_type.upper() == "V":
            customer = Customers(uni_id=uniq_id, name=name, value=vip_member_price)
            member = VIPMember(customer=customer)
            discount_rate = member.min_discount
        elif membership_type.upper() == "M":
            customer = Customers(uni_id=uniq_id, name=name, value=member_price)
            member = Member(customer=customer)
            discount_rate = member.discount_rate
        else:
            print("Invalid input choose correct option")
            return self.create_member(name)
        return customer

    def customer_get_or_create(self) -> Tuple[Customers, Union[Member, VIPMember]]:
        name = str(input("Enter your first name:"))
        discount_rate = 0
        uniq_id = self._get_random_id()
        member = None
        customer_data = records.find_customer_name(name)
        if not customer_data:
            membership = str(input("Do you wish to be member(Y/N):"))
            if membership.upper() == "Y":
                print("NOTE: VIP Members will have to pay $200 more for than regular members")
                customer = self.create_member(name)
            else:
                customer = Customers(uni_id=uniq_id, name=name)
            customer.new_entry = True
            records.create_customer(customer)
        else:
            member = customer_data.member
            vip_member = customer_data.vip_member
            discount_rate = customer_data.min_discount
            if vip_member:
                member = VIPMember(customer=customer_data, min_discount=float(discount_rate))
            if member:
                member = Member(customer=customer_data, discount_rate=float(discount_rate))
        customer_data.min_discount = discount_rate
        return customer_data, member

    @staticmethod
    def list_all_product():
        print(f"{'ID':^4} | {'Product Name':^40} | {'Product Price':^20} | {'Quantity':^20} |")
        print('_' * 95)
        for i in records.list_products_data:
            product = Product(**i)
            print(f"{product.ID:^4} | {product.Name:^40} | {product.Price:^20} | {product.Stock:^20} |")

    def product_get(self):
        self.list_all_product()
        query = str(input("Enter product id you want to purchase:"))
        product = records.find_product_id(query)
        if not product:
            print("Incorrect product id enter valid id again")
            quit()
        else:
            product = Product(**product)
        return product

    @staticmethod
    def purchase_product(customer: Customers, product: Product) -> Order:
        quantity = int(input("Enter quantity of the product you want to purchase.:"))
        if product.Stock >= quantity:
            product_quantity = product.Stock - quantity
            total_price = product.Price * quantity
            order = Order(customer=customer, product=product, quantity=quantity, total=total_price)
            product.set_Stock(product_quantity)
            records.update_products(product)
            customer.set_Value(customer.Value + (product.Price * order.Quantity))
            records.update_customers(customer)
            return order
        else:
            raise ValueError("Stock is not available")

    @staticmethod
    def purchase_product_member(member: Union[Member, VIPMember], product: Product) -> Order:
        quantity = int(input("Enter quantity of the product you want to purchase.:"))
        if product.Stock >= quantity:
            customer = member.customer
            product_quantity = product.Stock - quantity
            total_price = product.Price * quantity
            print(total_price)
            discount_rate, discounted_price = member.get_discount(total_price)
            order = Order(customer=customer, product=product, quantity=quantity, total=discounted_price,
                          discount_rate=discount_rate)
            product.set_Stock(product_quantity)
            records.update_products(product)
            customer.set_Value(customer.Value + discounted_price)
            records.update_customers(customer)
            return order
        else:
            raise ValueError("Stock is not available")

    @staticmethod
    def print_existing_customer_receipt(order: Order):

        """
        <customer name > purchases <quantity> x <product>.
        Unit price: <the price of the product> (AUD)
        <customer name> gets a discount of <discount percentage>%.
        Total price: <the total price> (AUD)
        :return:
        """

        print(f"{'Receipt': ^75}")
        print("=" * 75)
        print(f"{order.Customer.Name:<20} | {'purchases':<20} | {order.Quantity:<5} x {order.Product.Name:<30}")
        print(f"{'Unit price:':<20} | {' ':<20} | {order.Product.Price:<5} {'(AUD)':<5}")
        print(f"{order.Customer.Name:<20} | {'gets a discount of':<20} | {str(order.Discounted_Rate) + '%':<5}{'':<5}")
        print(f"{'Total price:':<20} | {' ':<20} | {order.Total:<5} {'(AUD)':<5}")

    @staticmethod
    def print_new_customer_receipt(order: Order, membership_price: float):

        """
        <customer name > purchases <quantity> x <product>.
        Unit price: <the price of the product> (AUD)
        Membership price: <the price of VIP membership> (AUD)
        <customer name> gets a discount of <discount percentage>%.
        Total price: <the total price> (AUD)

        :return:
        """
        print(f"{'Receipt': ^65}")
        print("=" * 65)
        print(f"{order.Customer.Name:<20} | {'purchases':^20} | {order.Quantity:<5} x {order.Product.Name:<30}")
        print(f"{'Unit price:':<20} | {' ':^20} | {order.Product.Price:<5} {'(AUD)':<5}")
        print(f"{'Membership price:':<20} | {' ':^20} | {membership_price:<5} {'(AUD)':<5}")
        print(f"{order.Customer.Name:<20} | {'gets a discount of':^20} | {str(order.Discounted_Rate) + '%':<5}{'':<5}")
        print(f"{'Total price:':<20} | {' ':^20} | {order.Total:<5} {'(AUD)':<5}")
