# LeetCode 22: Generate Parentheses
# Given n pairs of parentheses, write a function to generate 
# all combinations of well-formed parentheses.

# Example: generateParenthesis(3)
#   Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

def checkParenthesis(string):
	count = 0

	for letter in string:
		if letter == '(':
			count += 1
		elif letter == ')' and count > 0:
			count -= 1
		else:
			return False

	if count == 0:
		return True
	return False

def generateParenthesisHelper(n, string, holder):
	if n == 0:
		if checkParenthesis(string):
			holder.append(string)
		return string
	else:
		string += '('
		generateParenthesisHelper(n - 1, string, holder)
		string = string[:-1]

		string += ')'
		generateParenthesisHelper(n - 1, string, holder)
		string = string[:-1]

def generateParenthesis(n):
	holder = []
	generateParenthesisHelper(n * 2, "", holder)
	return holder

def main():
	print(generateParenthesis(2))
	print('---------------------')
	print(generateParenthesis(3))

if __name__ == "__main__":
    main()