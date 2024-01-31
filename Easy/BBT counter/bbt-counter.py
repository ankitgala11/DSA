#User function Template for python3
mod=10**9 + 7

class Solution:
    def countBT (self, h):
        # code here 
        def solve(h):
            
            if h==0 or h==1:
                return 1
                
            if dp[h]!=-1:
                return dp[h]
                
            dp[h]= ((solve(h-1)*solve(h-1))%mod + (solve(h-2)*solve(h-1))%mod + (solve(h-1)*solve(h-2))%mod)%mod
            return dp[h]
            
            
        dp=[-1]*(h+1)    
        return solve(h)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        h = int(input())
        
        ob = Solution()
        print(ob.countBT(h))
# } Driver Code Ends