#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        
        def issafe(i, j):
            if i>=0 and i<n and j>=0 and j<m and vis[i][j]==1:
                return True
                
            return False
        
        def dfs(i, j):
            vis[i][j]=0
            
            for x in range(8):
                newi=i+row[x]
                newj=j+col[x]
                
                if issafe(newi, newj):
                    dfs(newi, newj)
            
            
            
        row=[-1,-1,0,1,1,1,0,-1]
        col=[0,1,1,1,0,-1,-1,-1]
            
            
            
            
        n=len(grid)
        m=len(grid[0])
        
        vis=grid[:]
        
        ans=0
        
        for i in range(n):
            for j in range(m):
                if vis[i][j]==1:
                    ans+=1
                    dfs(i , j)
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends