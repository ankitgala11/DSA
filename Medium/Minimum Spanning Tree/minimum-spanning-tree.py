#User function Template 
from collections import defaultdict
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        # prim
        adjL=defaultdict(list)
        
        for i in range(V):
            for j in adj[i]:
                adjL[i].append(j)
        
        vis=[0]*V
        parent=[-1]*V
        dist=[float('inf')]*V
        
        dist[0]=0
        # print(adjL)
        for i in range(V-1):
            
            mini=float('inf')
            midx=0
            
            for j in range(V):
                if vis[j]!=1 and dist[j]<mini:
                    mini=dist[j]
                    midx=j
                    
            
            vis[midx]=1
            
                    
            
            for nbr in adjL[midx]:
                if vis[nbr[0]]!=1 and dist[nbr[0]]>nbr[1]:
                    # dist[nbr[0]]=dist[midx]+nbr[1]
                    dist[nbr[0]]=nbr[1]
                    parent[nbr[0]]=midx
                    
            
        
        # print(parent , dist, sep="\n")
        ans=0
        for i in range(V):
            if parent[i]==-1:continue
        
            for nbr in adj[i]:
                if nbr[0]==parent[i]:
                    ans+=nbr[1]
                    
                    
        return ans
        # ans=0
        # for i in range(V):
        #     ans+=dist[i]
                    
                    
        # return ans
      
        
        
            
            
                    
                
                
        
        
        
        
        
        
        
        
        # Kruskal
        # def par(i):
        #     if parent[i]==i:
        #         return i
                
        #     parent[i]=par(parent[i])
        #     return parent[i]
            
            
        # def union(x, y):
        #     if rank[x]>rank[y]:
        #         parent[y]=x
        #     elif rank[x]<rank[y]:
        #         parent[x]=y
                
        #     else:
        #         rank[x]+=1
        #         parent[y]=x
                
                
                
        # # [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]        
            
            
        # adjL=[]
        # for i in range(V):
        #     for j in adj[i]:
        #         adjL.append([i, j[0], j[1]])
        
        # adjL.sort(key=lambda x:x[2])
        # # print(adjL)
        
        
        # parent=[0]*V
        # rank=[-1]*V
        
        # ans=0
        
        # for i in range(V):
        #     parent[i]=i
            
      
        
        # for i in adjL:
        #     u=i[0]
        #     v=i[1]
        #     wt=i[2]
            
            
        #     u=par(u)
        #     v=par(v)
            
        #     if u!=v:
        #         union(u, v)
        #         ans+=wt
                
                
        # return ans
                
        


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
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends