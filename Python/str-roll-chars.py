# Upstart Coding Challenge 2/26/2019
# Roll the characters of string
# Given a string s and an array roll 
#   where roll[i] represents rolling first roll[i] characters in string. 
# We need to apply every roll[i] on string and output final string. 
# Rolling means increasing ASCII value of character, 
#   like rolling ‘z’ results in ‘a’, rolling ‘b’ results in ‘c’, etc.

# Example: s = 'abz', roll = [3, 2, 1]
#   Roll[0] = 3: shift 3 letters --> 'bca'
#   Roll[1] = 2: shift 2 letters --> 'cda'
#   Roll[2] = 1: shift 1 letter --> 'dda'

def rollTheString(s, roll):
    convert = [0] * len(s)
    res = ""

    for r in roll:
        convert[0] += 1
        if not r >= len(convert):
            convert[r] -= 1
    
    for i in range(1, len(s)):
        convert[i] = convert[i] + convert[i - 1]
    
    for i in range(len(s)):
        res += chr(((ord(s[i]) - ord('a') + convert[i]) % 26) + ord('a'))
    
    return res

def main():
    print(rollTheString('abz', [3, 2, 1]))
    print(rollTheString('vwxyz', [1, 2, 3, 4, 5]))
    print(rollTheString('zdkaie', [1, 6, 3, 6]))

if __name__ == "__main__":
    main()