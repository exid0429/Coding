#여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임.
#NXM 형태로 N은 행의 개수 M은 열의 갯수
#1.먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택.
#2.그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
#3.그 중에서 가장 큰 수를 서낵해야함.

#열과 행의 수를 입력
#min함수 이용
n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)


