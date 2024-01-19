#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        def solve(i, w):
            if i>=N:
                return 0
                
            if dp[i][w]!=-1:
                return dp[i][w]
                
            inc=0
            if wt[i]<=w:
                inc=val[i]+solve(i, w-wt[i])
                
            exc=solve(i+1, w)
            
            
            dp[i][w]= max(inc, exc)
            return dp[i][w]
            
            
        def solveTab():
            dp=[[-1]*(W+2) for _ in range(N+1)]
            
            
            for i in range(N-1, -1, -1):
                
                for w in range(W+1):
                    
                    inc=0
                    if wt[i]<=w:
                        inc=val[i]+dp[i][w-wt[i]]
                        
                    exc=dp[i+1][w]
                    
                    
                    dp[i][w]= max(inc, exc)
            return dp[0][W]
                    
            
        # dp=[[-1]*(W+1) for _ in range(N)]
        # return solve(0, W)
        
        return solveTab()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends