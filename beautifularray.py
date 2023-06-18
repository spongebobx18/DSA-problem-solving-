n = int(input())  # Number of elements in the array
array = list(map(int, input().split())) 
array.sort()
positives = []
zeros = []  
negatives = array[0]
array.pop(0)
zeros = [num for num in array if num == 0]
positives = [num for num in array if num != 0]
neg = [num for num in array if num < 0]
if len(neg) % 2 != 0:
    zeros.append(positives[0])
    positives.pop(0)
print(1, negatives)
print(len(positives), *positives)
print(len(zeros), *zeros)