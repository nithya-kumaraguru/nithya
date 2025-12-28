price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

discount = discount / 100

final_price = price * (1 - discount)

print(round(final_price, 2))

