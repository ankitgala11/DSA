#User function Template for python3

class Solution:
	def minSteps(self, m, n, d):
		# Code here
		
		q=[(0, 0)]
		

		
		vis=set()
		vis.add((0, 0))
		
		step=0
		
		while q:
		    
		    for z in range(len(q)):
		        
		        x, y=q.pop(0)
		        
		        
		        if x==d or y==d:
		            return step
		            
	            if (0, y) not in vis:
		            vis.add((0 ,y))
		            q.append((0 , y))
	                
	                
                if (x, 0) not in vis:
		            vis.add((x , 0))
		            q.append((x , 0))
		            
		            
		            
		        if (x, n) not in vis:
		            vis.add((x, n))
		            q.append((x, n))
		            
		        if (m, y) not in vis:
		            vis.add((m ,y))
		            q.append((m , y))
		            
	            
	            if (x-min(x, n-y) , y+min(x, n-y)) not in vis:
	                vis.add( (x-min(x, n-y) , y+min(x, n-y)) )
	                q.append( (x-min(x, n-y) , y+min(x, n-y)) )
	            
	            if (x+min(m-x, y) , y-min(m-x, y)) not in vis:
	                vis.add( (x+min(m-x, y) , y-min(m-x, y)) )
	                q.append( (x+min(m-x, y) , y-min(m-x, y)) )
		            
		            
		            
	            
		            
		            
		            
                  
            step+=1 


		            
                    
		            
		            
		            
		        
		        
		        
		    
		    
                
		    
		   
		     
		    
	    return -1
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n, d = map(int,input().strip().split())
		ob = Solution()
		ans = ob.minSteps(m, n, d)
		print(ans)
# } Driver Code Ends