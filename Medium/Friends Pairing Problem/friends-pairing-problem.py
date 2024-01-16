#User function Template for python3

mod=10**9+7

class Solution:
    def countFriendsPairings(self, n):
        # code here 


        # Recurrence relation wala dp  :(
        
        
        def solve(n):
            if n==1:return 1
            
            if n==2:
                return 2
                
            if dp[n]!=-1:
                return dp[n]
                
                
            dp[n] = ((solve(n-1))%mod + ((n-1)*solve(n-2))%mod)%mod
            return dp[n]
        
        
        dp=[-1]*(n+1)
        return solve(n)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends