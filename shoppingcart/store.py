class Store:
    def __init__(self, name):
        self.name = name
        self.stock = []

    def add_stock(self, item):
        self.stock.append(item)
        return item.name

    def print_stock(self):
        for item in self.stock:
            print(item.name)

    def __repr__(self):
        return self.name

