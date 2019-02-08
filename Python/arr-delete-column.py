def minDeletionSize(A):
    count = 0
    checker = [0] * len(A[0])

    for word in A:
        for index, letter in enumerate(word):
            if checker[index] >= 0 and ord(letter) >= checker[index]:
                checker[index] = ord(letter)
            else:
                checker[index] = -1

    for num in checker:
        if num == -1:
            count += 1

    return count


def main():
    print(minDeletionSize(["cba","daf","ghi"])) # => 1
    print(minDeletionSize(["a","b"])) # => 0
    print(minDeletionSize(["zyx","wvu","tsr"])) # => 3

if __name__ == "__main__":
    main()