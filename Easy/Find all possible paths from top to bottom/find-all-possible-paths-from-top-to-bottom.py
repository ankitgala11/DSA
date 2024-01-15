
from typing import List
class Solution:
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        # code here
        
        ans=[]
        # vis=[[0]*m for _ in range(n)]
        
        
        def issafe(x, y):
            if x>=0 and x<n and y>=0 and y<m:
                return True
                
            return False
            
        def solve(x,y, path):
            if x==n-1 and y==m-1:
                path.append(grid[x][y])
                ans.append(path[:])
                path.pop()
                return
            
            path.append(grid[x][y])
            # vis[x][y]=1
            
            if issafe(x+1, y):
                solve(x+1,y,path)
                
            if issafe(x, y+1):
                solve(x,y+1,path)
            
            path.pop()
            # vis[x][y]=0
            
            
        
        solve(0, 0, [])
        return ans
        






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
        
        a=IntArray().Input(2)
        
        
        grid=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findAllPossiblePaths(a[0],a[1], grid)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends