#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        
        def dfs(i , j):
            
            
            if j>=N or j<0:
                return float('-inf')
            
            if i==N-1:
                return Matrix[i][j]
            
            if dp[i][j]!=-1:
                return dp[i][j]
                
            
            ldia=Matrix[i][j] + dfs( i+1, j-1)
                
            d= Matrix[i][j] + dfs(i+1, j )
                
            rdia=Matrix[i][j] + dfs(i+1, j+1 )
            
            
            dp[i][j]= max(ldia,d,rdia)
            return dp[i][j]
            
            
            
            
            
            
            
        
        dp=[[-1]*N for _ in range(N)]
        res=0
        for i in range(N):
            
            
            
            res=max(res, dfs(0, i))
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends