# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        left, right =ListNode(), ListNode()
        ltail, rtail= left, right 
        index=1
        while head :
            if index%2==0:
                rtail.next=head 
                rtail=rtail.next
            else:
                ltail.next=head
                ltail=ltail.next
            head=head.next
            index+=1
        

        rtail.next=None
        ltail.next=None
        ltail.next=right.next
        return left.next
