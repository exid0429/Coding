n,m = map(int,input().split())

#2중 for문으로 해결해보자.

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10000000
    for a in data:
        if a < min_value:
            min_value = a
    result = max(result, min_value)
print(result)
