class Solution:
    def simplifyPath(self, path: str) -> str:
        self.stack=[]
        for i in path.split('/'):
            if i=='..':
                if self.stack:
                    self.stack.pop()
            elif i not in ('','.'):
                self.stack.append(i)
        return "/"+"/".join(self.stack)
            

        
        
        
        