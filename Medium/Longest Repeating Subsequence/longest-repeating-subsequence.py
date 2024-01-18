#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		
		def solve(i, j):
		    
		    if i>=n or j>=n:
		        return 0
		        
		        
	        if dp[i][j]!=-1:
	            return dp[i][j]
		        
	        
	        if s1[i]==s2[j] and i!=j:
	            
	            dp[i][j] = 1+solve(i+1, j+1)
	            
	            
            else:
                dp[i][j] = max(solve(i+1, j) , solve(i, j+1))
                
                
            return dp[i][j]
                
                
                
            
        



            		        
	        
		
		
		
		
		s1=str
		s2=str
		n=len(str)
		
		dp=[[-1]*n for _ in range(n)]
		return solve(0, 0)
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends