# 99club Day4_middler - 2024-07-25(Thu)
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    word = ''
    arr = list(s.split(" "))
    for x in arr:
        count = 0
        for j in x:
            if count == 0 and j.isalpha() == True:
                word = j.upper()
            else:
                word = j.lower()
            answer += word
            count += 1
        answer += " "
    answer = answer[:-1]
    return answer

    # words = s.split(" ")
    # answer = [word[0].upper()+word[1:].lower() if word else "" for word in words]
    # return " ".join(answer)


print(solution("3people unFollowed me"))