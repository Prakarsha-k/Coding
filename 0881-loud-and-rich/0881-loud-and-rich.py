from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        
        res = [-1] * n
        
        def dfs(u):
            if res[u] != -1:
                return res[u]
            res[u] = u
            for v in graph[u]:
                cand = dfs(v)
                if quiet[cand] < quiet[res[u]]:
                    res[u] = cand
            return res[u]
        
        for i in range(n):
            dfs(i)
        return res
