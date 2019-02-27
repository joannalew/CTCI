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


def quicksortHelper(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksortHelper(arr, low, pivot - 1)
        quicksortHelper(arr, pivot + 1, high)


def quicksort(arr):
    quicksortHelper(arr, 0, len(arr) - 1)


def main():
    arr = [1, 9, 5, 3, 7, 4, 0, 8, 2]
    quicksort(arr)
    print(arr)

    arr = [7, 5, 3, 7, 9, 5, 2, 1, 6, 3, 2, 7, 2]
    quicksort(arr)
    print(arr)

    arr = [1]
    quicksort(arr)
    print(arr)


if __name__ == "__main__":
    main()
