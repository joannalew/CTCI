# CTCI 1.6
# Write a method to perform basic string compression using
# the counts of repeated characters.
# Example: aabcccccaaa => a2b1c5a3
# If compressed string is longer than original, return original string


# Method: Iterate through string
# If current character is the same as previous character, increment count
# Otherwise, add previous character and count to result string
# Check length of result string; return if shorter; otherwise return original
def string_compression(s):
    last_char = ''
    count = ''
    res = ''

    for ch in s:
        if ch == last_char:
            count += 1
        else:
            res = res + last_char + str(count)
            last_char = ch
            count = 1

    res = res + last_char + str(count)

    if (len(res) > len(s)):
        return s

    return res


def main():
	print(string_compression('aabcccccaaa'))
	print(string_compression('abcdefg'))
	print(string_compression('a'))
	print(string_compression('assssbdddfffaa'))

if __name__ == "__main__": 
	main()