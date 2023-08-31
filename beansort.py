class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beanlen=len(beans)
        beans.sort()
        totalSum=sum(beans)
        minn=float('inf')
        for i , bean in enumerate(beans):
            minn=min(minn, totalSum-(beanlen-i)*bean)
        return minn

        
        
        
            
        