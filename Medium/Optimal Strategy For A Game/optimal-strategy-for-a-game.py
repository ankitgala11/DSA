#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,arr, n):
        # code here
      
        def solve(i, j):
            # if i==j:
            #     return arr[i]
            if i>=j:
                return 0
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
                
            left=arr[i]+min(solve(i+2, j),solve(i+1, j-1))
                
            # if arr[i+1]>arr[j]:
            #     left=arr[i] + solve(i+2, j)
            # else:
            #     left=arr[i] + solve(i+1, j-1)
                
            right=arr[j]+min(solve(i+1, j-1),solve(i, j-2))
                
            # if arr[i]>arr[j-1]:
            #     right=arr[j] + solve(i+1, j-1)
            # else:
            #     right=arr[j] + solve(i, j-2)
                
            
            
            
            dp[i][j]= max(left, right)
            return dp[i][j]
            
            
        dp=[[-1]*n for i in range(n)] 
        return solve(0, n-1)


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
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(arr,n))

# } Driver Code Ends