# 99club Day11_beginner - 2024-08-01(Thu)
# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    nList = list(map(int, str(n)))
    newL = sorted(nList, reverse=True)
    strings = [str(i) for i in newL]
    a_string = "".join(strings)
    return int(a_string)


print(solution(118372))