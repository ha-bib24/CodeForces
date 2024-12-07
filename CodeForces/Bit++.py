n = int (input())
x = 0
for _ in range(n):
    y = input().strip().lower()
    if "--" in y:
        x -= 1
    elif "++" in y:
        x += 1
print(x)