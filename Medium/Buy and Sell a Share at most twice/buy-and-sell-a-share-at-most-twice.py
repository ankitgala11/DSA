from typing import List
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        
        
        def solve(i, buy, k ):
            
            if i>=n:
                return 0
                
            if k==0:
                return 0
                
                
            if dp[i][buy][k]!=-1:
                return dp[i][buy][k]
                
            if buy:
                
                inc=-price[i]+solve(i+1, 0, k)
                exc=solve(i+1, 1, k)
                
            else:
                
                inc=price[i]+solve(i+1, 1, k-1)
                exc=solve(i+1, 0, k)
                
                
                
            dp[i][buy][k] = max(inc, exc)
            return dp[i][buy][k]
            
        def solveTab():
            dp=[[[0]*3 for _ in range(2)] for _ in range(n+1)]
            
            for i in range(n-1, -1, -1):
                for buy in range(2):
                    for k in range(1, 3):
                       
                
                        if buy:
                            
                            inc=-price[i]+dp[i+1][0][k]
                            exc=dp[i+1][1][k]
                            
                        else:
                            
                            inc=price[i]+dp[i+1][1][k-1]
                            exc=dp[i+1][0][k]
                            
                            
                            
                        dp[i][buy][k] = max(inc, exc)
                        
            return dp[0][1][2]
                        
                        
            
        # dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        # return solve(0, 1, 2)
        
        return solveTab()
                
                
                
            



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends