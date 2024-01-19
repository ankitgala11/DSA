#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
		# code here
		arr.sort()
		
		i=0
		j=0
		
		
		ans=0
		
		while j<n:
		    if arr[j]-arr[i]<=k:
		        j+=1
		        
	        else:
	            i+=1
	            
	            
            ans=max(ans, j-i)
            
            
            
        return n-ans
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends