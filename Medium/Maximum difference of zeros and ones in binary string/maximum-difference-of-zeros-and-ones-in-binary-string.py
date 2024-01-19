#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		
		temp=0
	        
	        
        res=-1
        
        for i in range(len(S)):
            if S[i]=='0':
    		    x=1
    	    else:
    	        x=-1
    	       
	        temp+=x 
	        temp=max(temp, x)
	        res=max(res, temp)
	        
	        
        if not res:return -1
        return res
    	        
	        
	       
    	        
    	        
    	        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends