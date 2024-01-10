#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        
      
        
        # step 1    topo sort 
        def topo(i):
            
            vis.add(i)
            
            for nbr in adj[i]:
                
                if nbr not in vis:
                    topo(nbr)
                    
                    
            stack.append(i)
            
            
            
        stack=[]
        vis=set()
        
        for i in range(V):
            if i not in vis:
                
                topo(i)
                
            
        
        
        
        # step 2    transpose of adj
        
        adjTran=defaultdict(list)
        
        for i in range(len(adj)):
            for j in adj[i]:
                
                
                adjTran[j].append(i)
                
             
                
        # step 3      traverse and find number of components
        
        def dfs(i):
            vis.add(i)
            
            for nbr in adjTran[i]:
                
                if nbr not in vis:
                    dfs(nbr)
                    
                    
        
        ans=0
        vis.clear()
        while stack:
            i=stack.pop()
            if i not in vis:
                ans+=1
                dfs(i)
                
                
        
        return ans
            
            
            
            
        
        
        
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends