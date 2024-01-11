from typing import List

from collections import defaultdict

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        
        
        # jiska indegree zero hota jaye uska time ans list mein update karte jao
        # uska ans uske parent ka ans + 1 hoga
        
        
        adj=defaultdict(list)
        for i in edges:
            adj[i[0]].append(i[1])
            
        indegree=[0]*(n+1)
        ans=[0]*(n+1)

        
        
        for i in adj:
            for j in adj[i]:
                indegree[j]+=1
                
            
        q=[]
        # print(indegree)
        for i in range(1, n+1):
            if indegree[i]==0:
                q.append(i)
                ans[i]=1
                
                
        while q:
            curr=q.pop(0)
            
            for nbr in adj[curr]:
                
                indegree[nbr]-=1
                
                if indegree[nbr]==0:
                    ans[nbr]=ans[curr]+1
                    q.append(nbr)
                
      
        
        return ans[1:]
        
        



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
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends