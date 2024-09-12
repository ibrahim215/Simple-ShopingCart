menu = {
    "pizza" : 3.00,
    "soda" : 10.00,
    "tomato" : 8.00,
    "chips" : 4.99,
    "coca" : 13.80,
    "potato" : 2.99
}

cart = []
total = 0

print("------ MENU ------")
for key,value in menu.items():
    print(f"{key:10} = ${value}")
print("------------------")

while True:
    food = input("Select an item (r to quit): ").lower()
    if food == "r":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER IS ------")
for food in cart:
    total+=menu.get(food)
    print(food, end=" ")

print()
print(f"Total is : ${total:.2f}")