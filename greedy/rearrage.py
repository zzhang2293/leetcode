from typing import List, OrderedDict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        dic = {}
        for i in hand:
            dic[i] = dic.get(i, 0) + 1
        dict_sorted = OrderedDict(sorted(dic.items()))
        for _ in range(len(hand) // groupSize):
            left, right, start = 0, 1, 0
            lst = list(dict_sorted.keys())
            while right < len(lst):
                if lst[left] + 1 == lst[right]:
                    if right - start == groupSize:
                        break
                    left += 1
                    right += 1
                else:
                    start = right
                    left = right
                    right += 1
            if right - start == groupSize:
                for i in range(start, right):
                    dict_sorted[lst[i]] -= 1
                    if dict_sorted[lst[i]] == 0:
                        del dict_sorted[lst[i]]
            else:
                return False
        return True


print(Solution().isNStraightHand([1,2,3,8,5,6,7,8], 4))
