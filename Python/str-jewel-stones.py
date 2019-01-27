# LeetCode 771: Jewels and Stones
# You're given strings J representing the types of stones 
# that are jewels, and S representing the stones you have.  
# Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in 
# J and S are letters. Letters are case sensitive, so "a" is considered 
# a different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0

# Method: put the letters of J (jewels) in a set
# Iterate through S (stones), and increment count if letter in jewel set
def numJewelsInStones(self, J, S):
    s = set()
    for letter in J:
        s.add(letter)
    
    count = 0
    for letter in S:
        if letter in s:
            count += 1
    
    return count

# Method: iterate through jewels
# Count the number of that jewel in S (stones)
# Add to running sum; return sum
def numJewelsInStonesBetter(self, J, S):
    count = 0
    
    for letter in J:
        count += S.count(letter)
    
    return count

# Method: Iterate through stones
# Count the stone if it's also in jewel
def numJewelsInStonesBest(self, J, S):
    count = 0
    
    for letter in S:
        if letter in J:
            count += 1
            
    return count