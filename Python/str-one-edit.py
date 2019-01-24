# CTCI 1.5
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.
# There are three types of edits that can be performed on strings:
#    1. Insert a character
#    2. Remove a character
#    3. Replace a character

# Method: Iterate through both strings; check for only one difference
# Have 2 pointers checking each character of both strings
# If characters don't match, log the difference
# Increment the pointer on the shorter string only if it's a replacement
# Insertion and deletion are the same thing, mirrored
def one_edit(s1, s2):
    length1 = len(s1)
    length2 = len(s2)

    if (abs(length1 - length2)) > 1:
        return False

    shorter = s1 if length1 < length2 else s2
    longer = s2 if length1 < length2 else s1

    i = 0
    j = 0
    foundDiff = False

    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:             # if chars don't match
            if foundDiff:                       # and already found a diff
                return False                    # more than one edit away

            foundDiff = True                    # first edit
            if length1 == length2:              # increment shorter index
                i += 1                          # only if it's a replacement
        else:
            i += 1
        j += 1
    
    return True


    

def main():
    print(one_edit("pale", "ple"))  
    print(one_edit("pales", "pale"))
    print(one_edit("pale", "bale")) 
    print(one_edit("pale", "bake"))


if __name__ == "__main__": 
	main()