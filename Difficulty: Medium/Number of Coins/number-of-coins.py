#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
	def minCoins(self, coins, M, V):
		# code here
		
		def solve(i, V):
		    
		    if V==0:
		        return 0
		        
		    if V<0:
		        return float('inf')
		        
		    if i>=M:
		        return float('inf')
		        
	        if dp[i][V] != -1:
	            return dp[i][V]
	        
		    inc=float('inf')
		    if V>=coins[i]:
		        inc= 1 + solve(i, V-coins[i])
		    exc= solve(i+1, V)
		    
		
		    dp[i][V]= min(inc, exc)
		    return dp[i][V]
		    
		    
	    dp = [ [-1]*(V+1) for _ in range(M)]
	    
	    ans= solve(0, V)
	    if ans!=-1 and ans!= float('inf'):return ans
	    else:return -1
	    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends