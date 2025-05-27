from multipledispatch import dispatch

# Method overloading using multipledispatch

@dispatch(int)
def calculate_bill(food_price):
    print(f"Total Bill (Food Only): ${food_price}")

@dispatch(int, int)
def calculate_bill(food_price, drink_price):
    total = food_price + drink_price
    print(f"Total Bill (Food + Drink): ${total}")

@dispatch(int, int, int)
def calculate_bill(food_price, drink_price, dessert_price):
    total = food_price + drink_price + dessert_price
    print(f"Total Bill (Full Order): ${total}")

# Demonstration
calculate_bill(12000)                   # Output: Food Only
calculate_bill(12000, 3000)             # Output: Food + Drink
calculate_bill(12500, 3000, 5000)       # Output: Full Order
