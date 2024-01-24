#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        def solve(i, j):
            
            if i==j:
                return 0
                
            if dp[i][j]!=-1:
                return dp[i][j] 
                
            mini=float('inf')
            for k in range(i, j):
                
                ans= arr[i-1] * arr[k] * arr[j] + solve(i, k) + solve(k+1, j)
                
                
                mini= min(ans, mini)
                
                
                
                
            dp[i][j]= mini
            return dp[i][j]
            
            
        def solveTab():
            dp=[[0]*(N+1) for _ in range(N+1)]
            
            for i in range(N-1, 0, -1):
                for j in range(1, N):
                    
                    
                    mini=float('inf')
                    for k in range(i, j):
                        
                        ans= arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j]
                        
                        
                        mini= min(ans, mini)
                        
                        
                        
                        
                        dp[i][j]= mini
                    
            return dp[1][N-1]
                    
            
           
            
            
        # dp=[[-1]*N for _ in range(N)]
        # return solve(1, N-1)
                
                
        return solveTab()
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends