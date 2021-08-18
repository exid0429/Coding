#1이 될때까지
#N에서 1을 뺀다.
#N을 K로 나눈다. 둘중에 하나를 선택해서 최소값을 구해라.

#25,5면 25 => 5 => 1로 2 25,3이면 25->24->8->7->6->2->1 로 6

n,k = map(int,input().split())
result = 0

while n>=k:
    if n%k != 0:
        n -= 1
        result +=1
    n=n//k
    result +=1

while n>1:
    n -= 1
    result +=1

print(result)
