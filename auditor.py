inventory = 0

while True:
    stockQuantity = input("Enter a stock quantity: ")
    if not stockQuantity.isdigit() or int(stockQuantity) < 0:
        if stockQuantity.lower().strip() == "quit":
            break
        print("Invalid input, please try again!")
        continue
    inventory += int(stockQuantity)
    if inventory > 500:
        print("Inventory has exceeded 500 units")
        break