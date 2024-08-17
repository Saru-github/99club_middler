# 99club Day27_middler - 2024-08-17(Sat)
# https://school.programmers.co.kr/learn/courses/30/lessons/131127


from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {w:n for w,n in zip(want, number)}

    for i in range(len(discount)):
        if dic == Counter(discount[i:i+10]):
            answer += 1

    return answer
