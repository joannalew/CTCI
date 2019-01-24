# CTCI 8.3
# Write a method that returns all subsets of a set

# Iterative: using bitwise operators
# Total number of subsets = 2^n, where n is length of set
# Notice that binary representation of (0...2^n) correlates to elements in subset

# i.e. Given a set {a, b, c, d}, 
# 0000 = {}, 0001 = {a}, 0010 = {b}, 0011 = {a, b}, 0010 = {c}, etc.
def findSubsets(s):
	res = []
	n = len(s)

	for i in range(0, (1 << n)):				# i from 0 to 2^n
		sub = []								
		for j, el in enumerate(s):				# for each element in set
			if (i & (1 << j)) > 0:				# if index matches up with binary i
				sub.append(el)					# append to subset
		res.append(set(sub))

	return res


# Backtracking
# Have two choices for each element: include or don't
def findSubsetsBack(s):
	res = []
	sub = []

	res.append(set(sub))			# add the null set
	subsetsUtil(s, res, sub, 0)

	return res

def subsetsUtil(s, res, sub, index):
	for i, el in enumerate(s):				# for i in range(index, len(s))
		if i >= index: 
			sub.append(el)					# sub.append(s[i])
			res.append(set(sub))

			subsetsUtil(s, res, sub, i+1)

			sub.pop()
	
	return

def main():
	s = {1, 2, 3, 4, 5, 6, 7}
	subsets = sorted(findSubsets(s), key=len)
	subsetsBack = sorted(findSubsetsBack(s), key=len)

	for sub in subsets:
		print (sub)

	print (len(subsets) == len(subsetsBack))
	


if __name__ == "__main__": 
	main()