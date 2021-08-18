#문제6
#3,6,9 1부터 number까지 몇번의 박수를 폈는지..

def solution(number):
    count = 0

    for i in range(1,number+1):
        current = i
        while current !=0:
            if current % 10 ==3 or current % 10 == 6 or current % 10 ==9:
                count +=1
            current = current // 10
    return count

number = int(input())
ret = solution(number)

print("solution 함수의 반환 값은",ret,"입니다.")


"""
-3,6,9로 끝나는 경우만 박수를 친다?
for i in range(1,number+1):
    if i % 10 ==3 or i % 10 == 6 or i % 10 == 9:
        print(i)
        count +=1

-10의 자리에 3,6,9가 들어가면 박수를 친다?
for i in range(1,number+1):
    current = i
    while current != 0:
        if current % 10 ==3 or current %10 ==6 or current % 10 ==9:
            count +=1
        current = current // 10


"""


