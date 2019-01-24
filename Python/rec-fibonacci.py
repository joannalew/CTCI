# CTCI 8.1
# Write a method to generate the nth Fibonacci number

# Recursively
# Base Case: fib starts with 0 & 1
# Iterative Step: fib(n) = fib(n - 1) + fib(n - 2)
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	return fib(n - 1) + fib(n - 2)

# Iteratively
# Loop up to n, adding up the previous two values
def fib_iter(n):
	if n == 0:
		return 0

	first = 0
	second = 1

	for i in range(1, n):
		res = first + second
		first = second
		second = res

	return second

def main():
	for i in range(10):
		print (fib(i))


if __name__ == "__main__": 
	main()
