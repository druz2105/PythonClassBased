from typing import Tuple, Union

from customers import Customers, Member, VIPMember
from products import Product
from orders import Order
from records import Records
from random import randint

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

    def customer_get_or_create(self) -> Tuple[Customers, Union[Member, VIPMember], bool]:
        name = str(input("Enter your first name:"))
        created = False
        discount_rate = 0
        member_price = 800
        vip_member_price = 1000
        uniq_id = self._get_random_id()
        member = None
        customer_data = records.find_customer_name(name)
        if not customer_data:
            created = True
            membership = str(input("Do you wish to be member(Y/N):"))
            if membership == "Y" or membership == "y":
                print("NOTE: VIP Members will have to pay $200 more for than regular members")
                membership_type = str(
                    input("Chose membership type for VIP Membership choose (V) otherwise choose (M):"))
                uniq_id = self._get_random_id(membership_type)
                if membership_type == "V" or membership_type == "v":
                    customer = Customers(uni_id=uniq_id, name=name, value=vip_member_price)
                    member = VIPMember(customer=customer)
                    discount_rate = member.min_discount
                else:
                    customer = Customers(uni_id=uniq_id, name=name, value=member_price)
                    member = Member(customer=customer)
                    discount_rate = member.discount_rate
            else:
                customer = Customers(uni_id=uniq_id, name=name)
            user_data = f"{customer.Id}, {customer.Name}, {discount_rate}, {customer.Value}"
            records.write_customer(user_data)
        else:
            member = customer_data.pop("member")
            vip_member = customer_data.pop("vip_member")
            discount_rate = customer_data.pop("discount_rate")
            customer = Customers(**customer_data)
            if member:
                member = Member(customer=customer, discount_rate=float(discount_rate))
            if vip_member:
                member = VIPMember(customer=customer, min_discount=float(discount_rate))
        customer.min_discount = discount_rate
        return customer, member, created

    @staticmethod
    def product_get():
        query = str(input("Enter product id you want to purchase:"))
        product = records.find_product_id(query)
        if not product:
            print("Incorrect product id enter valid id again")
            quit()
        else:
            product = Product(**product)
        return product

    def purchase_product(self, customer: Customers, product: Product) -> Order:
        quantity = int(input("Enter quantity of the product you want to purchase.:"))
        if product.Stock >= quantity:
            product_quantity = product.Stock - quantity
            order = Order(customer=customer, product=product, quantity=quantity)
            product.set_Stock(product_quantity)
            records.update_products(product)
            customer.set_Value(customer.Value + (product.Price * order.Quantity))
            records.update_customers(customer)
            return order
        else:
            raise ValueError("Stock is not available")

    def purchase_product_member(self, member: Union[Member, VIPMember], product: Product) -> Order:
        quantity = int(input("Enter quantity of the product you want to purchase.:"))
        if product.Stock >= quantity:
            customer = member.customer
            product_quantity = product.Stock - quantity
            total_price = product.Price * quantity
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
        print(f"{order.Customer.Name}  |     purchases      | {order.Quantity} x {order.Product.Name}")
        print(f"Unit price:            |                    | {order.Product.Price} (AUD)")
        print(f"{order.Customer.Name}  | gets a discount of | {order.Discounted_Rate}%")
        print(f"Total price:           |                    | {order.Total}(AUD)")

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
        TOTAL = order.Total + membership_price
        print(f"{order.Customer.Name}  |     purchases      | {order.Quantity} x {order.Product.Name}")
        print(f"Unit price:            |                    | {order.Product.Price} (AUD)")
        print(f"Membership price:      |                    | {membership_price}(AUD)")
        print(f"{order.Customer.Name}  | gets a discount of | {order.Discounted_Rate}%")
        print(f"Total price:           |                    | {TOTAL}(AUD)")
