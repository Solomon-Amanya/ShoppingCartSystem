from store import Store
from item import Item
from customer import Customer
Total = 0


class ShoppingCartSystem:
    def find_price(self, item, store):
        if store.stock.__contains__(item):
            return item.price
        else:
            print("sorry, item will be back soon")
            return None

    def apply_discount(self, item):
        discount = item.price * item.discount
        new_price = item.price - discount
        return new_price

    def delete_item(self, item, store):
        if store.stock.__contains__(item):
            store.stock.remove(item)
        else:
            return None

    def total_amount(self, item, store):
        amount_given = input("Money Given:")
        for cost in store.prices:
            total_cost = sum(store.prices)
            balance = int(amount_given) - total_cost
            print("Total cost: " + str(total_cost))
            return balance


store = Store("Amanya and sons")
item1 = Item("2kg Banana", 800, 0.1)
item2 = Item("1kg Sugar", 3000, 1)
item3 = Item("Noodles", 500, 0.2)
store.add_stock(item1)
store.add_stock(item2)
store.add_stock(item3)
store.add_price(item1)
store.add_price(item2)
store.add_price(item3)


shoppingCartSystem = ShoppingCartSystem()

# shoppingCartSystem.find_price(item1, store)

print(shoppingCartSystem.apply_discount(item1))

print(shoppingCartSystem.total_amount(item1, store))

