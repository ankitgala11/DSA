#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		
# 		O(2^n) O(2^n)

		def solve(i, op):
		    if i>=n:
		        if op:
		            ans.append(op)
		        return 
		    
		    op+=s[i]
	        inc=solve(i+1, op)
	        op=op[:-1]
	        
	        exc=solve(i+1, op)
	        
	        
        n=len(s)
        ans=[]
        solve(0, "")
        return sorted(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends