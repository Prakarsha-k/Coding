from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> list[int]:
        graph = defaultdict(list)
        
        def buildGraph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                buildGraph(node.left, node)
                buildGraph(node.right, node)
        
        buildGraph(root, None)
        
        seen = set([target.val])
        queue = deque([(target.val, 0)])
        res = []
        
        while queue:
            node, dist = queue.popleft()
            if dist == K:
                res.append(node)
            elif dist < K:
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, dist + 1))
        return res
