import sys
sys.setrecursionlimit(10**8)

class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		
# 		print(adj)

		degree=[0]*V
		
		for i in range(V):
		    for j in adj[i]:
		        degree[i]+=1
        
        
        def dfs(i):
            
            vis.add(i)
            
            for nbr in adj[i]:
                if nbr not in vis:
                    dfs(nbr)
                    
                    
        vis=set()
        dfs(0)
        for i in range(1, V):
            if i not in vis:
                if degree[i]!=0:
                    return 0
                
                
        cnt=0
        for i in degree:
            
            if i&1:
                cnt+=1
                
            
        if cnt==0:
            return 2
        elif cnt==2:
            return 1
            
        else:
            return 0
        
            

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends