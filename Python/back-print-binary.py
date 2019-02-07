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