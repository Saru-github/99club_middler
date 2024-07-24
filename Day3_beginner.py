# 99club Day2_beginner - 2024-07-24(Wed)
# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    if s.lower().count("y") == s.lower().count("p"):
        return True
    return False


print(solution("pPoooyY"))