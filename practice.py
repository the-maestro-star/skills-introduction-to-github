def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
data = [64, 34, 25, 99, 22, 11, 90]
sorted_data = bubble_sort(data)
print("Sorted array:", sorted_data)