class Solution: 
    def select(self, arr, i):
        n = len(arr)
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min_index = self.select(arr, i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
