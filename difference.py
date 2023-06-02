
n_english = int(input())
english_roll_numbers = set(map(int,input().split()))
n_french = int(input())
french_roll_numbers = set(map(int,input().split()))


english_only = english_roll_numbers.difference(french_roll_numbers)
tenglish_only = len(english_only)


print(tenglish_only)
