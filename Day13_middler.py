# 99club Day13_middler - 2024-08-03(Sat)
# https://www.acmicpc.net/problem/10815

N = int(input())
own_card = list(map(int, input().split()))
M = int(input())
find_card = list(map(int, input().split()))

dic = {}

for find_num in find_card:
    dic[find_num] = 0

for own_num in own_card:
    if own_num in dic:
        dic[own_num] = 1

for d in dic:
    print(dic[d], end=' ')