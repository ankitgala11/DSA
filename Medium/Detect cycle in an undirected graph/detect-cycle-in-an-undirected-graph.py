from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
# 		---------------------DFS--------------------------- O(V + E)
		vis=set()
		
		def dfs(i, parent):
	        vis.add(i)
	        for nbr in adj[i]:
	            if nbr not in vis:
		            if dfs(nbr, i):
		                return True
		            
                else:
                    if nbr!=parent:
                        return True
                        
            return False
		    
		    
		    
	    for i in range(V):
	        if i not in vis:
                if dfs(i, -1):
                    return True
            
        return False
        
        
        
# 		---------------------BFS--------------------------- O(V + E)
        # parent=[-1]*(V)
        # vis=set()
        # q=[]
        
    
            
        # for i in range(V):
            
        #     if i not in vis:
                
        #         q.append(i)
        #         vis.add(i)
                
        #         while q:
        #             curr=q.pop(0)
                    
        #             for nbr in adj[curr]:
                        
        #                 if nbr not in vis:
        #                     vis.add(nbr)
        #                     parent[nbr]=curr
        #                     q.append(nbr)
                            
        #                 else:
        #                     if parent[curr]!=nbr:return True
                            
                        
            
        # return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends