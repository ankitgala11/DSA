#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		
		pre=1
		suff=1
		
		ans=float('-inf')
		
		for i in range(n):
		    
		    
		    if pre==0:pre=1
		    if suff==0:suff=1
		    
		    pre*=arr[i]
		    suff*=arr[n-1-i]
		    
		    ans=max(ans, pre, suff)
		    
		    
    
        return ans
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends