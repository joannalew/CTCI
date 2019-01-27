# CTCI 1.7
# Given a N x N matrix, rotate the matrix by 90 degrees

# [ 1, 2, 3 ]           [ 3, 6, 9 ]
# [ 4, 5, 6 ]     =>    [ 2, 5, 8 ]
# [ 7, 8, 9 ]           [ 1, 4, 7 ]

# [ 00 01 02 ]          [ 02 12 22 ]
# [ 10 11 12 ]    =>    [ 01 11 21 ]
# [ 20 21 22 ]          [ 00 10 20 ]

# Method: create another array, and
# store the element at the corresponding index
def rotate_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = [[0 for j in range(cols)] for x in range(rows)]

    for i in range(rows):
        for j in range(cols):
            res[i][j] = mat[j][rows - i - 1]

    return res


def print_matrix(mat):
    for row in mat:
        print(row)

def main():
    print_matrix(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == "__main__":
    main()