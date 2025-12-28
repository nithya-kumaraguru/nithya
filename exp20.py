items = []

while True:
    choice = input("Enter add / remove / show / quit: ").lower()

    if choice == "add":
        item = input("Enter item: ")
        items.append(item)

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item)
        else:
            print("Item not found")

    elif choice == "show":
        if item in item in items:
             print(items)
        else:
            print("item not found")

    elif choice == "quit":
        break

   
