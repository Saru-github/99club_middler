# 99club Day5_middler - 2024-07-26(Fri)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    # 길이순 정렬
    phone_book.sort()

    # 반복문을 마지막 index 제외하여 돌고, 현재 index 가 다음 index 로 시작하는 지 비교
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        else:
            continue

    return True


print(solution(["119", "97674223", "1195524421"]))
