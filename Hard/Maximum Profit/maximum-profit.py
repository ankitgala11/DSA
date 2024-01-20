#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        def solveOpt():
            
            next=[[0]*(K+1) for _ in range(2)]
            curr=[[0]*(K+1) for _ in range(2)]
            
            for i in range(N-1, -1, -1):
                for buy in range(2):
                    for k in range(1, K+1):
                       
                
                        if buy:
                            
                            inc=-A[i]+next[0][k]
                            exc=next[1][k]
                            
                        else:
                            
                            inc=A[i]+next[1][k-1]
                            exc=next[0][k]
                            
                            
                            
                        curr[buy][k] = max(inc, exc)
                        
                    
                next=curr[:]
                        
                        
            return curr[1][K]
                        
                        
            
        # dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        # return solve(0, 1, 2)
        
        # return solveTab()
        
        return solveOpt()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends