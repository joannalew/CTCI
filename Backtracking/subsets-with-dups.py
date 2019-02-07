# LeetCode 90: Subsets II 	(The Sets Strike Back!)
# Given a collection of integers that might contain duplicates, nums
# Return all possible subsets (the power set)
# Note: The solution set must not contain duplicate subsets

# Example:
# Input: [1, 2, 2]
# Output: [ [], [1], [2], [1, 2], [2, 2], [1, 2, 2] ]

def subsetsDup(nums):
	res = []
	nums = sorted(nums)				# sort to compare dups
	helper(res, [], nums, 0)
	return res

def helper(res, step, nums, start):
	res.append(step[:])

	for i in range(start, len(nums)):
		# skip duplicates
		if (i > start and nums[i] == nums[i-1]):
			continue

		step.append(nums[i])
		helper(res, step, nums, i + 1)
		del step[-1]

def main():
	test = [1, 2, 2]
	print (subsetsDup(test))

if __name__ == "__main__": 
	main()