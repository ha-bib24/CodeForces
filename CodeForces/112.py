x = input().strip()
y = input().strip()

x_lower = x.lower()
y_lower = y.lower()

if x_lower < y_lower:
    print(-1)
elif x_lower > y_lower:
    print(1)
else:
    print(0)