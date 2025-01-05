# Definition for a binary tree node.
# time complexity: O(n)
# space complexity: O(w). w - width of a tree. In the wors case O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        depth = 0

        while queue:
            depth+=1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth