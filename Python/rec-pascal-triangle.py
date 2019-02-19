# LeetCode 118: Pascal's Triangle
# Given a non-negative integer, numRows,
#   generate the first numRows of Pascal's triangle

# Example: 
#   Input: 5
#   Output: [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        prevRows = generate(numRows - 1)
        lastRow = prevRows[-1]
        resRow = []

        for i in range(0, len(lastRow) - 1):
            resRow.append(lastRow[i] + lastRow[i + 1])
        resRow.insert(0, lastRow[0])
        resRow.append(lastRow[-1])

        prevRows.append(resRow)
        return prevRows

def printArray(arr):
    for row in arr:
        print(row)

def main():
    printArray(generate(5))
    print('-------------------')
    printArray(generate(10))

if __name__ == "__main__":
    main()
    