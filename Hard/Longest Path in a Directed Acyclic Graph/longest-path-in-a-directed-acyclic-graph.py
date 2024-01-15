from typing import List


from collections import defaultdict


class Solution:
    def maximumDistance(self, v : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        # code here
        
        # Find topo order 
        # Iterate through that 
        # if udhar se uske nbr tak jaane ke distance dist array mein kam hai isse toh update
        
        
        adj=defaultdict(list)
        
        for i in edges:
            adj[i[0]].append((i[1], i[2]))
            
            
            
            
            
        def topo(i):
            vis.add(i)
            
            for nbr in adj[i]:
                if nbr[0] not in vis:
                    topo(nbr[0])
                    
                    
            stack.append(i)
        
        
        vis=set()
        stack=[]
        
        for i in range(v):
            if i not in vis:
                topo(i)
                
                
        dist=[float('-inf')]*v
        
        dist[src]=0
        
        while stack:
            curr=stack.pop()
            
            if dist[curr]!=float('-inf'):
                
                for nbr in adj[curr]:
                    
                    if dist[nbr[0]]<dist[curr]+nbr[1]:
                        dist[nbr[0]]=dist[curr]+nbr[1]
                        
                        
        for i in range(v):
            if dist[i]==float('-inf'):
                dist[i]="INF"
                
                
        return dist
            
            
        
        
                
        
        
        



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
        
        v = int(input())
        
        
        e = int(input())
        
        
        src = int(input())
        
        
        edges=IntMatrix().Input(e, e)
        
        obj = Solution()
        res = obj.maximumDistance(v, e, src, edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends