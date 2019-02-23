# In a country popular for train travel, 
#   you have planned some train travelling one year in advance.  
# The days of the year that you will travel is given as an array days.  
# Each day is an integer from 1 to 365.

# Train tickets are sold in 3 different ways:
#   a 1-day pass is sold for costs[0] dollars;
#   a 7-day pass is sold for costs[1] dollars;
#   a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  
# For example, if we get a 7-day pass on day 2, 
#   then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

# Return the minimum number of dollars you need to travel every day 
#   in the given list of days.

# Example: 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# Here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, 
#   which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, 
#   which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, 
#   which covered day 20.
# In total you spent $11 and covered all the days of your travel.

def mincostTickets(days, costs):
    if len(days) <= 0:
        return 0
    
    memo = [0] * (days[-1] + 1)
    
    for i in range(1, (days[-1] + 1)):
        if i in days:
            if i < 7:
                memo[i] = min(memo[i - 1] + costs[0], costs[1], costs[2])
            elif i < 30:
                memo[i] = min(memo[i - 1] + costs[0], memo[i - 7] + costs[1], costs[2])
            else:
                memo[i] = min(memo[i - 1] + costs[0], memo[i - 7] + costs[1], memo[i - 30] + costs[2])
        else:
            memo[i] = memo[i - 1]
    
    return memo[-1]

def main():
    print(mincostTickets([1,4,6,7,8,20], [2,7,15])) # => 11
    print(mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])) # => 17
    print(mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50])) # => 50
    print(mincostTickets([6,9,10,14,15,16,17,18,20,22,23,24,29,30,31,33,35,37,38,40,41,46,47,51,54,57,59,65,70,76,77,81,85,87,90,91,93,94,95,97,98,100,103,104,105,106,107,111,112,113,114,116,117,118,120,124,128,129,135,137,139,145,146,151,152,153,157,165,166,173,174,179,181,182,185,187,188,190,191,192,195,196,204,205,206,208,210,214,218,219,221,225,229,231,233,235,239,240,245,247,249,251,252,258,261,263,268,270,273,274,275,276,280,283,285,286,288,289,290,291,292,293,296,298,299,301,303,307,313,314,319,323,325,327,329,334,339,340,341,342,344,346,349,352,354,355,356,357,358,359,363,364], [21,115,345])) # => 3040

if __name__ == "__main__":
    main()