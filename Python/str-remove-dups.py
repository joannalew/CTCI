# CTCI 1.3
# Design an algorithm and write code to remove the duplicate characters
# in a string without using any additional buffer.

# Returns string without duplicates
# Runtime: O(n^2), where n is the length of s
def remove_dups(s):
	length = len(s)
	if length < 2:
		return s

	for i in range(length - 1, 0, -1):
		for j in range(i - 1, -1, -1):
			if s[i] == s[j]:
				s = s[:i] + s[i+1:]
				break

	return s

# Using additional memory of constant size (fixed array)
# Runtime: O(n), where n is len(s); uses array of size 256
def remove_dups_list(s):
	if len(s) < 2:
		return s

	chars = [False] * 256
	i = 0

	while i < len(s):
		idx = ord(s[i])
		if chars[idx]:
			s = s[:i] + s[i+1:]
		else:
			chars[idx] = True
			i += 1

	return s

def main():
	print (remove_dups('a'))
	print (remove_dups('aa'))
	print (remove_dups('abcadierajdkb'))
	print (remove_dups('abcdefg'))
	print (remove_dups('aaabbb'))
	print (remove_dups(''))
	print (remove_dups('ababababa'))


if __name__ == "__main__": 
	main()