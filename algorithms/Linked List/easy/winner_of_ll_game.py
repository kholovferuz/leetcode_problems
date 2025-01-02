# Definition for singly-linked list.
# 3062. Winner of the Linked List Game
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gameResult(self, head: ListNode) -> str:
        odd = 0
        even = 0
        current = head
        while current:
            if current.val > current.next.val:
                even+=1
            if current.val < current.next.val:
                odd +=1
            current = current.next.next
        
        
        if odd > even:
            return "Odd"
        elif odd < even:
            return "Even"
        else:
            return "Tie"
      