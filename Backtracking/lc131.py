# LeetCode 131: Palindrome Partitioning
# Given a string s, partition s such that 
# every substring of the partition is a palindrome.

# Example:
# Input: "aab"
# Output: [ ["aa", "b"], ["a", "a", "b"] ]

# https://bit.ly/2P9KO5b
# https://bit.ly/2PclkUM

def partition(s):
	# Backtracking
	# Edge case
	if s == None or len(s) == 0:
		return []

	res = []
	helper(s, [], res)
	return res


def helper(s, step, result):
	# Base Case
	if s == None or len(s) == 0:
		result.append(step[:])		# don't forget to copy!
		return

	for i in range(1, len(s) + 1):
		temp = s[0 : i]

		# only do backtracking if current string is palindrome
		if not isPalindrome(temp):
			continue

		step.append(temp) 						# choose
		helper(s[i : len(s)], step, result)		# explore
		del step[-1]							# unchoose

	return

def isPalindrome(s):
	left = 0
	right = len(s) - 1

	while left <= right:
		if s[left] != s[right]:
			return False
		left += 1
		right -= 1

	return True


def main():
	test = "aabaa"
	print (partition(test))

if __name__ == "__main__": 
	main()
