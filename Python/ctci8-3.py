# CTCI 8.3
# Write a method that returns all subsets of a set

# Using bitwise operators
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


def main():
	s = {1, 2, 3, 4, 5, 6, 7}
	subsets = sorted(findSubsets(s), key=len)

	for sub in subsets:
		print (sub)


if __name__ == "__main__": 
	main()