from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with characters from the first word
        common = Counter(words[0])
        # Iterate through the remaining words
        for word in words[1:]:
            # Update the counter by taking the intersection of characters
            common &= Counter(word)
        return list(common.elements())