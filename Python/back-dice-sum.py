# Stanford CS 106B Backtracking Intro
# https://www.youtube.com/watch?v=Frr8U5_TTtg

# Write a function diceSum that accepts two integer parameters
# A number of dice to roll, and a desired sum of all die values
# Output all combinations of die values that add up exactly to that sum
# Example: diceSum(2, 7)
#   Output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 2}
# Example: diceSum(3, 7)
#   Output: {1, 1, 5}, {1, 2, 4}, {1, 3, 3}, {1, 4, 2}, {1, 5, 1},
#           {2, 1, 4}, {2, 2, 3}, {2, 3, 2}, {2, 4, 1},
#           {3, 1, 3}, {3, 2, 2}, {3, 3, 1},
#           {4, 1, 2}, {4, 2, 1},
#           {5, 1, 1}

def diceSumHelper(dice, desiredSum, chosen):
	if dice == 0:
		if desiredSum == 0:
			print(chosen)
		return chosen
	else:
		for i in range(1, 7):
			chosen.append(i)
			diceSumHelper(dice - 1, desiredSum - i, chosen)
			chosen.pop()

def diceSum(dice, desiredSum):
	result = []
	diceSumHelper(dice, desiredSum, result)

def main():
	diceSum(2, 7)
	print('--------------')
	diceSum(3, 7)

if __name__ == "__main__": 
	main()

