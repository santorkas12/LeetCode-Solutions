# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #Recursive Solution
        
        if head is None or head.next is None:
            return head
        
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rev
        

        
        
        
        #iterative solution
        
#         prev = None
        
#         while head: #While head is not equal to None
#             current = head #Current pointer on head
#             head = head.next #Change head as the next element
#             current.next = prev #
#             prev = current
#         return prev