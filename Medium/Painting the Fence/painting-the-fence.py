#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

mod=10**9 + 7

class Solution:
    def countWays(self,n,k):
        #code here.
        # // at each post
        # // same => how many ways to have same last 2 color 
        # // diff => how many ways to have different last 2 color 
        # // diff = (total_previous_color)*(k-1)  
        # // same = (previous_diff_color)   
        M = 10**9+7
        same, diff = 0, k
        for i in range(1, n):
            diff, same = (same+diff)*(k-1)%M, diff
        return (same+diff)%M
        


'''
    def countWays(self,n,k):
        #code here.
        
        def solveMem(n):
            
            if n==1:
                return k
                
            if n==2:
                return k**2
                
                
            if dp[n]!=-1:return dp[n]
            
            
            dp[n]=((solveMem(n-1)*(k-1))%mod + (solveMem(n-2)*(k-1))%mod)%mod
            
            return dp[n]
            
            
        def solveTab():
            
            if n==1:return k
            dp=[0]*(n+1)
                
            dp[1]=k
            dp[2]=k**2
            
            for i in range(3, n+1):
                
                dp[i] = (dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)) % mod
                
            return dp[n]
        
        
        # dp=[-1]*(n+1)
        
        # return solveMem(n)
        
        return solveTab()
            
            
'''


#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends