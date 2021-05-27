# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        firstnode = head
        secondnode = head.next
            
        firstnode.next = self.swapPairs(secondnode.next)
        secondnode.next = firstnode
            
        
        return secondnode        