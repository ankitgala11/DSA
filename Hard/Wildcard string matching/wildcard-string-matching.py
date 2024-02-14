#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def match(self, wild, pattern):
        # code here
        
        def solve(i, j):
            if i<0 and j<0:
                return True
                
            if i<0 and j>=0:
                return False
                
                
            if i>=0 and j<0:
                for p in range(i, -1, -1):
                    if wild[p]!='*':
                        return False
                        
                        
                return True
                
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if wild[i]==pattern[j] or wild[i]=='?':
                dp[i][j]= solve(i-1, j-1)
                
                
            elif wild[i]=='*':
                dp[i][j]= solve(i, j-1) or solve(i-1, j)
            
 
            else:
                dp[i][j]= False
                
            
            return dp[i][j]
            
            
        # need to convert to 1 based for tabular
        def solveTab():
            dp=[[0]*(m+1) for _ in range(n+1)]
            
            dp[0][0]=True
            
            for j in range(1 , n+1):
                if wild[j-1]=='*':
                    dp[0][j]=True
                else:
                    break
                    
            
            for i in range(1 ,n+1):
                for j in range(1 , m+1):
                    
                    if wild[i-1]==pattern[j-1] or wild[i-1]=='?':
                        dp[i][j]= dp[i-1][j-1]
                        
                        
                    elif wild[i-1]=='*':
                        dp[i][j]= dp[i][j-1] or dp[i-1][j]
                    
         
                    else:
                        dp[i][j]= False
                        
                    
            return dp[n][m]
                    
            
            
            
        n=len(wild)
        m=len(pattern)
        
        dp=[[-1]*m for _ in range(n)]
        
        return solve(n-1, m-1)
        
        # return solveTab()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends