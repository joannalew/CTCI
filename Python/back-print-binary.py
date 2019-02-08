# Stanford CS 106B Backtracking Intro
# Print out all Binary Numbers with n number of digits
# Example: n = 2
# 	Output: 00, 01, 10, 11
# Example: n = 3
# 	Output: 000, 001, 010, 011, 100, 101, 110, 111

def printAllBinaryHelper(n, s):
	if n == 0:
		print(s)
		return
    
	printAllBinaryHelper(n - 1, s + '0')
	printAllBinaryHelper(n - 1, s + '1')

def printAllBinary(n):
	if n == 0:
		return ''
    
	printAllBinaryHelper(n, '')    


def main():
	printAllBinary(2)
	print('-----------------')
	printAllBinary(3)
	print('-----------------')
	printAllBinary(5)

if __name__ == "__main__": 
	main()