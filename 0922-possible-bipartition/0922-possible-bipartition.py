from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, N: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        
        for node in range(1, N + 1):
            if node not in color:
                queue = deque([node])
                color[node] = 0
                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        if nei in color:
                            if color[nei] == color[curr]:
                                return False
                        else:
                            color[nei] = 1 - color[curr]
                            queue.append(nei)
        return True
