#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        
        def solve(i, j, k):
            
            if i==n1 or j==n2 or k==n3:
                return 0
                
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
                
            if A[i]==B[j] and B[j]==C[k]:
                dp[i][j][k] = 1+solve(i+1, j+1, k+1)
                
                
            else:
                
                dp[i][j][k] =  max(solve(i+1, j, k), solve(i, j+1, k), solve(i, j, k+1))
                
            return dp[i][j][k]
        
        dp=[[[-1]*n3 for _ in range(n2)] for _ in range(n1)] 
        
        return solve(0, 0, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends