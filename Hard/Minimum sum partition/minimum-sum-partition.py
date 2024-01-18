#User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        # code here
        
        def solve(i,s):
            nonlocal mini
            
            if i>=n:
                return 
            
            if dp[i][s]!=float('inf'):
                return dp[i][s]
                
             
            
            solve(i+1, s+arr[i])
            solve(i+1, s)
            
            
            dp[i][s]=min(mini, abs(abs(s) - abs(total-s)))
            
            
                
        
        
        total=sum(arr)
        
        mini=float('inf')
        dp=[[float('inf')]*total for _ in range(n)]
        solve(0, 0)
        
        for i in dp:
            mini=min(mini, min(i))
            
        return mini





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends