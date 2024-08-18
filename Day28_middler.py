# 99club Day28_middler - 2024-08-18(Sun)
# https://school.programmers.co.kr/learn/courses/30/lessons/76502


def solution(s):
    answer = 0
    s_lst = list(s)
    for _ in range(len(s)):
        temp_s = s
        while temp_s.find('()') != -1 or temp_s.find('[]') != -1 or temp_s.find('{}') != -1:
            temp_s = temp_s.replace('()','').replace('[]','').replace('{}','')
        if len(temp_s) == 0:
            answer += 1
        s = s[1:] + s[0]
    return answer
