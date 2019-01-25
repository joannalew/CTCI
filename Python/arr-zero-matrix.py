# CTCI 1.8
# Write a method such that if an element in an M x N matrix is 0,
# its entire row and column are set to 0

# Method: record the row and column index of all the zeros in the matrix
# Iterate through matrix again, setting elements with matching index to 0
def zero_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    zeroRow = set()
    zeroCol = set()

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                zeroRow.add(i)
                zeroCol.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in zeroRow or j in zeroCol:
                mat[i][j] = 0
    
    return mat

# Method: record the row and column index of all the zeros in the matrix
# Instead of storing in set, store in two 1-d arrays as boolean
# Iterate through array, if element is true, zero out that row or column
# Improvement: don't need to iterate through whole matrix again
def zero_matrix_better(mat):
    rows = len(mat)
    cols = len(mat[0])

    zeroRow = [False] * rows
    zeroCol = [False] * cols

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                zeroRow[i] = True
                zeroCol[j] = True
    
    for i in range(rows):
        if zeroRow[i]:
            for j in range(cols):
                mat[i][j] = 0

    for j in range(cols):
        if zeroCol[j]:
            for i in range(rows):
                mat[i][j] = 0

    return mat


def print_matrix(mat):
	for row in mat:
		print(row)

def main():
	print_matrix(zero_matrix_better([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
	print_matrix(zero_matrix_better([[1, 2, 3, 0], [2, 3, 1, 2], [0, 2, 2, 1], [5, 6, 7, 8]]))

if __name__ == "__main__": 
	main()