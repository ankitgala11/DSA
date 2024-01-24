#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        
        l_a=len(A)
        l_b=len(B)
        l_c=len(C)
        
        if l_c!=l_a+l_b:
            return 0
        
        def solve(i, j, k):
            if i>=l_c:
                return True
            
            
            if dp[j][k]!=-1:
                return dp[j][k]
            
            q=0
            r=0
                
                
            if j<len(A) and C[i]==A[j]:
                q = solve(i+1, j+1, k)
                
            if k<len(B) and C[i]==B[k]:
                r = solve(i+1, j, k+1)
          
                
                
            dp[j][k] = q or r
            return dp[j][k]
                    
                    
                    
                
        dp=[[-1]*(l_b+1)  for _ in range(l_a+1)]         
        return solve(0, 0, 0)
                
                
                    
            
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends