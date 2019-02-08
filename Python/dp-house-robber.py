# LeetCode 198
# You're a house robber, robbing houses on a street.
# Each house has a certain amount of money stashed.
# You can't rob houses that are adjacent to each other.
# Determine the max amount of money you can rob tonight.

# Example 1: robber([1, 2, 3, 1])
#   Output: 4
#   Rob house #1 ($1), and house #3 ($3) --> $4

# Example 2: robber([2, 7, 9, 3, 1])
#   Output: 12
#   Rob house #1 ($2), house #3 ($9), house #5 ($1) --> $12

# Example 3: robber([6, 7, 1, 3, 8, 2, 4])
#   Output: 19

# Example 4: robber([5, 3, 4, 11, 2])
#   Output: 16

def robber(nums):
    n = len(nums)

    # Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    # Memoize
    memo = [0] * n
    memo[0] = nums[0]
    memo[1] = max(nums[0], nums[1])

    for i in range(2, n):
        memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])

    return memo[-1]

def main():
    print(robber([1, 2, 3, 1])) # => 4
    print(robber([2, 7, 9, 3, 1])) # => 12

if __name__ == "__main__":
    main()