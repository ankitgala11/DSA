from typing import List
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def minCashFlow(self, n : int, g : List[List[int]]) -> List[List[int]]:
        # code here
    
            
            
        def maxdebt(sol):
            
            val=float('inf')
            idx=0
            
            for i in range(n):
                if sol[i]<val:
                    val=sol[i]
                    idx=i
                    
                    
            return idx
            
        def maxcred(sol):
            
            val=float('-inf')
            idx=0
            
            for i in range(n):
                if sol[i]>val:
                    val=sol[i]
                    idx=i
                    
                    
            return idx
                    
       
        
        
        
        def solve(debt , cred):
            
            if sol[debt] == 0 and sol[cred] == 0:
                return
            
            
            mini=min( abs(sol[debt]) , abs(sol[cred]) )
            
            ans[debt][cred]=mini
            
            
            sol[debt]+=mini
            sol[cred]-=mini
            
            debt=maxdebt(sol)
            cred=maxcred(sol)
            
            solve(debt, cred)
            
            
        
        sol=[0]*n
        
        for i in range(n):
            for  j in range(n):
                
                sol[i]+=g[j][i]-g[i][j]
                
        
        
        
        debt=maxdebt(sol)
        cred=maxcred(sol)
        
        ans=[[0]*n for _ in range(n)]
        
        solve(debt, cred)
        
        return ans
        
        
        
        
        
        
        
        
        
        



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


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        g=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.minCashFlow(n, g)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends