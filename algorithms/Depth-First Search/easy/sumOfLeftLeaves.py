# Definition for a binary tree node.
# Time complexity: O(n)
# Space complexity: O(n), best case: O(logn)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_sums=0
        
        def traverse(current_node, is_left):
            nonlocal left_sums
            if not current_node:
                return 
            if not current_node.left and not current_node.right and is_left:
                left_sums += current_node.val

            if current_node.left:
                traverse(current_node.left, True)
            if current_node.right:
                traverse(current_node.right, False)
            
        traverse(root, False)
        return left_sums
            
            