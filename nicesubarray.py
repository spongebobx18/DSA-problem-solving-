left=0
right=0
sub=0
count=0
odd=0
while right<len(num):
    if num[right]%2==1:
        odd+=1
        count=0
    while odd==k:
        count+=1
        if num[left]%2==1:
            odd-=1
        left+=1
    right+=1
    sub+=count
    return sub