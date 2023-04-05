class Customers:

    def __init__(self, uni_id: str, name: str, value: float = 0):
        self.Id = uni_id
        self.Name = name
        self.Value = value
        self.min_discount = 0

    def _get_Id(self):
        return self.Id

    def _get_Name(self):
        return self.Name

    def _get_value(self):
        return self.Value

    def get_discount(self, price):
        return 0, price

    def set_Value(self, value: float):
        self.Value = value

    def read_Customers(self):
        return f"{self.Id}, {self.Name}, {self.min_discount}, {self.Value}"

    def display_info(self):
        print(f"Id: {self._get_Id()}")
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
