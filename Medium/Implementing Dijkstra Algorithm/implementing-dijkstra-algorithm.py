import heapq

class Solution:
    


    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        #  O(E * log V)
        dist=[float('inf')]*V
        dist[S]=0
        vis=set()
        minheap=[]
        heapq.heappush(minheap, (0, S))
        
        
        while minheap:
            
            
            
            d , i=heapq.heappop(minheap)
            if i in vis:continue
            
            vis.add(i)
            
            for temp in adj[i]:
                nbr=temp[0]
                dis=temp[1]
            
                if nbr not in vis and dist[nbr]>d+dis:
                    dist[nbr]=dist[i]+dis
                    heapq.heappush(minheap, (dist[nbr], nbr))
                
                
                
        return dist
                    
            
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends