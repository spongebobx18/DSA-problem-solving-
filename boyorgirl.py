username = input()

distinct_chars = set(username)
count = len(distinct_chars)

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
