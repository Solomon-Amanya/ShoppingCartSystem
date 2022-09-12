class Store:
    def __init__(self, name):
        self.name = name
        self.stock = []
        self.prices = []

    def add_stock(self, item):
        self.stock.append(item)
        return item.name

    def add_price(self, item):
        self.prices.append(item.price)
        return self.prices

    def print_stock(self):
        for item in self.stock:
            print(item.name)

    def __repr__(self):
        return self.name

