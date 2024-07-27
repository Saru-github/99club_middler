# 99club Day6_middler - 2024-07-27(Sat)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    # 곱할 것 이므로, 1
    answer = 1
    # 딕셔너리 생성
    style_dic = {}
    for x in clothes:
        # 의상 종류별로 갯수 저장
        style_dic[x[1]] = style_dic.get(x[1], 0) + 1

    for i in style_dic.values():
        answer += i * answer
    # 아무것도 안입은 것
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
