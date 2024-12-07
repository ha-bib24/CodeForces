n = int(input())
i = 0
for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v+ t >= 2:
        i += 1
print(i)