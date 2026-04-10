# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self, head) -> int:
        if not head:
            return 0
        return 1 + self.get_length(head.next)
 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.get_length(head)
        # if removing head, head becomes next 
        if n == size and head:
            head = head.next
            return head
            
        ptr: Optional[ListNode] = head

        prev_ptr: Optional[ListNode] = None
        for _ in range(size - n):
            if not ptr:
                return None
            prev_ptr = ptr
            ptr = ptr.next

        if prev_ptr and ptr:
            prev_ptr.next = ptr.next
        
        return head
