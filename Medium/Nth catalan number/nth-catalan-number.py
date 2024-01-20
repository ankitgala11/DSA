import sys
sys.setrecursionlimit(10**8)

mod=10**9+7

class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        
        def solveMem(n):
            
            if n<=1:
                return 1
                
            if dp[n]!=-1:
                return dp[n]
                
            ans=0    
            for i in range(1, n+1):
                
                ans+=solveMem(n-i) * solveMem(i-1)
            dp[n]=ans%mod    
            return dp[n]
            
        def solveTab():
            N=n
            dp=[0]*(N+1)
            
            dp[0]=1
            dp[1]=1
            
            for n in range(2, N+1):
                ans=0    
                for i in range(1, N+1):
                    
                    ans+=solveMem(n-i) * solveMem(i-1)
                dp[n]=ans%mod     
                
                
            return dp[N]
                
                
                
                
                
            
        
        dp=[-1]*(n+1)
        return solveMem(n)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends