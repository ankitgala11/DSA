#User function Template for python3

class Solution:
    def minimumCost(self, cost, n, W):
        # code here
        
        def solve(i, w):
            
            if i>=n or w<0:
                return float('inf')
                
            if w==0:
                return 0
            
            if dp[i][w]!=-1:
                return dp[i][w]
                
            inc=float('inf')
            exc=float('inf')
            if i+1<=w and cost[i]!=-1:
                inc=cost[i] + solve(i, w-(i+1))
                # print(inc, i, W)
                
            exc=solve(i+1, w)
            
            # print(inc, exc)
            dp[i][w]= min(inc, exc)
            return dp[i][w]
            
            
        dp=[[-1]*(W+1) for _ in range(n)]    
        ans= solve(0, W)
        
        if ans==float('inf'):return -1
        return ans
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,w = input().split()
		n,w = int(n),int(w)
		a = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minimumCost(a,n,w)
		print(ans)

# } Driver Code Ends