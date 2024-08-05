# 99club Day15_middler - 2024-08-05(Mon)
# https://leetcode.com/problems/prefix-and-suffix-search/description/


class WordFilter:
    def __init__(self, words):
        self.word_dict = {}

        for index, word in enumerate(words):
            # 모든 접두사와 접미사 조합을 저장
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    prefix = word[:i]
                    suffix = word[j:]
                    self.word_dict[(prefix, suffix)] = index

    def f(self, prefix: str, suffix: str) -> int:
        # (prefix, suffix) 조합으로 해시 맵에서 값을 가져옴
        return self.word_dict.get((prefix, suffix), -1)

# 입력 예제
words = ["apple"]
wf = WordFilter(words)

# 주어진 접두사와 접미사로 검색
result = wf.f("a", "e")
print("검색 결과:", result)  # Expected output: 0