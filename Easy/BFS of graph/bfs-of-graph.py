#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        vis=set()
        ans=[]
        q=[]
        
        
        def bfs(i):
            q.append(i)
            
            while q:
                curr=q.pop(0)
                ans.append(curr)
                
                for nbr in adj[curr]:
                    if nbr not in vis:
                        vis.add(nbr)
                        q.append(nbr)
                        
                        
            
        # Given in question to only consider nodes connected to 0 
        # hence no for loop here
        
        # for i in range(V):
        #     if i not in vis:
        vis.add(0)
        bfs(0)
                
        
        return ans
                


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends