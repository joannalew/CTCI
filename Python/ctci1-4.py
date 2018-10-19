# CTCI 1.4
# Write a method to determine if two strings are anagrams or not

# Method: counting characters in each string; making sure they have same num of chars
# Runtime: O(len(s1) + len(s2) + 256); uses array of size 256
def anagram(s1, s2):
	if len(s1) != len(s2):
		return False

	chars = [0] * 256

	for c in s1:
		chars[ord(c)] += 1

	for c in s2:
		chars[ord(c)] -= 1

	for count in chars:
		if count != 0:
			return False

	return True

# Method: sort the strings and compare
# Runtime: O(n log n), where n is the length of the longer string; creates arrays
def anagram_sort(s1, s2):
	s1 = ''.join(sorted(s1))
	s2 = ''.join(sorted(s2))
	return s1 == s2

def main():
	print (anagram('a', 'a'))
	print (anagram('abcdefg', 'cbdeagf'))
	print (anagram('abcabc', 'abcabc'))
	print (anagram('aaabbb', 'aabbcc'))
	print (anagram('abc', 'ab'))

if __name__ == "__main__": 
	main()