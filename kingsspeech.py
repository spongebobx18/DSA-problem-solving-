n = int(input())  
for _ in range(n):
    word = input()  
    pronunciation = word[:2] + '... ' + word + '?'
    print(pronunciation)
