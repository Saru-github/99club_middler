# 99club Day4_middler - 2024-07-25(Thu)
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    str = ''
    arr = list(s.split(" "))
    for x in arr:
        count = 0
        for j in x:
            if count == 0 and j.isalpha() == True:
                str = j.upper()
            else:
                str = j.lower()
            answer += str
            count += 1
        answer += " "
    answer = answer[:-1]
    return answer


print(solution("3people unFollowed me"))