#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		
		
		def solve(i , cnt):
		    
		    if i >= n:
		      #  print(path)
		        return 0
		    
		    if dp[i][cnt]!=-1:
		        return dp[i][cnt]
		     
	       
		    if not cnt:
                # path.append(arr[i])
		        
    	        inc=arr[i]+(solve(i+2, 1))
    	       # path.pop()
    	        exc= solve(i+1,  1)
    	        
    	        
	        else:
	           # path.append(arr[i])
	            inc = arr[i]+(solve(i+1, cnt-1))
                # path.pop()
	            exc = solve(i+1,  cnt)
                
                
            dp[i][cnt]= max(inc, exc)
	        return dp[i][cnt]
	        
        # path=[]
        
        def solveTab():
	        dp=[[0]*2 for _ in range(n+2)]   

	            
            for i in range(n-1, -1 , -1):
                
                for cnt in range(1, -1, -1):
                    
                    if not cnt:
            	        inc=arr[i]+ dp[i+2][1]
            	       # path.pop()
            	        exc= dp[i+1][1]
            	        
            	        
        	        else:
        	           # path.append(arr[i])
        	            inc = arr[i]+dp[i+1][cnt-1]
                        # path.pop()
        	            exc = dp[i+1][cnt]
                        
                        
                    dp[i][cnt]= max(inc, exc)
	        return dp[0][1]
                    
                    
            
	   # dp=[[-1]*2 for _ in range(n)]    
    #     return solve(0, 1)
    
        return solveTab()


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends