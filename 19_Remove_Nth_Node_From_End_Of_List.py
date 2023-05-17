# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        tmp_head = head
        while tmp_head:
            length+=1
            tmp_head = tmp_head.next

        length2 = length
        length -= n

        if length == 0:
            if length2 > 0:
                return head.next
            else:
                return None
        
        ans = head
        for i in range(length-1):
            ans = ans.next

        if n == 1:
            ans.next = None
            return head

        ans.next = ans.next.next
        return head
