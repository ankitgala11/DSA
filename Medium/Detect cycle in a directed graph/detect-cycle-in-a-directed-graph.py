#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        # -------------DFS------------------- O(V + E)
        vis=[0]*V
        path=[0]*V
        
        def dfs(i):
            vis[i]=1
            path[i]=1
            
            for nbr in adj[i]:
                if vis[nbr]!=1:
                    if dfs(nbr):
                        return True
                    
                elif path[nbr]==1:
                    return True
            
            
            
            
            path[i]=0
            return False
        
        for i in range(V):
            if vis[i]!=1:
                if dfs(i):
                    return True
                    
        return False
        
        
        
        # -------------BFS------------------- O(V + E)
        # indegree=[0]*V
        
        # for i in adj:
        #     for j in i:
                
        #         indegree[j]+=1
                
        # q=[]
        # cnt=0
            
        # for i in range(V):
        #     if indegree[i]==0:
        #         q.append(i)
                
                
        # while q:
        #     curr=q.pop(0)
        #     cnt+=1
            
        #     for nbr in adj[curr]:
        #         indegree[nbr]-=1
        #         if indegree[nbr]==0:
        #             q.append(nbr)
                              
                
        # if cnt==V:
        #     return False
        # return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends