#User function Template for python3



class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code heref
		if not edges:return 0
		dist=[float('inf')]*(n)
		dist[edges[0][0]]=0
		
		
		
		for i in range(n-1):
		    for j in edges:
    		    u=j[0]
    		    v=j[1]
    		    wt=j[2]
    		    
    		  #  to check dist[u] not inf gives tle  god knows why
    		  #  if dist[u]!=float('inf') and dist[v]>dist[u]+wt:
    		  
    		    if dist[v]>dist[u]+wt:
    		        dist[v]=dist[u]+wt
		        
		       
        for j in edges:
            u=j[0]
		    v=j[1]
		    wt=j[2]
    		    
		    
		  #  to check dist[u] not inf gives tle  god knows why
		  #  if dist[u]!=float('inf') and dist[v]>dist[u]+wt:
		    if dist[v]>dist[u]+wt:
		        return 1
		        
        return 0
        
  

 
		        


#  # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends