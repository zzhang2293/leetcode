from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # prepare
        adj = {}
        for word in words:
            for c in word:
                if c not in adj: adj[c] = []
        first, second = 0, 1
        while second < len(words):
            ptr = 0
            while ptr < len(words[first]) and ptr < len(words[second]) and words[first][ptr] == words[second][ptr]:
                ptr += 1
            if ptr < len(words[first]) and ptr < len(words[second]) and words[first][ptr] != words[second][ptr] and words[second][ptr] not in adj[words[first][ptr]]:
                adj[words[first][ptr]].append(words[second][ptr])
            elif len(words[first]) > ptr >= len(words[second]) and words[first][ptr - 1] == words[second][ptr - 1]:
                return ""

            first += 1
            second += 1

        visited, cur_visited, res, node_lst = set(), set(), [], list(adj.keys())

        def dfs(cur: str):
            if cur in cur_visited: return False
            if cur in visited: return True
            visited.add(cur)
            cur_visited.add(cur)
            while adj[cur]:
                if not dfs(adj[cur].pop(0)): return False
            cur_visited.remove(cur)
            res.insert(0, cur)
            node_lst.remove(cur)
            return True

        while node_lst:
            if not dfs(node_lst[0]): return ""
            cur_visited.clear()
        return "".join(res)



print(Solution().alienOrder(["abc", "ab"]))
