# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        
        
        
        
        def solve(i , j):
            
            if i>=n or i<0:
                return 0
                
            if j==m-1:
                return M[i][j]
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
            op1 = M[i][j] + solve(i-1, j+1)
            op2 = M[i][j] + solve(i, j+1)
            op3 = M[i][j] + solve(i+1, j+1)
            
            dp[i][j] = max(op1, op2, op3)
            return dp[i][j]
        
        dp=[[-1]*(m) for _ in range(n)]
        ans=0
        for i in range(n):
            if M[i][0]!=0:
                ans=max(ans, solve(i, 0))
                
                
                
        return ans

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends