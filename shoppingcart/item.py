class Item:
    def __init__(self, name, price, discount_coupon):
        self.name = name
        self.price = price
        self.discount_coupon = discount_coupon

    def subsidised_price(self):
        discount_amount = (self.discount_coupon.percentage/100) * self.price
        return self.price - discount_amount

    def __repr__(self):
        return self.name
