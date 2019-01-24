# CTCI 1.1
# Implement an algorithm to determine if a string has all unique characters
# Returns true if all characters unique; false if duplicate characters exist
# Runtime: O(n), where n is len(s); uses an additional array of size 256
def is_unique(s):
	letters = [False] * 256			# characters, not just letters!
	for c in s:
		idx = ord(c)
		if letters[idx]:
			return False
		letters[idx] = True
	return True


# CTCI 1.1 - Part 2
# What if you can not use additional data structures?
# Runtime: O(n^2), where n is len(s)
def is_unique_slow(s):
	length = len(s)

	if length == 1:
		return True

	for i in range(length - 1):
		for j in range(i + 1, length):
			if s[i] == s[j]:
				return False

	return True

# CTCI 1.1 - Using Bitwise Operators
# Assuming string only contains lowercase letters
def is_unique_bitwise(s):
	check = 0

	for c in s:
		val = ord(c) - ord('a')			# get ascii value
		if check & (1 << val) > 0:		# if it toggles a bit already hit
			return False 				# character has already been seen
		check |= (1 << val)				# else, record in check's bits

	return True

# CTCI 1.1 - Sort, then iterate through
# Runtime: O(n log n), where n is len(s); possible additional data structures
def is_unique_sort(s):
	s_sort = ''.join(sorted(s))
	prev = s_sort[0]

	for c in s_sort[1:]:
		if c == prev:
			return False
		prev = c

	return True

def main():
	print (is_unique_sort('a'))
	print (is_unique_sort('zo'))
	print (is_unique_sort('abcdefg'))
	print (is_unique_sort('aa'))
	print (is_unique_sort('abcdzicoecm'))




if __name__ == "__main__": 
	main()
