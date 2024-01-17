#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        
        def solveMem(i, j):
            
            if i==x or j==y:
                return 0
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
            if s1[i]==s2[j]:
                dp[i][j]= 1+solveMem(i+1, j+1)
                return dp[i][j]
                
            else:
                dp[i][j]= max(solveMem(i, j+1) , solveMem(i+1, j))
                return dp[i][j]
                
                
        def solveTab():
            dp=[[0]*(y+1) for _ in range(x+1)]
            
            for i in range(x-1, -1, -1):
                for j in range(y-1, -1, -1):
                    
                    if s1[i]==s2[j]:
                        dp[i][j]= 1+dp[i+1][j+1]
                        
                    else:
                        dp[i][j]= max( dp[i][j+1] , dp[i+1][j] )
            
            return dp[0][0]
                
        # dp=[[-1]*y for _ in range(x)]    
        # return solveMem(0, 0)
        
        return solveTab()


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends