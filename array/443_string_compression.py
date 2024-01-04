from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0
        while ptr < len(chars):
            cur = chars[ptr]
            count = 1
            while ptr + 1 < len(chars) and chars[ptr + 1] == cur:
                count += 1
                chars.pop(ptr + 1)
            if count != 1:
                count_str = str(count)
                for c in count_str:
                    chars.insert(ptr + 1, c)
                    ptr += 1
            ptr += 1
        return len(chars)


print(Solution().compress(["a", "a", "b"]))
