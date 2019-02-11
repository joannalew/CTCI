# LeetCode 46: Permutations
# Given a collection of distinct integers,
# Return all possible permutations

# Example:
# Input: [1, 2, 3]
# Output: [ [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1] ]

def permute(nums):
	res = []
	permuteHelper([], nums, res)
	return res


def permuteHelper(step, nums, res):
	# Base Case
	if len(step) == len(nums):
		res.append(step[:])
		return

	for num in nums:
		# element already exists, skip
		if num in step:
			continue

		step.append(num)				# choose
		permuteHelper(step, nums, res)	# explore
		del step[-1]					# unchoose

def main():
	test = [1, 2, 3]
	print (permute(test))

if __name__ == "__main__": 
	main()
