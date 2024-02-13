import copy

class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		def issafe(i, j):
		    
		    if i<n and i>=0 and j<m and j>=0 and image[i][j]==initial and ans[i][j]!=newColor:
		        return True
	        return False
		    
		    
		    
		    
		row=[1,-1,0,0]
		col=[0, 0, 1, -1]
		
		
		n=len(image)
		m=len(image[0])
		
		q=[(sr, sc)]
		ans=copy.deepcopy(image)
		
		initial=image[sr][sc]
		ans[sr][sc]=newColor
		while q:
		    
		    r,c=q.pop(0)
		    
		    for i in range(4):
		        
		        newr=r+row[i]
		        newc=c+col[i]
		        
		        
		        if issafe(newr, newc):
                    ans[newr][newc]=newColor
		            q.append((newr, newc))
		            
		            
		            
		            
	            
        return ans
		            
		            
		            
		    
		    
		



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends