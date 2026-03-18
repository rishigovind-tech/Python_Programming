items = {
    "Hotdog": 30,
    "Burger": 50,
    "Pizza": 120,
    "Sandwich": 40,
    "Fries": 60
}

for item, price in items.items():
    dash = 20 - len(item) - len(str(price))
    print(item + ("-" * dash) + str(price))