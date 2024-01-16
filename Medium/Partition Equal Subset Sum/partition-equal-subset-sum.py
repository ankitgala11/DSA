# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        
        
        def solve(i, s):
            if i>=N:
                return 0
                
            if s<0:
                return 0
                
                
            if s==0:
                return 1
                
            if dp[i][s]!=-1:
                return dp[i][s]
                
            inc=solve(i+1 , s-arr[i])
            exc=solve(i+1, s)
            
            dp[i][s] = inc or exc
            return dp[i][s]
            
            
            
            
        s=sum(arr)
        if s&1:
            return False
            
     
        s=s//2
        
        dp=[[-1]*(s+1) for _ in range(N)]
        
        return solve(0, s )


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends