# LeetCode 11: Container with Most Water
# Given n non-negative integers a1, a2, ..., an, 
#   where each represents a point at coordinate (i, ai). 
#   n vertical lines are drawn such that the two endpoints of line i 
#   is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, 
#   such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Example Input: [1,8,6,2,5,4,8,3,7]
#   Output: 49

def maxArea(height):
	length = len(height)
	
	pointerLeft = 0
	pointerRight = length - 1
	maxArea = 0
	
	while pointerLeft < pointerRight:
		area = (pointerRight - pointerLeft) * min(height[pointerLeft], height[pointerRight])
		if area > maxArea:
			maxArea = area
		
		if height[pointerLeft] < height[pointerRight]:
			pointerLeft += 1
		else:
			pointerRight -= 1
	
	return maxArea

def main():
    print(maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == "__main__":
	main()