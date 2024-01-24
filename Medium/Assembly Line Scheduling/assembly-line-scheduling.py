from typing import List
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def carAssembly(self, n : int, a : List[List[int]], T : List[List[int]], e : List[int], x : List[int]) -> int:
        # code here
        
        def solve(lane, i):
            if i==n-1:
                if lane==0:
                    return x[0]
                else:
                    return x[1]
                    
            
            if dp[lane][i]!=-1:
                return dp[lane][i]
            
            op1=a[lane][i+1] + solve(lane , i+1 )
            op2=a[not lane][i+1] + T[lane][i+1] + solve(1^lane , i+1)
            
            
            dp[lane][i]= min(op1, op2)
            return dp[lane][i]
            
            
        def solveTab():
            dp=[[0]*n for _ in range(2)]
            
            dp[0][n-1]=x[0]
            dp[1][n-1]=x[1]
            
            for i in range(n-2, -1, -1):
                for lane in range(2):
                    
                    op1=a[lane][i+1] + dp[lane][i+1]
                    op2=a[not lane][i+1] + T[lane][i+1] + dp[1^lane][i+1]
                    
                    
                    dp[lane][i]= min(op1, op2)
                    
                    
            
            return min( e[0]+a[0][0]+dp[0][0]  ,  e[1]+a[1][0]+dp[1][0] )
            
            
        # dp=[[-1]*n for _ in range(2)]
        # return min(e[0]+a[0][0]+solve(0, 0)  ,  e[1]+a[1][0]+solve(1, 0))
        
        
        return solveTab()



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



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
        
        
        a=IntMatrix().Input(2, 2)
        
        
        T=IntMatrix().Input(2, 2)
        
        
        e=IntArray().Input(2)
        
        
        x=IntArray().Input(2)
        
        obj = Solution()
        res = obj.carAssembly(n, a, T, e, x)
        
        print(res)
        

# } Driver Code Ends