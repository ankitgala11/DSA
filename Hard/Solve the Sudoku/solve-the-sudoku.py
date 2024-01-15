#User function Template for python3

class Solution:
    
    # O(9N*N) O(N*N)
    
    def SolveSudoku(self,grid):
        
        def check(r,c,j):
            
            for i in range(9):
                if grid[r][i]==j:
                    return False
                    
                if grid[i][c]==j:
                    return False
                    
                if grid[3*(r//3)+i//3][3*(c//3)+i%3]==j:
                    return False
                    
                
            return True
                
            
        
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if grid[r][c]==0:
                        
                        for i in range(1, 10):
                            if check(r,c,i):
                                grid[r][c]=i
                                if solve():
                                    return True
                                else:
                                    grid[r][c]=0
                                    
                        return False
                        
            return True
            
        return solve()
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
     
        for i in grid:
            for j in i:
                print(j, end=" ")
         
                
            
                
        # Your code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends