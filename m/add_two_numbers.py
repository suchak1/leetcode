# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mult = 1
        n1 = 0
        
        while l1:
            n1 += mult * l1.val
            mult *= 10
            l1 = l1.next
        
        mult = 1
        n2 = 0
        
        while l2:
            n2 += mult * l2.val
            mult *= 10
            l2 = l2.next
            
        n3 = n1 + n2    
        l3 = ListNode(0)
        temp = l3
        
        while n3 > 0:
            temp.val = n3 % 10
            
            if n3 // 10 == 0:
                break
            else:
                n3 //= 10
                temp.next = ListNode(0)
                temp = temp.next
                
        return l3
    
        #80ms, 97.05%
