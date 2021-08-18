#뭄ㄴ제7
#초급강의가 650에서 800까지 ㅇ인 학생들이 있는데
#여기서 몇명이 들을 수 있는지 알아봐..

def solution(scores):
    count = 0
    for score in scores:
        if score >=650 and score <800:
            count +=1
    return count

scores = [650,722,914,558,714,803,650,679,669,800]
ret = solution(scores)

print(ret)
