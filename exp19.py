grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

a = 0
b = 0
c = 0
d = 0

for g in grades:
    if g >= 90:
        a += 1
    elif g >= 80:
        b += 1
    elif g >= 70:
        c += 1
    else:
        d += 1

print(a)
print(b)
print(c)
print(d)
