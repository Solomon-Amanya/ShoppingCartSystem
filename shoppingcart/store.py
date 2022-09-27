class Store:
    def __init__(self, name):
        self.name = name
        self.stock = []

    def print_remaining_stock(self):
        return self.stock

    def __repr__(self):
        return self.name
