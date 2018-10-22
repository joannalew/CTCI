# LeetCode 78: Subsets
# Given a set of distinct integers, nums,
# Return all possible subsets (the power set)
# Note: The solution set must not contain duplicate subsets

# Example:
# Input: nums = [1, 2, 3]
# Output: [ [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3] ]


def subsets(nums):
	res = []
	helper(res, [], nums, 0)
	return res


def helper(res, step, nums, start):
	res.append(step[:])

	for i in range(start, len(nums)):
		step.append(nums[i])
		helper(res, step, nums, i + 1)
		del step[-1]


def main():
	test = [1, 2, 3]
	print (subsets(test))

if __name__ == "__main__": 
	main()
