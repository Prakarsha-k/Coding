from typing import List

class Solution:
    def insertIntoMaxTree(self, root: 'TreeNode', val: int) -> 'TreeNode':
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
