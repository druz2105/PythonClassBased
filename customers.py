class Customers:

    def __init__(self,
                 uni_id: str,
                 name: str,
                 value: float = 0,
                 new_entry=False,
                 member=False,
                 discount_rate=0,
                 vip_member=False,
                 **kwargs):
        self.uni_id = uni_id
        self.customer_id = int(uni_id[1:])
        self.Name = name
        self.Value = value
        self.min_discount = discount_rate
        self.member = member
        self.vip_member = vip_member
        self.new_entry = new_entry

    def _get_Id(self):
        return self.uni_id

    def _get_Name(self):
        return self.Name

    def _get_value(self):
        return self.Value

    def get_discount(self, price):
        return 0, price

    def set_Value(self, value: float):
        self.Value = value

    def get_dict(self):
        data = {
            "ID": self.customer_id,
            "uni_id": self.uni_id,
            "name": self.Name,
            "discount_rate": self.min_discount,
            "value": self.Value,
            "member": self.member,
            "vip_member": self.vip_member,
        }
        return data

    def display_info(self):
        print(f"uni_id: {self._get_Id()}")
        print(f"Name: {self._get_Name()}")
        print(f"Value: {self._get_value()}")


class Member:

    def __init__(self, customer: Customers, discount_rate: float = 5.0, **kwargs):
        self.customer = customer
        self.discount_rate = discount_rate
        self.context = kwargs

    def _get_discount_rate(self):
        return self.discount_rate

    def get_discount(self, price: float):
        discount_rate = self.discount_rate / 100
        discount_price = price - (price * discount_rate)
        return discount_rate, discount_price

    def set_rate(self, rate: float):
        self.discount_rate = rate

    def display_info(self):
        print(f"Discount: {self._get_discount_rate()}")


class VIPMember:

    def __init__(self, customer: Customers, min_discount: float = 10.0,
                 threshold: float = 1000):
        self.customer = customer
        self.min_discount = min_discount
        self.max_discount = min_discount + 5
        self.threshold = threshold

    def _get_min_discount_rate(self):
        return self.min_discount

    def _get_max_discount_rate(self):
        return self.max_discount

    def _get_threshold(self):
        return self.threshold

    def get_discount(self, price: float):
        if price >= self.threshold:
            discount_rate = self.max_discount / 100
        else:
            discount_rate = self.min_discount / 100
        discount_price = price - (price * discount_rate)
        return discount_rate, discount_price

    def display_info(self):
        print(self._get_min_discount_rate)
        print(self._get_max_discount_rate)
        print(self._get_threshold)

    def set_rate(self, min_rate, max_rate):
        self.min_discount = min_rate
        self.max_discount = max_rate

    def set_threshold(self, threshold):
        self.threshold = threshold
