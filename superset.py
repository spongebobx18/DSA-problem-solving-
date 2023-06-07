# Enter your code here. Read input from STDIN. Print output to STDOUT
set1 = set(input().split())
for _ in range(int(input())):
    subSet = set(input().split())
    if not(set1.intersection(subSet) == subSet
     and 
    set1.difference(subSet)):
        print("False")
        break
else:
    print("True")