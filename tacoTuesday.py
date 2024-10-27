prices = [5, 4, 2, 1]

introText = "Welcome to Taco Palace, please view the menu below and enter the number that represents selection"

food = ["Taco", "Burrito", "Nachos", "Soft Drink"]

def menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $5")
    print("2. Burrito - $4")
    print("3. Nachos - $2")
    print("4. Soft Drink - $1")
    print("5. Quit")

def price(food_item):
    return prices[food_item - 1]

def order():
    total = 0.0
    orders = []
    food_item = 0

    print(introText)

    while True:
        menu()  # Show the menu
        choice = int(input("Enter your desired food item (1-5): \n"))

        if 1 <= choice <= 4:
            item = food[choice - 1]
            orders.append(item)
            total += prices[choice - 1]
            print("You selected:", item)

        elif choice == 5:
            break

    print("You ordered", orders)
    print("Your total is $" + str(total))

order()
