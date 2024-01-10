#User function Template for python3

class Solution:
	def isBipartite(self, V, adj):
		#code here
		
# 		if even cycle then it is bipartite
		
# 		if odd cycle never a bipartite
		
# 		if linear graph then bipartite
		
		
		
# 		bfs O(V + E)

        def bfs(i, c):

        
            q=[i]
            
            color[i]=c
            
            while q:
                
                i = q.pop(0)
                
                
                for nbr in adj[i]:
                    
                    if color[nbr]==-1:
                        
                        color[nbr]=not color[i]
                        q.append(nbr)
                        
                        
                        
                    else:
                        if color[nbr]==color[i]:
                            return False
                        
    
            return True



		
# 		dfs O(v+e)
# 		def dfs(i, c):
		    
# 		    color[i]=c
		    
		    
# 		    for nbr in adj[i]:
		        
# 		        if color[nbr]==-1:
# 		            if dfs(nbr , not c) == False:
# 		                return False
		            
		            
# 	            else:
# 	                if color[nbr]==c:
# 	                    return False
	                    
	                    
                    
                    
#             return True
		    
		    
		    
	    
	    color=[-1]*V
	    
	    for i in range(V):
	        
	        if color[i]==-1:
	            if bfs(i, 0)==False:
	                return False
	           # if dfs(i, 0)==False:
	           #     return False
	                
	                
        return True

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