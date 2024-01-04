from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        record = {}
        for i in range(len(s)):
            if s[i] not in record:
                record[s[i]] = []
        for i in range(len(s)):
            record[s[i]].append(i)
        res = []
        for key, val in record.items():
            res.append([val[0], val[-1]])
        res.sort()
        res_val = []
        for left, right in res:
            if not res_val or res_val[-1][-1] < left:
                res_val.append([left, right])
            elif res_val[-1][-1] > left:
                res_val[-1][-1] = max(res_val[-1][-1], right)
        ls = []
        for left, right in res_val:
            ls.append(right - left + 1)
        return ls


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
