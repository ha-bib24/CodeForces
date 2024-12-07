n, k = map(int, input().split())
scores = list(map(int, input().split()))
threshold = scores[k - 1]
print(sum(1 for score in scores if score > 0 and score >= threshold))




#.....................................................


n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k - 1]
count = 0
for score in scores:
    if score > 0 and score >= threshold:
        count += 1
print(count)
