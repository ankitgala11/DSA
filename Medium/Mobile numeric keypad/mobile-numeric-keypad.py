#User function Template for python3
class Solution:
	def getCount(self, N):
		# code here
		
		mat=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
		
		
        def solve(i, j, n):
            
            if n==1:
                return 1
            
            if dp[i][j][n]!=-1:
                return dp[i][j][n]
            
            a=solve(i, j, n-1)
            
            b,c,d,e=0,0,0,0
            
            if i-1>=0 and mat[i-1][j]!=-1:
                b=solve(i-1, j, n-1)
                
            if i+1<4 and mat[i+1][j]!=-1:
                c=solve(i+1, j, n-1)
                
            if j-1>=0 and mat[i][j-1]!=-1:
                d=solve(i, j-1, n-1)
                
            if j+1<3 and mat[i][j+1]!=-1:
                e=solve(i, j+1, n-1)
                
                
            dp[i][j][n]= a+b+c+d+e
            return dp[i][j][n]
            
                
        dp=[[ [-1]*(N+1)  for _ in range(3)] for _ in range(4)]
        ans=0
        for i in range(4):
            for j in range(3):
                
                if mat[i][j]!=-1:
                    ans+=solve(i, j, N)
            
            
        return ans
        
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.getCount(N)
		print(ans)

# } Driver Code Ends