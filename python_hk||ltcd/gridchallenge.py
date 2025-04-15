def gridChallenge(grid):
    for f in range(len(grid)):  
        grid[f] = sorted(grid[f])
        print(grid[f])
        
    for c in range(len(grid[0])):    
        for f in range(1, len(grid)):    
            if grid[f][c] < grid[f - 1][c]:  
                print(grid[f][c], grid[f-1][c])
                return "NO"
             
    return "YES" 

grid = ["ebacd", "fghij", "olkmn", "trpqs", "xywuv"]
result = gridChallenge(grid)
print(result) 

           
