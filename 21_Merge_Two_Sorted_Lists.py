# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = ListNode()
        
        if list1.val<=list2.val:
            head=list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        head2 = ListNode()
        head2 = head
        while True:
            if list2 == None:
                head.next = list1
                break
            if list1 == None:
                head.next = list2
                break
            
            if list1.val <= list2.val:
               # ListNode tmp = list1.next
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        return head2
                
        
        

