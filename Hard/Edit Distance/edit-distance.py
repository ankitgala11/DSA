import sys
sys.setrecursionlimit(10**8)

class Solution:
	def editDistance(self, s, t):
		# Code here
		n1=len(s)
		n2=len(t)
		
		
		def solveMem(i, j):
		    
		    if i==n1:
		        return n2-j
		        
	        if j==n2:
	            return n1-i
	            
	        if dp[i][j]!=-1:
	            return dp[i][j]
            
            if s[i]==t[j]:
                dp[i][j]= solveMem(i+1 , j+1)
                
                
            else:
                
                # delete
                op1=1+solveMem(i+1 , j)
                
                # insert
                op2=1+solveMem(i , j+1)
                
                # replace
                op3=1+solveMem(i+1 , j+1)
                
                dp[i][j]= min(op1, op2, op3)
                
            return dp[i][j]
                
        dp=[[-1]*n2 for _ in range(n1)]        
        return solveMem(0, 0)
	            
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends