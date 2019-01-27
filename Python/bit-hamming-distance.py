# LeetCode 461: Hamming Distance
# The Hamming distance between two integers is the 
# number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.
# Example:
# Input: x = 1, y = 4
# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions 
# where the corresponding bits are different.

# Method: convert number to binary, then to string
# Make the strings the same length
# Count the number of differences
# Return the count
def hammingDistance(self, x, y):
        first = str(bin(x))[2:]
        second = str(bin(y))[2:]
        
        len_first = len(first)
        len_second = len(second)
        
        if (len_first < len_second):
            first = (len_second - len_first) * "0" + first
        if (len_second < len_first):
            second = (len_first - len_second) * "0" + second
            
        count = 0
        
        for i in range(len(first)):
            if first[i] != second[i]:
                count += 1
        
        return count