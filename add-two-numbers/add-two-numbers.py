# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_pointer = l1
        string1 = ""
        
        while l1_pointer:
            string1 = string1 + str(l1_pointer.val)
            
            l1_pointer = l1_pointer.next
            
        l2_pointer = l2
        string2 = ""
        
        while l2_pointer:
            string2 = string2 + str(l2_pointer.val)
            
            l2_pointer = l2_pointer.next
        
        str1_reversed = string1[::-1]
        str2_reversed = string2[::-1]
        
        num1 = int(str1_reversed)
        num2 = int(str2_reversed)
               
        total = num1 + num2       
        
        str_total = str(total)
        
        head = None
        
        while str_total:
            #create node with each str element and convert to int
            #Append node to list
            if head:
                new_node = ListNode(int(str_total[0]))
                new_node.next = head
                head = new_node
                
                str_total = str_total[1:]
        
            else:
                new_node = ListNode(int(str_total[0]))
                head = new_node
                str_total = str_total[1:]
                
        return head