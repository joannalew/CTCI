# LeetCode 36: Valid Sudoku
# Determine if a 9x9 Sudoku board is valid. 
# Only the filled cells need to be validated.

def isValidSudoku(board):
	size = 9
	rows = set()
	cols = set()
	squares = set()
	
	for i in range(size):
		rows.clear()
		cols.clear()
		
		for j in range(size):
			if board[i][j] in rows or board[j][i] in cols:
				return False
			
			if board[i][j] != '.':
				rows.add(board[i][j])
			if board[j][i] != '.':
				cols.add(board[j][i])
	
	for k in range(0, 9, 3):
		for m in range(0, 9, 3):
			for i in range(0 + k, 3 + k):
				for j in range(0 + m, 3 + m):
					if board[i][j] in squares:
						return False
					
					if board[i][j] != '.':
						squares.add(board[i][j])
	
			squares.clear()
	
	return True

def main():
    # => True
    print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

if __name__ == '__main__':
    main()
