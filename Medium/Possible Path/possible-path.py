#User function Template for python3

class Solution:
	def isPossible(self, paths):
        '''
        ------------------------------------
        
        Just check if Graph contains Eulers circuit or not.
        
        If every node in a graph has even degree then it contains eulers circuit
        		
        ------------------------------------
		
		
		 
		Euler Circuit is a graph where you can travel from one node and return back to the same node 
		by exactly visiting all the edges once
		(All nodes even degree)
		
		A----B----C    A->B->C->E->B->D->A   F
	    |   / \   |
		|  /   \  |     
		| /     \ |
		 D        E  
		 
		    
		    F
		
		
		
		If you can start from one node and visit all the edges, but cannot return back to the starting
		node, it is called as semi euler circuit 
		(Here degree of the starting and ending node will be odd, 
		whereas all other nodes will be even)
		
		
		A----B----C    A->B->C->E->B   F
              \   |
		       \  |
		        \ |
		 F       E  
		
		A single vertex with no edges is always a euler circuit
		
        '''
		
		for i in range(n):
		    c=0
		    for j in range(n):
		        
		        if paths[i][j]==1:
		            c+=1
            
            if c&1:
                return 0
                
        return 1
       
	                
		    
		    
		    
	    

	    
	    
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		paths = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			paths.append(cur)
		obj = Solution()
		ans = obj.isPossible(paths)
		print(ans)

# } Driver Code Ends