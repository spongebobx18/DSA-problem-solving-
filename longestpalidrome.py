class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters={}
        for i in s:
            if i not in letters:
                letters[i]=1
            else:
                letters[i]+=1
        res=0
        odd=0
        for i in letters.values():
            if i%2==0:
                res+=i
            else:
                res+=i-1
                odd=True
        if odd:
            res+=1
        return res
                

#from collections import Counter
#you can also solve this alternatively by using the counter from collections rather than initializing the dictionary yourself

"""class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)
        palindrome_length = 0
        odd_count_exists = False

        for count in char_counts.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                odd_count_exists = True

        if odd_count_exists:
            palindrome_length += 1

        return palindrome_length
