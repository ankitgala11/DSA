from typing import List

import heapq
from collections import defaultdict


class Solution:
    def minimumEdgeReversal(self,edges : List[List[int]], n : int, m : int, src : int, dst : int) -> int:
        # code here
        
        adj=defaultdict(list)

        for i in edges:
            
            adj[i[0]].append((i[1], 0))
            adj[i[1]].append((i[0], 1))
            
            
    
        dist=[float('inf')]*(n+1)
        dist[src]=0
        
        minheap=[]
        
        heapq.heappush(minheap, (0, src))
        
        while minheap:
            
            d, curr=heapq.heappop(minheap)
            
          
            
            for nbr in adj[curr]:
                
                if dist[nbr[0]]>d+nbr[1]:
                    dist[nbr[0]]=d+nbr[1]
                
                    
                    heapq.heappush( minheap, ( dist[nbr[0]], nbr[0] ) )
                    
           
                    
        if dist[dst]!=float('inf'):
            return dist[dst]
        else:
            return -1
        
        
            
        



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
        n,m=map(int,input().split())
        edges=IntMatrix().Input(m,2)
        
        
        src = int(input())
        
        
        dst = int(input())
        
        obj = Solution()
        res = obj.minimumEdgeReversal(edges, n, m, src, dst)
        
        print(res)
        

# } Driver Code Ends