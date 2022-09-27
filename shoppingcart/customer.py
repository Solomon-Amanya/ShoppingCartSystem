class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.shopping_cart = []

    def shop(self, item, store):
        if item in store.stock:
            self.shopping_cart.append(item)
            store.stock.remove(item)
        else:
            print("sorry item will be back soon")
            return None,

    def __repr__(self):
        return self.name






