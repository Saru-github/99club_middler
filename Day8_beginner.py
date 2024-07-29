# 99club Day8_beginner - 2024-07-29(Mon)
# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stack = []
    for c in s:
        if c=='(':
            stack.append(c)
        # 스택이 비었거나, stack의 마지막 값이 '(' 이 아니면 실패 리턴
        elif not stack or stack.pop()!='(':
            return False
    return False if stack else True


print(solution(")()("))
