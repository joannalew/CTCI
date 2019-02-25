import random

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def main():
    arr = [1, 9, 5, 3, 7, 4, 0, 8, 2]
    quicksort(arr, 0, len(arr))
    print(arr)

    # print(quicksort([7, 5, 3, 7, 9, 5, 2, 1, 6, 3, 2, 7, 2]))
    # print(quicksort([1]))

if __name__ == "__main__":
    main()