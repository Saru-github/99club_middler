# 99club Day20_middler - 2024-08-10(Sat)
# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(number, k):
    answer = ''

    num_list = [int(x) for x in list(number)]  # 숫자를 한개씩 나눠 리스트로 저장
    box = []  # 숫자를 담을 리스트

    num_length = len(number) - k  # 문제에서 요구하는 리스트 크기

    for i in range(len(number)):
        while k > 0 and box and box[-1] < num_list[i]:  # k > 0, 리스트 안 비어있고, 새로운 값이 크면 pop진행
            box.pop()
            k -= 1

        if k == 0:
            box += num_list[i:]  # 뒤에 남은 숫자들 붙여줌
            break  # k가 0이면 더이상 이 과정을 진행할 수 없으니까 break

        box.append(num_list[i])  # 숫자 추가

    if len(box) > num_length:  # 숫자를 담은 리스트가 정답길이보다 길면 슬라이싱
        box = box[:num_length]

    answer = ''.join(map(str, box))  # 리스트들 join함수로 합쳐줌

    return answer
