# CTCI 8.2
# Imagine a robot sitting on the upper left hand corner of an NxN grid.
# The robot can only move in two directions: right and down.
# How many possible paths are there for the robot?

# Return list with all the possible paths 
def printPaths(mat):
	m = len(mat)
	n = len(mat[0])

	allpaths = []
	path = [0 for d in range(m + n - 1)]

	findPathsUtil(mat, m, n, 0, 0, path, 0, allpaths)
	return allpaths

# Helper function for printPaths
def findPathsUtil(mat, m, n, i, j, path, idx, allpaths):
	# if reached bottom of mat, can only move right
	if i == m - 1:
		for k in range(j, n):
			path[idx + k - j] = mat[i][k]

		allpaths.append(path.copy())
		return

	# if reach right of mat, can only move down
	if j == n - 1:
		for k in range(i, m):
			path[idx + k - i] = mat[k][j]

		allpaths.append(path.copy())
		return

	# add current element to path list
	path[idx] = mat[i][j]
	findPathsUtil(mat, m, n, i + 1, j, path, idx + 1, allpaths)	# check right
	findPathsUtil(mat, m, n, i, j + 1, path, idx + 1, allpaths)	# check down

# Counts the number of possible paths from TL to BR
def countPaths(m, n):
	# Base Case: if there's only a row or columns, then only 1 possible way
	if m == 1 or n == 1:
		return 1

	# Iterative step: count the number of rights & downs
	return countPaths(m - 1, n) + countPaths(m, n - 1)

# Prints a matrix
def printMat(mat):
	for row in mat:
		print (row)


def main():
	mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
	printMat(printPaths(mat))
	print (countPaths(len(mat), len(mat[0])))

	print ('---------------')

	mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	printMat(printPaths(mat))
	print (countPaths(len(mat), len(mat[0])))


if __name__ == "__main__": 
	main()

