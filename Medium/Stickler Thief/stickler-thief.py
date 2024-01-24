#User function Template for python3
import sys

sys.setrecursionlimit(10**8)

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        
        def solve(i):
            
            if i>=n:
                return 0
                
            if dp[i]!=-1:
                return dp[i]
                
            inc=a[i]+solve(i+2)
            exc=solve(i+1)


            dp[i]= max(inc, exc)
            return dp[i]
            
        def solveTab():
            dp=[0]*(n+2)
            
            
            for i in range(n-1, -1, -1):
                inc=a[i]+dp[i+2]
                exc=dp[i+1]
    
    
                dp[i]= max(inc, exc)
                
                
            return max(dp[0], dp[1])
                
            
        # dp=[-1]*n
        
        # return max(solve(0) , solve(1) )


        return solveTab()
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends