# LeetCode 784: Letter Case Permutation
# Given a string, transform each letter individually to be
# uppercase or lowercase to create another string
# Return a list of all possible strings we could create

# Example: letterCasePermute("a1b2")
#   Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Example: letterCasePermute("3z4")
#   Output: ["3z4", "3Z4"]


def letterCasePermutationHelper(string, res, holder):
	if len(string) <= 0:
		holder.append(res)
		return res
	else:
		if ord(string[0]) >= ord('0') and ord(string[0]) <= ord('9'):
			res += string[0]
			letterCasePermutationHelper(string[1:], res, holder)
		else:
			res += string[0].lower()
			letterCasePermutationHelper(string[1:], res, holder)
			res = res[:-1]
			res += string[0].upper()
			letterCasePermutationHelper(string[1:], res, holder)
			res = res[:-1]


def letterCasePermutation(string):
	holder = []
	letterCasePermutationHelper(string, "", holder)
	return holder

def main():
    print(letterCasePermutation("a1b2"))  # => ["a1b2", "a1B2", "A1b2", "A1B2"]
    print(letterCasePermutation("3z4")) # => ["3z4", "3Z4"]
    print(letterCasePermutation("12345")) # => ["12345"]

if __name__ == "__main__":
    main()
