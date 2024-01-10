class Solution:
	def isBipartite(self, V, adj):
		#code here
		def dfs(i, c):
		    
		    color[i]=c
		    
		    
		    for nbr in adj[i]:
		        
		        if color[nbr]==-1:
		            if dfs(nbr , not c) == False:
		                return False
		            
		            
	            else:
	                if color[nbr]==c:
	                    return False
	                    
	                    
                    
                    
            return True
		    
		    
		    
	    
	    color=[-1]*V
	    
	    for i in range(V):
	        
	        if color[i]==-1:
	            if dfs(i, 0)==False:
	                return False
	                
	                
        return True


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends