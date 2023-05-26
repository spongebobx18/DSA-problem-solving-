class Solution(object):
    def smallestEvenMultiple(n):
        if n % 2==0:
           return n
        else :
           return 2*n
    n=int(input("Enter number: "))
    result = smallestEvenMultiple(n)
    print(result)
          