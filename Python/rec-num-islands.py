def floodIsland(grid, x, y):
    if ((x < len(grid)) and (x >= 0) and 
        (y < len(grid[0])) and (y >= 0) and 
        (grid[x][y] == "1")):

        grid[x][y] = "0"
        floodIsland(grid, x - 1, y)
        floodIsland(grid, x + 1, y)
        floodIsland(grid, x, y - 1)
        floodIsland(grid, x, y + 1)

    else:
        return
    
def numIslands(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == "1"):
                floodIsland(grid, i, j)
                count += 1   
    
    return count

def main():
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # => 1
    print(numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))  # => 3

if __name__ == "__main__":
    main()