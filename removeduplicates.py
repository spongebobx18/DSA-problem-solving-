# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)#introduce a dummy node to check for edge cases
        dummy.next=head
        prev=dummy
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:#duplicates
                while cur and  cur.next and cur.val==cur.next.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return dummy.next

       
           

        