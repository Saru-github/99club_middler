# 99club Day12_beginner - 2024-08-02(Fri)
# https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    s = sorted(s, reverse=True)
    return "".join(s)


print(solution("Zbcdefg"))