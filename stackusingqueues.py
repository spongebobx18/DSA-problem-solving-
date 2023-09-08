class Node:
    def __init__(self,val=0,next=None ):
        self.val=val
        self.next=next
class MyStack:
    def __init__(self):
        self.head=Node()
    def push(self, x:int) -> None:
            newnode = Node(val=x)
            newnode.next=self.head
            self.head=newnode
            
    def pop(self) -> int:
        if self.head:

            val=self.head.val
            self.head=self.head.next
            return val
        else:
            return 
    
    def top(self) -> int:
        if not self.head:
            return 
        else:
            return self.head.val
    def empty(self) -> bool:
        return self.head.next==None
        

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()