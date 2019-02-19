# LeetCode 4: Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example: nums1 = [1, 3], nums2 = [2]
#          The median is 2.0

# Example: nums1 = [1, 2], nums2 = [3, 4]
#          The median is (2 + 3)/2 = 2.5


# Method:
# 1. Calculate the medians m1, m2 of the input arrays a1[] and a2[]
# 2. If m1 and m2 are equal, then we're done. return m1 or m2.
# 3. If m1 > m2, the median is in one of the following two subarrays:
#       a. From the first element of a1 to m1 --> a1[0 ... n/2]
#       b. From m2 to the last element of a2 --> a2[n/2 ... -1]
# 4. If m2 > m1, the median is is in one of the following two subarrays:
#       a. From m1 to the last element of a1 --> a1[n/2 ... -1]
#       b. From the first element of a2 to m2 --> a2[0 ... n/2]
# 5. Repeat above steps until size of both subarrays becomes 2
# 6. If size of two arrays is 2, the use formula below to get median:
#       median = (max(a1[0], a2[0]) + min(a1[1], a2[1])) / 2

def findMedian(nums):
    length = len(nums)

    if length < 1:
        return 0
    elif length % 2 == 1:
        return nums[int(length / 2)]
    
    return (nums[int(length / 2) - 1] + nums[int(length / 2)]) / 2

def findMedianSortedArrays(nums1, nums2):
    length1 = len(nums1)
    length2 = len(nums2)

    if length1 == 2 and length2 == 2:
        return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

    m1 = findMedian(nums1)
    m2 = findMedian(nums2)

    if m1 == m2:
        return m1
    elif m1 > m2:
        return findMedianSortedArrays(nums1[:int(length1/2) + 1], nums2[int(length2/2):]) 
    else:
        return findMedianSortedArrays(nums1[int(length1/2):], nums2[:int(length2/2) + 1])

def main():
    print(findMedianSortedArrays([1, 3], [2]))
    print(findMedianSortedArrays([1, 2], [3, 4]))
    print(findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
    print(findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
    print(findMedianSortedArrays([1, 2], [1, 2, 3]))

if __name__ == "__main__":
    main()

