#User function Template for python3

class Solution:
	def isPossible(self, paths):
		# Code here
		
		n=len(paths)
		
# 		degree=[0]*n
		
		for i in range(n):
		    c=0
		    for j in range(n):
		        
		        if paths[i][j]==1:
		            c+=1
		            
            if c&1:
                return 0
                
        return 1
        
#         print(degree)
#         cnt=0
#         for i in degree:
#             if i&1:
#                 return 0
                
#             if i==0:
#                 cnt+=1
                
            
#         if cnt==n:return 1
        
		
		
		
# 		def dfs(i):
		    
# 		    vis.add(i)
		    
# 		    for nbr in range(n):
		        
# 		        if paths[i][nbr]==1 and nbr not in vis:
# 		            vis.add(nbr)
		            
# 		            dfs(nbr)
		                
		    
		    
		    
	    
# 	    vis=set()
# 	    dfs(0)
# 	   # print(degree, vis)
# 	    for i in range(n):
# 	        if i not in vis and degree[i]!=0:
# 	            return 0
            
#         return 1
	    
	    
                
            


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