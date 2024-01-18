#User function Template for python3

class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        
        def solve(n,m,mat, i, j):
            nonlocal maxi
            
            if i>=n or j>=m:
                return 0
                
            diagonal=solve(n,m,mat, i+1, j+1)
            right=solve(n,m,mat, i, j+1)
            
            down=solve(n,m,mat, i+1, j)
            
            
            if mat[i][j]==1:
                ans=1+min(right, diagonal , down)
                
                maxi=max(maxi, ans)
                
                return ans
                
            else:
                return 0
                
        def solveMem(n,m,mat, i, j, dp):
            nonlocal maxi
            
            if i>=n or j>=m:
                return 0
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
            diagonal=solveMem(n,m,mat, i+1, j+1, dp)
            right=solveMem(n,m,mat, i, j+1 , dp)
            down=solveMem(n,m,mat, i+1, j, dp)
            
            
            if mat[i][j]==1:
                dp[i][j]=1+min(right, diagonal , down)
                
                maxi=max(maxi, dp[i][j])
                
                return dp[i][j]
                
            else:
                dp[i][j]=0
                return dp[i][j]
                
        def solveTab(n,m,mat):
            nonlocal maxi
            
            dp=[[0]*(m+1) for _ in range(n+1)]
            dp[n][m]=0
            
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    
                    diagonal=dp[i+1][j+1]
                    right=dp[i][j+1]
                    down=dp[i+1][j]
                    
                    
                    if mat[i][j]==1:
                        dp[i][j]=1+min(right, diagonal , down)
                        
                        maxi=max(maxi, dp[i][j])
                        
                        
                        
                    else:
                        dp[i][j]=0
                        
                        
        def solveTabOpt(n,m,mat):
            nonlocal maxi
            
            curr=[0]*(m+1)
            nex=[0]*(m+1)
            
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    
                    diagonal=nex[j+1]
                    right=curr[j+1]
                    down=nex[j]
                    
                    
                    if mat[i][j]==1:
                        curr[j]=1+min(right, diagonal , down)
                        
                        maxi=max(maxi, curr[j])
                        
                        
                        
                    else:
                        curr[j]=0
                        
                    
                nex=curr[:]
                
        def solveTabO1(n,m,mat):
           
            nonlocal maxi
            
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    
                    
                    
                    if mat[i][j]==1 and i<n-1 and j<m-1:
                         mat[i][j]=1+min(mat[i+1][j],min(mat[i][j+1],mat[i+1][j+1]))
                        
                    maxi=max(maxi, mat[i][j])
                        
                        
                        
                    
                
                
                
        maxi=0
        # dp=[[-1]*(m+1) for _ in range(n+1)]
        # solveMem(n,m,mat, 0, 0, dp)
        # return maxi
        
        solveTabO1(n,m,mat)
        return maxi





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        arr = input().split()
        for i in range(n*m):
            mat[i//m][i%m] = int(arr[i])
        
        ob = Solution()
        print(ob.maxSquare(n, m, mat))
# } Driver Code Ends