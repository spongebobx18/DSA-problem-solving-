# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummy = curr = ListNode()
            while head1 and head2:
                if head1.val <= head2.val:
                    curr.next = head1 
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            
            if head1:
                curr.next = head1
            else:
                curr.next = head2
            return dummy.next


        def sort(head):
            if not head.next:
                return head
                
            fast = slow = head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None 
            return merge(sort(head), sort(slow))
        if head:
            return sort(head)