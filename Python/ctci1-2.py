# CTCI 1.2 - Reverse a string
# Write code to reverse a C-style string
def reverse(s):
	length = len(s)

	if length == 1:
		return ''

	res = ''
	for i in range(length - 2, -1, -1):
		res += s[i]
	return res

# Write code to reverse a C-style string in place
def reverse_in_place(s):
	rev = s[::-1]				# reverse by slicing
	return rev[1:]				# remove 0

def main():
	a = ['abcdefg0', 'tiems0', 'a0', '0', '2348723840']
	for x in a:
		print (reverse_in_place(x))


if __name__ == "__main__": 
	main()