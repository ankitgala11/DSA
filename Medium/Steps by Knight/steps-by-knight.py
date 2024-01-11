import sys
sys.setrecursionlimit(10**8)

class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		
		
# 		kabhi bhi koi src se dest min time mein pohochne ko bola toh --BFS-- it is
		
# Time Complexity: O(N^2), As in the worst case we have to check/Traverse
# all N2 positions/state of board.

# Space Complexity: O(N^2), Maintaining visited array takes O(N2) space.

		row=[-2, -1, 1, 2,  1,  2, -1, -2   ]
		col=[ 1,  2, 2, 1, -2, -1, -2 , -1  ]
		
        vis=[[0]*(N+1) for _ in range(N+1)]
        
        
		def issafe(i, j):
		    if i<=N and j<=N and i>=1 and j>=1 and vis[i][j]==0 :return True
		    
		    return False
		    
	    q=[(KnightPos[0], KnightPos[1], 0)]
	    vis[KnightPos[0]][KnightPos[1]]=1
	    
	    ans=float('inf')
	    
	    while q:
	        x, y, cnt=q.pop(0)
	        if x==TargetPos[0] and y==TargetPos[1] :
	            return cnt
	            
	            
	            
	        
	        for i in range(8):
	            newx=x+row[i]
	            newy=y+col[i]
	            
	            if issafe(newx, newy):
	                vis[newx][newy]=1
	                q.append((newx, newy, cnt+1))
	            
		    
	    return ans
		    
    # DFS DOES NOT WORK HERE
	   # def solve(i, j, cnt):
	   #     nonlocal ans
	   #     if cnt>=ans:return
	   #     if i==TargetPos[0] and j==TargetPos[1]:
	   #         ans=min(ans, cnt)
	   #         return
	        
	        
    #         vis[i][j]=1
	        
	   #     for x in range(8):
	   #         newi=i+row[x]
	   #         newj=j+col[x]
	            
	   #         if issafe(newi, newj):
	   #             solve(newi, newj, cnt+1)
	                
    #         vis[i][j]=0
    
        
#         ans=float('inf')
#         solve(KnightPos[0], KnightPos[1], 0)
		
# 		return ans


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends