#User function Template for python3

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        # code here
        def dfs(i, parent):
            nonlocal timer 
            
            vis[i]=1
            
            
            low[i]=timer
            misc[i]=timer
            
            timer+=1
            
            
            for nbr in adj[i]:
                
                if nbr==parent:
                    continue
                
                if vis[nbr]==0:
                    
                    vis[nbr]=1
                    if dfs(nbr, i):
                        return 1
                    
                    low[i] = min( low[nbr] ,  low[i] )
                    
                    if ((i==c and nbr==d) or (i==d and nbr==c)) and low[nbr] > misc[i]:
                        return 1
                        
                        
                else:
                    
                    low[i] = min( low[i], misc[nbr])
                        
                
                
            
            
            
            
        vis=[0]*V
        misc=[-1]*V
        low=[-1]*V
        parent=-1
        
        timer = 0
        
        for i in range(V):
            if vis[i]==0:
                if dfs(i , -1):
                    return 1
                    
                
        return 0

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
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends