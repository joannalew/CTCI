
# CTCI 1.5
# Write a method to replace all spaces in a string with '%20'

# Uses Python's replace function
# Runtime: O(num_spaces * len(s)), assuming replace is O(len(s))
def replace_spaces2(s):
	replaced = True

	while replaced:
		replaced = False
		old = len(s)
		s = s.replace(' ', '%20')
		if len(s) != old:
			replaced = True

	return s

# Concatenate appropriate characters to a second string
# Runtime: O(n), where n is length of string
def replace_spaces(s):
	res = ''

	for c in s:
		if c == ' ':
			res += '%20'
		else:
			res += c

	return res



def main():
	print (replace_spaces('a b c'))
	print (replace_spaces('abc'))
	print (replace_spaces('a bc'))
	print (replace_spaces('a b c '))
	print (replace_spaces(' a b c'))

if __name__ == "__main__": 
	main()