c = float(input("Enter temperature in Celsius: "))

f = c * 9/5 + 32

print("tempreture:",f)

if c < 0:
    print("Very cold! Wear thick jacket")
elif c <= 15:
    print("Cold. Wear jacket")
elif c <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")

