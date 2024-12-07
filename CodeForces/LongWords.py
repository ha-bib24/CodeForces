n = int(input())
for i in range(0,n):
    m = str(input())
    q = len(m)
    if q > 10:
        print(m[0], end="")
        print(q - 2, end="")
        print(m[-1])
    else:
        print(m)

#...................Using While Loop.............
n = int(input())
i = 0
while i < n:
    x = str(input())
    y = len(x)
    if y > 10:
        print(x[0], end="")
        print(y - 2, end="")
        print(x[-1], end="")
    else:
        print(x)
    i += 1