
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=ListNode()
        tmp=head
        res=[]
        for l in lists:
            while l!=None:
                res.append(l.val)
                l=l.next
        print(res)
        sort=sorted(res)
        #converting back to listNode
        for i in sort:
            tmp.next=ListNode()
            tmp=tmp.next
            tmp.val=i
        return head.next
        
      