prices = {
    "bananas": 10,
    "apples": 8,
    "bread": 7,
    "cheese": 20,
    "juice": 15
}

cart_shopping = {
    "bananas": 2,
    "bread": 3,
    "cheese": 1
}

total = 0

for product , value in cart_shopping.items():
    total += prices[product] * value
print(total)

cart_shopping["mlk"] = 2

total = 0

for product, value in cart_shopping.items():
    if product in prices:
        total += prices[product] * value
    else:
        print(f"{product} not found in prices")

print("Total:", total)