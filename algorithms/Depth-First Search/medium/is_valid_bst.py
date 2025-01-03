class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def in_order_traverse(node, prev):
            if not node:
                return True
            
            # we are checking the left subtree
            if not in_order_traverse(node.left, prev):
                return False
            
            # we are checking the current node's value
            if prev[0] is not None and node.val <= prev[0]:
                return False
            
            # updating the previous value
            prev[0] = node.val
            
            # checking the right subtree
            return in_order_traverse(node.right, prev)
        
        # we are using a mutable container (prev) to store the previously visited value
        return in_order_traverse(root, [None])
