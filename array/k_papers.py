from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        lst = [0]
        for i in citations:
            lst.append(lst[-1] + 1)
        res = 0
        for i in range(1, len(lst)):
            if citations[i - 1] <= lst[i]:
                res = max(res, citations[i - 1])

        return res


print(Solution().hIndex([3, 0, 6, 1, 5]))