#User function Template for python3

class Solution:
    def longestSubsequence(self, N, A):
        # code here

        def solveMem(i , prev):
            if i>=N:
                return 0
                
            if dp[i][prev]!=-1:
                return dp[i][prev]
                
                
            inc=0
            if prev==-1 or abs(A[i]-A[prev])==1:
                inc=1+solveMem(i+1, i)
                
            exc=solveMem(i+1, prev)
            
            dp[i][prev]=max(inc, exc)
            return dp[i][prev]
            
            
            
        def solveTab():
            dp=[[0]*(N+1) for _ in range(N+1)]
            
            for i in range(N-1, -1, -1):
                for prev in range(N-2 ,-2, -1):
                    
                    inc=0
                    if prev==-1 or abs(A[i]-A[prev])==1:
                        inc=1+dp[i+1][i+1]
                        
                    exc=dp[i+1][prev+1]
                    
                    dp[i][prev+1]=max(inc, exc)
                    
            return dp[0][0]
        
        def solveOpt():
            next=[0]*(N+1) 
            curr=[0]*(N+1) 
            
            for i in range(N-1, -1, -1):
                for prev in range(N-2 ,-2, -1):
                    
                    inc=0
                    if prev==-1 or abs(A[i]-A[prev])==1:
                        inc=1+next[i+1]
                        
                    exc=next[prev+1]
                    
                    curr[prev+1]=max(inc, exc)
                next=curr[:]    
            return curr[0]
            
        def solve():
            lst=[1]*N
        
        # iterate backwards through the list
            for i in range(len(A)-1,-1,-1):
                for j in range(i+1,len(A)):
                    # if the absolute difference between A[i] and A[j] is 1,
                    # update lst[i] to be the maximum value between lst[i] and 1+lst[j]
                    if abs(A[i]-A[j])==1:
                        lst[i]=max(lst[i],1+lst[j])
            
            # return the maximum value in lst
            return max(lst)
            
  
        # dp=[[-1]*N for _ in range(N)]
        # return solveMem(0, -1)
        
        # return solveTab()
        
        # return solveOpt()
        
        return solve()
        
 

                
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))
# } Driver Code Ends