from store import Store
from item import Item
from customer import Customer
from discount_coupon import DiscountCoupon


def calc_total(bought_items):
    total = 0
    for item in bought_items:
        total += item.subsidised_price()
    return total


shoe_coupon = DiscountCoupon("X105", 20)
shocks_coupon = DiscountCoupon("X302", 5)
no_discount = DiscountCoupon("X001", 0)
item1 = Item("shoes", 25000, shoe_coupon)
item2 = Item("socks", 2000, shocks_coupon)
item3 = Item("trouser", 15000, no_discount)

store = Store("KK Traders")

store.stock.append(item1)
store.stock.append(item2)

customer = Customer("Emily", 100000)
customer.shop(item1, store)
customer.shop(item2, store)

total = calc_total(customer.shopping_cart)

change = customer.money - total

print("Dear {}, {} is the total amount of purchased products".format(customer.name, total))
print("Your change is {}".format(change))
print(store.print_remaining_stock())
