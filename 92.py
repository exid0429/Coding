#n,m,k룰 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

#입력받은 수 들 정력하기
data.sort()

first = data[n-1] #제일 큰 수
second = data[n-2] #그다음으로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m ==0:
            break
        result = result + first
        m = m-1
    if m ==0:
        break
    result = result + second
    m = m -1

print(result)

