#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        def solveMem(i, cap):
            
            if i==0:
                
                if wt[i]<=cap:
                    return val[i]
                    
                else:
                    return 0
                    
            
            if dp[i][cap]!=-1:
                return dp[i][cap]
                    
                
            # inc
            inc=0
            if cap-wt[i]>=0:
                inc = val[i] + solveMem(i-1, cap-wt[i])
            
            # exc
            exc = solveMem(i-1, cap)
            
            
            dp[i][cap] = max(inc, exc)
            return dp[i][cap]
            
            
            
            
            
            
        dp=[[-1]*(W+1) for _ in range(n)]
        return solveMem(n-1, W)
        
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends