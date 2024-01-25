#User function Template for python3

class Solution:
	def solveWordWrap(self, nums, k):
		#Code here
		
	
		
		def solve(i, rem):
		    
		    
		    if i>=n:
		        return 0
		        
		    if dp[i][rem]!=-1:
		        return dp[i][rem]
	        
	        ans=0
	        
	       # taking the prev line cost while moving ahead 
	       #this also ensures we wont take last line cost
	        
	        if nums[i]>rem:
	            ans=(rem+1)*(rem+1) + solve(i+1, k-nums[i]-1)
	            
            # taking both options in else because if we dont take it will solve like greedy approach
            # jagah hai toh daal do
            
            else:   
                same=solve(i+1 , rem-nums[i]-1)
                next=(rem+1)*(rem+1) + solve(i+1, k-nums[i]-1)
                
                
                
                ans=min(same, next)
                
                
            dp[i][rem]=ans
            return dp[i][rem]
            
        n=len(nums)    
        dp=[[-1]*(k+1) for _ in range(n)]    
        return solve(0, k)
                
		        
		        
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends