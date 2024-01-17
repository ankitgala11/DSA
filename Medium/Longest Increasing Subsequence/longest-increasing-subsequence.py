#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

import bisect

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        
        
        def solveMem(i, prev):
            
            if i==n:
                return 0
                
                
            if dp[i][prev+1]!=-1:
                return dp[i][prev+1]
                
            # inc
            inc=0
            
            if prev==-1 or a[i]>a[prev]:
                
                inc=1+solveMem(i+1, i)
            
            # exc
            exc=solveMem(i+1, prev)
            
            
            
            dp[i][prev+1]= max(inc, exc)
            return dp[i][prev+1]
            
        def solveTab():
            dp=[[0]*(n+1) for _ in range(n+1)]
            
            for i in range(n-1, -1, -1):
                for prev in range(n-1, -2, -1):
                    
                    
                    inc=0
            
                    if prev==-1 or a[i]>a[prev]:
                        
                        inc=1+dp[i+1][i+1]
                    
                    # exc
                    exc=dp[i+1][prev+1]
                    
                    
                    
                    dp[i][prev+1]= max(inc, exc)
                    

            return dp[0][0]
        
        def solveOpt():
            curr=[0]*(n+1) 
            next=[0]*(n+1) 
            
            for i in range(n-1, -1, -1):
                for prev in range(n-1, -2, -1):
                    
                    
                    inc=0
            
                    if prev==-1 or a[i]>a[prev]:
                        
                        inc=1+next[i+1]
                    
                    # exc
                    exc=next[prev+1]
                    
                    
                    
                    curr[prev+1]= max(inc, exc)
                    
                next=curr[:]

            return curr[0]
            
        
        def solve():
            
            temp=[a[0]]
            cnt=1
            
            
            for i in range(1, n):
                if temp[-1]<a[i]:
                    temp.append(a[i])
                    cnt+=1
                    
                else:
                    idx=bisect.bisect_left(temp, a[i])
                    temp[idx]=a[i]
         
       
                
            return cnt
                    
       
        # dp=[[-1]*(n) for _ in range(n)]
        # return solveMem(0,  -1)
        
        
        # return solveTab()
        
        # return solveOpt()
        
        return solve()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends