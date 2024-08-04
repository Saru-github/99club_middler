# 99club Day13_middler - 2024-08-03(Sat)
# https://www.acmicpc.net/problem/10815

from collections import Counter

# 입력 받기
N = int(input())
own_card = list(map(int, input().split()))
M = int(input())
find_card = list(map(int, input().split()))

# 상근이가 가지고 있는 카드의 수를 센다
own_card_counter = Counter(own_card)

# 결과를 출력
result = []
for card in find_card:
    result.append(str(own_card_counter[card]))

print(' '.join(result))
