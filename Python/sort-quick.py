import random

def quicksort(arr):
    if len(arr) > 1:
        pivot = random.randint(0, len(arr))
        arr[0], arr[pivot] = arr[pivot], arr[0]
        pivot = arr[0]

        left = [el for el in arr if el < pivot]
        middle = [el for el in arr if el == pivot]
        right = [el for el in arr if el > pivot]

        quicksort(left) + middle + quicksort(right)
    else:
        return arr

def main():
    print(quicksort([1, 9, 5, 3, 7, 4, 0, 8, 2]))
    print(quicksort([7, 5, 3, 7, 9, 5, 2, 1, 6, 3, 2, 7, 2]))
    print(quicksort([1]))

if __name__ == "__main__":
    main()