# LeetCode 985: Sum of Even Numbers after Query
# We have an array A of integers, and an array queries of queries.

# Example:
# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]

# Explanation: 
#   At the beginning, the array is [1,2,3,4].
#   After adding 1 to A[0], the array is [2,2,3,4], 
#       and the sum of even values is 2 + 2 + 4 = 8.
#   After adding -3 to A[1], the array is [2,-1,3,4], 
#       and the sum of even values is 2 + 4 = 6.
#   After adding -4 to A[0], the array is [-2,-1,3,4], 
#       and the sum of even values is -2 + 4 = 2.
#   After adding 2 to A[3], the array is [-2,-1,3,6], 
#       and the sum of even values is -2 + 6 = 4.

def sumEvenAfterQueries(A, queries):
	sumEven = 0
	res = []
	
	for num in A:
		if num % 2 == 0:
			sumEven += num
			
	for query in queries:
		index = query[1]
		prevEven = A[index] if A[index] % 2 == 0 else 0
		
		A[index] += query[0]
		currEven = A[index] if A[index] % 2 == 0 else 0
		
		sumEven = sumEven - prevEven + currEven
		res.append(sumEven)
		
	return res

def main():
    print(sumEvenAfterQueries([1, 2, 3, 4], [[1,0],[-3,1],[-4,0],[2,3]]))

if __name__ == "__main__":
    main()