def bubblesort(elements):
    size = len(elements)
    for i in range(size - 1, 0, -1):
        swapped = False
        for j in range(i):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return elements

# Example usage:
elements = list(map(int, input().split()))
sorted_elements = bubblesort(elements)
print(sorted_elements)
