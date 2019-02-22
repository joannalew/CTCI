# LeetCode 905: Sort Array By Parity
# Given an array A of non-negative integers, 
#   return an array consisting of all the even elements of A, 
#   followed by all the odd elements of A.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

def sortArrayByParity(A):
    odd = []
    even = []

    for el in A:
        if el % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
            
    return even + odd
        
def main():
    print(sortArrayByParity([3, 1, 2, 4]))
    print(sortArrayByParity([1, 2, 3, 4, 5, 6]))
    print(sortArrayByParity([5, 6, 3, 2, 8, 6, 4, 7, 5, 8, 11]))

if __name__ == "__main__":
    main()