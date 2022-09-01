from store import Store
from item import Item
from customer import Customer


class ShoppingCartSystem:
    def find_price(self, item, store):
        if store.stock.__contains__(item):
            print(item.price)
        else:
            print("sorry, item will be back soon")
        return item.price


store = Store("Amanya and sons")
item1 = Item("2kg Banana", 800, 0.5)
item2 = Item("1kg Sugar", 3000, 1)
store.add_stock(item2)

shoppingCartSystem = ShoppingCartSystem()

shoppingCartSystem.find_price(item2, store)
