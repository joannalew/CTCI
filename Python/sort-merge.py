def merge(left, right):
    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        
    return res + left[i:] + right[j:]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]
        
        sortedLeft = mergeSort(left)
        sortedRight = mergeSort(right)

        return merge(sortedLeft, sortedRight)

    else:
        return arr

def main():
    print(mergeSort([5, 3, 7, 2, 4, 9, 1, 0]))
    print(mergeSort([3, 7, 9, 1, 4, 8, 2, 8, 9, 1, 3]))
    print(mergeSort([1]))

if __name__ == "__main__":
    main()