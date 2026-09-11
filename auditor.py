inventory = 0
rejected_ent = 0

while True:
    stockQuantity = input("Enter a stock quantity: ")
    if not stockQuantity.isdigit() or int(stockQuantity) < 0:
        if stockQuantity.lower().strip() == "quit":
            print(f"Total Units Processed: {inventory}\nNumber of Failed/Rejected Entries: {rejected_ent}")
            break
        rejected_ent += 1
        print("Invalid input, please try again!")
        continue
    inventory += int(stockQuantity)
    if inventory > 500:
        print("Inventory has exceeded 500 units")
        break