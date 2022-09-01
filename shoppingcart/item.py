class Item:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __repr__(self):
        return self.name
