# 99club Day30_middler - 2024-08-20(Tue)
# https://leetcode.com/problems/find-right-interval/

from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        # 각 구간의 시작점과 그 구간의 인덱스를 저장
        start_points = sorted((interval[0], i) for i, interval in enumerate(intervals))

        result = []

        for interval in intervals:
            end_point = interval[1]
            # end_point보다 크거나 같은 시작점을 이진 탐색으로 찾음
            idx = bisect_left(start_points, (end_point,))

            if idx < n:
                result.append(start_points[idx][1])
            else:
                result.append(-1)

        return result
