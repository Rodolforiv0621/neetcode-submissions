# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast = head
        
        while fast and fast.next:
            head = head.next
            fast = fast.next.next

            if fast and head.val == fast.val:
                return True
        
        return False