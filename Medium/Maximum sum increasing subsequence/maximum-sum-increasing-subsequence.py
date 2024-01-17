#User function Template for python3
import sys

sys.setrecursionlimit(10**8)

import bisect


class Solution:
	def maxSumIS(self, arr, n):
		# code here
		
		
		def solveMem(i, prev):
		    
		    if i==n:
		        return 0
		    
		    if dp[i][prev+1]!=-1:
		        return dp[i][prev+1]
		    
		    inc=0
		    if prev==-1 or arr[i]>arr[prev]:
		        inc=arr[i]+solveMem(i+1, i)
		        
	        exc=solveMem(i+1, prev)
	        
	        
	        
	        dp[i][prev+1]= max(inc, exc)
	        return dp[i][prev+1]
	        
	        
	        
        def solveTab():
            dp=[[0]*(n+1) for _ in range(n+1)]
            
            for i in range(n-1, -1, -1):
                for prev in range(n-2, -2, -1):
                    
                    inc=0
        		    if prev==-1 or arr[i]>arr[prev]:
        		        inc=arr[i]+dp[i+1][i+1]
    		        
        	        exc=dp[i+1][prev+1]
        	        
        	        
        	        
        	        dp[i][prev+1]= max(inc, exc)
        	        
	        return dp[0][0]
	        
        def solveOpt():
            curr=[0]*(n+1)
            next=[0]*(n+1)
            
            for i in range(n-1, -1, -1):
                for prev in range(n-2, -2, -1):
                    
                    inc=0
        		    if prev==-1 or arr[i]>arr[prev]:
        		        inc=arr[i]+next[i+1]
    		        
        	        exc=next[prev+1]
        	        
        	        
        	        
        	        curr[prev+1]= max(inc, exc)
        	        
    	        next=curr[:]
        	        
	        return curr[0]
                    
        def solve(i):
        
        
        
            if i==n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            
            ans = arr[i]
            for j in range(i+1,n):
                # Check if the current element is greater than the previous element
                if arr[i]<arr[j]:
                    ans = max(ans, arr[i]+solve(j))
            dp[i] = ans
            return dp[i]
                
            
        # dp=[[-1]*n for _ in range(n)]
        # return solveMem(0, -1)
        
        
        # return solveTab()
        
        # return solveOpt()
        
        dp = [-1]*(n+1)
        ans = 0
        for i in range(n):
            # Find the maximum increasing subsequence sum starting from each element
            ans = max(ans, solve(i))
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends