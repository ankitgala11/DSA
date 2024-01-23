#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,arr, n):
        # code here
      
        def solve(i, j):
            
            if i>=j:
                return 0
                
            if dp[i][j]!=-1:
                return dp[i][j]
                
            '''
            when things happen to you, assume the worst
            when you do things, you do the best
            '''
            
            
            
            # 30 10 2 
            
            # maine 30 uthaya
            
            # voh ya toh 10 utahayega toh muje 2 milega
            # ya 2 uthayega toh muje 10 milega
            
            # muje voh min dega so voh 10 le liya and muje 2 milla
            
            left=arr[i]+min(solve(i+2, j),solve(i+1, j-1))
                
                
            # Similarly yaha se ill check
            # maine 2 uthaya ...
            
            right=arr[j]+min(solve(i+1, j-1),solve(i, j-2))
                
            
            
            # aur un dono ka max is ans
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