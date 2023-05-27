def merge_strings(word1, word2):
    merged = ''
    max_len = max(len(word1), len(word2))
    for i in range(max_len):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
    return merged
#this confused me a bit ,took longer than expected

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
merged_string = merge_strings(word1, word2)
print("Merged string:", merged_string)
