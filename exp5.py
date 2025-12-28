a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)

if a > b:
    print(a, "is bigger")
elif b > a:
    print(b, "is bigger")
else:
    print("Both are equal")
