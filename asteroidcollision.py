

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # n=len(asteroids)
        # for i in range(n-1):
        #     if asteroids[i]==abs(asteroids[i+1]):
        #         return 
        #     if asteroids[i+1]<0 and asteroids[i]>abs(asteroids[i+1]):
        #         asteroids.pop()
        # return asteroids
       
        stack = []
    
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
               
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        
        return stack
