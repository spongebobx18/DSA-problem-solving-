t = int(input())

test_cases = []  # Store test cases in a list

# Take all inputs
for _ in range(t):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    test_cases.append((a1, b1, a2, b2))

# Process and print the answers
for test_case in test_cases:
    a1, b1, a2, b2 = test_case

    # Check if the rectangles can form a square
    if (a1 == a2 and b1 + b2 == a1) or (a1 == b2 and b1 + a2 == a1) or (b1 == a2 and a1 + b2 == b1) or (b1 == b2 and a1 + a2 == b1):
        print("YES")
    else:
        print("NO")
