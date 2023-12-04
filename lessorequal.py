def kth_largest_distinct():
    n, k = map(int, input().split())
    numbers = sorted(map(int, input().split()))
    
    if k == 0:
        return numbers[0] - 1 if numbers[0] > 1 else -1
    if k > n:
        return -1
    unique_numbers = []
    
    for i in range(k):
        unique_numbers.append(numbers[i])
        numbers[i] = -1
    
    for number in numbers[k:]:
        if number == unique_numbers[-1]:
            return -1
    return unique_numbers[-1]
print(kth_largest_distinct())
