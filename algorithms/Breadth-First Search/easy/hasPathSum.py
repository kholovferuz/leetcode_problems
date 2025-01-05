# Definition for a binary tree node.
# Time complexity: O(n)
# Space complexity: O(logn)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            node, sums = stack.pop()
            if not node.left and not node.right and sums==0:
                return True
            if node.right:
                stack.append((node.right, sums - node.right.val))
            if node.left:
                stack.append((node.left, sums - node.left.val))
            
        return False
            