#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        def solve(n, k):
            
            if n==1 or k==1 or k==0:
                return k
                
            if dp[n][k]!=-1:
                return dp[n][k]
                
                
            res=float('inf')
            # dropping the egg from ith floor
            for i in range(1, k+1):
                
                # does not break
                # then it wont break from any floor below i so we will check floors above i
                chance1 = 1 + solve(n, k-i)
                
                # breaks 
                # reducing egg by 1 and floor by 1
                chance2 = 1 + solve(n-1, i-1)
                
                # always considering the worst case scenario 
                worst=max(chance1, chance2)
                
                
                res=min(res, worst)
                
                
            dp[n][k]= res
            return dp[n][k]
            
            
        dp=[[-1]*(k+1) for _ in range(n+1)]    
        return solve(n, k)
                
                
                
                
           
                
         

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
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends