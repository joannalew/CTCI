# CTCI 8.4
# Write a method to compute all permutations of a string

# Given a string 'abc'
# Let first letter = 'a' ; Remainder = 'bc'
# Let list = permute(bc) = {'bc', 'cd'}
# Push 'a' into subword 'bc' -> {'abc', 'bac', 'bca'}, 
	# and 'cb'

def permutations(s):
	# Base Case: if there's one letter, then that's the permutation
	if len(s) == 1:
		return [s]

	# Iterative Step:
	# Take off the first letter
	# Find the possible permutations of the rest of the letters
	# Insert first letter at all possible positions in subwords
	letter = s[0]
	res = []
	lst = permutations(s[1:])

	for el in lst:
		for i, c in enumerate(el):
			res.append(el[:i] + letter + el[i:])
		res.append(el + letter)

	return res



def main():
	print(set(permutations('ab')))
	print(sorted(set(permutations('stop'))))


if __name__ == "__main__": 
	main()